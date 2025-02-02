#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import collections
import json
import logging
import os
import re
import sys
from datetime import datetime

import yaml
from openai import OpenAI
from peewee import MySQLDatabase, Model, CharField, CompositeKey

################################################################################################
# Constants
#
################################################################################################
BLOG_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
BLOG_DIR_SCRIPT = '/'.join([BLOG_DIR, 'scripts', 'generate_tags'])

BLOG_CONTENT_DIR = '/'.join([BLOG_DIR, 'contents', 'posts'])

BLOG_HOME_URL = 'https://blog.advenoh.pe.kr'

################################################################################################
# Functions
#
################################################################################################

db = MySQLDatabase(os.environ.get("RASBERRYPI_MYSQL_DATABASE"),
                   user=os.environ.get("RASBERRYPI_MYSQL_USER"),
                   password=os.environ.get("RASBERRYPI_MYSQL_PASSWORD"),
                   host=os.environ.get("RASBERRYPI_MYSQL_HOST"),
                   port=int(os.environ.get("RASBERRYPI_MYSQL_PORT")))


class UpdatedTags(Model):
    category = CharField(max_length=191)
    title = CharField(max_length=191)
    updated_at = datetime.now()

    class Meta:
        database = db
        table_name = 'updated_tags'
        primary_key = CompositeKey('category', 'title')
        indexes = (
            (('category', 'title', 'updated_at'), True),
        )


