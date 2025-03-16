#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import logging
import os
import re
import shutil
import sys
from datetime import datetime
from itertools import islice

################################################################################################
# todo :

################################################################################################


################################################################################################
# Constants
#
################################################################################################
BLOG_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
BLOG_DIR_SCRIPT = '/'.join([BLOG_DIR, 'scripts', 'generate_readme'])

BLOG_CONTENT_DIR = '/'.join([BLOG_DIR, 'contents', 'posts'])
README_FILE = os.path.join(BLOG_DIR, 'README.md')
README_HEADER_FILE = '/'.join([BLOG_DIR_SCRIPT, 'data', 'HEADER.md'])

BLOG_HOME_URL = 'https://blog.advenoh.pe.kr'

################################################################################################
# Functions
#
################################################################################################

class Generator:
    def __init__(self):
        self.toc_map = {}

    def update_readme(self):
        for file in self.__get_all_files_with_extension(BLOG_CONTENT_DIR, ['md']):
            category = os.path.basename(os.path.dirname(os.path.dirname(file))).capitalize()
            title = self.__get_blog_title(file)

            if self.toc_map.get(category):
                self.toc_map[category].append({'title': title, 'filename': file})
            else:
                self.toc_map[category] = [{'title': title, 'filename': file}]

        count_posting_from_readme = self.__count_toc_from_readme(README_FILE)
        count_new_posting = self.__count_new_toc()

        logging.info("count # of posting. readme:%d, new:%d", count_posting_from_readme, count_new_posting)
        if count_new_posting > count_posting_from_readme:
            self.__write_blog_list_to_file()

    def __get_blog_title(self, filename):
        with open(filename, 'r') as f:
            for line in islice(f, 1, 2):
                return re.findall(r'title:\s*"([^"]+)"', line)[0]

    def __write_blog_list_to_file(self):
        shutil.copyfile(README_HEADER_FILE, README_FILE)

        # write header to the file
        with open(README_FILE, 'a') as out_file:
            out_file.write('\nUpdated ' + datetime.now().strftime('%Y-%m-%d') + '\n\n')
            out_file.write('현재 [블로그](https://blog.advenoh.pe.kr)에 작성된 내용입니다.\n\n')

            for category in sorted(self.toc_map):
                out_file.write('## {}\n'.format(category))

                for title_file in sorted(self.toc_map[category], key=lambda k: k['title']):
                    end_path = os.path.basename(os.path.dirname(title_file.get('filename')))
                    link = BLOG_HOME_URL + '/' + end_path + '/'
                    out_file.write('* [{}]({})\n'.format(title_file.get('title'), link))
                out_file.write('\n')

    def __get_all_files_with_extension(self, path, extensions):
        filenames_with_extension = []
        for (dirpath, dirnames, filenames) in os.walk(path):
            for filename in filenames:
                ext = os.path.splitext(filename)[-1]
                for extension in extensions:
                    if ext == '.' + extension:
                        filenames_with_extension.append(os.path.join(dirpath, filename))
        return filenames_with_extension

    def __count_toc_from_readme(self, filename):
        count = 0
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                if line.startswith('*'):
                    count += 1
        return count

    def __count_new_toc(self):
        count = 0
        for category in self.toc_map:
            count += len(self.toc_map[category])
        return count

################################################################################################
# Main function
#
################################################################################################


def main():
    parser = argparse.ArgumentParser(description="Generate TOC for README.md")

    parser.add_argument("-g", "--generate", action='store_true',
                        help="Generate blog list for my blog in the readme file")

    if len(sys.argv[1:]) == 0:
        parser.print_help()
        parser.exit()

    args = parser.parse_args()
    logging.debug("args: %s", args)

    if args.generate:
        generator = Generator()
        generator.update_readme()


if __name__ == "__main__":
    fmt = '[%(asctime)s,%(msecs)d] [%(levelname)-4s] %(filename)s:%(funcName)s:%(lineno)d %(message)s'
    logging.basicConfig(format=fmt, level=logging.INFO,
                        datefmt='%Y-%m-%d:%H:%M:%S')
    sys.exit(main())