class GeneratorTags:
    def __init__(self, db):
        self.db = db
        self.db.connect()
        self.db.create_tables([UpdatedTags])  # Ensure the table exists

    def update_tags_by_file(self):
        '''
        Update tags by input file path (ex. folder or file)

        :return:
        '''
        logging.debug("update_tags_by_file")
        pass

    def update_tags_by_date(self, date):
        '''
        Generate tags for all today's blogs
        - 파일을 읽어서 tags 목록 생성하기
        - chatgpt를 이용해서 tags 생성하기
        - 업데이트 했다는 내용 db에 체크하기
        :return:
        '''

        index_md_files = self.__find_all_files_matched_by_date(BLOG_CONTENT_DIR, date)
        index_md_files = self.remove_already_stored_index_md_files(index_md_files)

        current_tags_per_file = self.__build_current_tags_per_file(index_md_files)

        chatgpt_tags_per_file = self.__build_chatgpt_tags(index_md_files)
        # chatgpt_tags_per_file = {}

        # merge current_tags_per_file and chatgpt_tags_per_file (make sure to delete duplicates)
        merged_tags_per_file = self.__merge_tags(current_tags_per_file, chatgpt_tags_per_file)

        # update tags in the index.md files
        self.__update_tags_in_index_md_files(merged_tags_per_file)

        # flag the db
        self.create_finance_tags(index_md_files)

    def __build_chatgpt_tags(self, index_md_files):
        tags_per_file = {}

        for file_path in index_md_files:
            link = self.__make_blog_link(file_path)
            tags = self.__generate_tags_from_chatgpt(link)
            tags_per_file[file_path] = tags
        return tags_per_file

    def __make_blog_link(self, filename):
        end_path = os.path.basename(os.path.dirname(filename))
        link = BLOG_HOME_URL + '/' + end_path + '/'
        return link

    def __build_current_tags_per_file(self, index_md_files):
        tags_per_file = {}

        for file_path in index_md_files:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                front_matter = content.split('---')[1]
                data = yaml.safe_load(front_matter)
                tags = data.get('tags', [])
                tags_per_file[f.name] = tags

        return tags_per_file

    def __generate_tags_from_chatgpt(self, link):
        '''
        Generate tags based on the content given blog post link
        :return:
        '''

        client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),
        )

        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "당신은 투자 전문가입니다"
                },
                {
                    "role": "user",
                    "content": "블로그 링크 내용 기반으로 추천할 태그를 추천해줘. 실제로 블로그 tag 목록에 추가할 거고 최소 20개 정도 추천해줘. 쉽게 파싱할 수 있도록 결과를 json 형태로 작성해줘. ex. '{tags:[\"투자\", \"투자전략\"]}'\n\nlink 주소:" + link + "\n\n"
                },
            ],
            model="gpt-4o-mini",
        )

        content = response.choices[0].message.content

        # Find the JSON part in the content
        json_start = content.find('```json')
        json_end = content.find('```', json_start + 1)
        json_str = content[json_start + 7:json_end].strip()

        # Parse the JSON data
        tags = json.loads(json_str)
        return tags['tags']

    def __find_all_files_matched_by_date(self, folder, today_date):
        index_md_files = []

        for root, dirs, files in os.walk(folder):
            for file in files:
                if file == 'index.md':
                    # get the date from the file
                    with open(os.path.join(root, file), 'r') as f:
                        lines = f.readlines()
                        for line in lines:
                            if re.match(r'^date: ', line):
                                date = line.split(': ')[1].strip()
                                if date == today_date:
                                    index_md_files.append(os.path.join(root, file))
        return index_md_files

    def __merge_tags(self, current_tags_per_file, chatgpt_tags_per_file):
        merged_tags_per_file = {}

        for file_path in current_tags_per_file:
            current_tags = current_tags_per_file.get(file_path, [])
            chatgpt_tags = chatgpt_tags_per_file.get(file_path, [])

            # Convert all tags to lowercase for case-insensitive comparison
            all_tags = [tag.lower() for tag in current_tags + chatgpt_tags]

            # Remove duplicates while preserving order
            merged_tags = list(collections.OrderedDict.fromkeys(all_tags))

            # merged_tags = list(set(current_tags + chatgpt_tags))
            merged_tags_per_file[file_path] = merged_tags

        return merged_tags_per_file

    def __update_tags_in_index_md_files(self, merged_tags_per_file):
        for file_path in merged_tags_per_file:
            tags = merged_tags_per_file[file_path]
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Split the content to get the front matter
            parts = content.split('---')
            if len(parts) < 3:
                continue  # Invalid front matter format

            front_matter = parts[1]
            body = '---'.join(parts[2:])

            # Manually update the tags in the front matter
            lines = front_matter.split('\n')
            new_lines = []
            in_tags_section = False
            for line in lines:
                if line.strip().startswith('tags:'):
                    in_tags_section = True
                    new_lines.append('tags:')
                    for tag in tags:
                        new_lines.append(f'  - {tag}')
                elif in_tags_section and (line.strip() == '' or not line.startswith('  -')):
                    in_tags_section = False
                    new_lines.append(line)
                elif not in_tags_section:
                    new_lines.append(line)

            new_front_matter = '\n'.join(new_lines)

            # Reconstruct the content with the updated front matter
            new_content = f'---{new_front_matter}---{body}'

            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)

    def create_finance_tags(self, index_md_files):
        """Insert a new record into updated_tags table."""
        for file_path in index_md_files:
            category, title = self.__get_category_and_title_path(file_path)

            with self.db.atomic():  # Ensure transaction safety
                UpdatedTags.create(
                    category=category,
                    title=title,
                    updated_at=datetime.now()
                )

    def remove_already_stored_index_md_files(self, index_md_files):
        """ Retrieve all records from the updated_tags table."""
        stored_index_md_files = []

        for file_path in index_md_files:
            category, title = self.__get_category_and_title_path(file_path)
            updated_tag = UpdatedTags.get_or_none(category=category, title=title)
            if updated_tag is None:
                stored_index_md_files.append(file_path)

        return stored_index_md_files

    def __get_category_and_title_path(self, file_path):
        category = os.path.basename(os.path.dirname(os.path.dirname(file_path)))
        title_path = os.path.basename(os.path.dirname(file_path))
        return category, title_path


################################################################################################
# Main function
#
################################################################################################


def main():
    parser = argparse.ArgumentParser(description="Generate tags for blog posts")

    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument("-f", "--file", action='store', help="file path")
    group.add_argument("-t", "--today", action='store_true', help="generate tags for all today's blogs ")

    args = parser.parse_args()
    logging.debug("args: %s", args)

    # set the default command option
    if not args.file and not args.today:
        args.today = True

    if args.today:
        generator = GeneratorTags(db)
        today_date = datetime.now().strftime('%Y-%m-%d')
        # today_date = '2024-10-21'
        generator.update_tags_by_date(today_date)
    elif args.file:
        generator = GeneratorTags(db)
        generator.update_tags_by_file(args.file)


if __name__ == "__main__":
    fmt = '[%(asctime)s,%(msecs)d] [%(levelname)-4s] %(filename)s:%(funcName)s:%(lineno)d %(message)s'
    logging.basicConfig(format=fmt, level=logging.DEBUG,
                        datefmt='%Y-%m-%d:%H:%M:%S')
    sys.exit(main())
