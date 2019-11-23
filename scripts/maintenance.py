#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import os
import re
import shutil
import sys
from itertools import islice

################################################################################################
# todo :
# README.md 파일에 블로그 목록을 추가하기
# master 브랜치에 cherry pick을 해야 함 - 자동으로 할 수 없는 방법은 없나?
################################################################################################


################################################################################################
# Constants
#
################################################################################################
BLOG_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
BLOG_CONTENT = '/'.join([BLOG_DIR, 'content', 'blog'])
README_FILE = os.path.join(BLOG_DIR, 'README.md')
README_HEADER_FILE = '/'.join([BLOG_DIR, 'scripts', 'data', 'HEADER.md'])
BLOG_HOME_URL = 'https://blog.advenoh.pe.kr'


################################################################################################
# Functions
#
################################################################################################

def generate_blog_list():
    result = {}
    for file in get_all_files_with_extension(BLOG_CONTENT, ['md']):
        category = os.path.basename(os.path.dirname(file))
        if result.get(category):
            result[category].append({'title': get_blog_title(file), 'filename': file})
        else:
            result[category] = [{'title': get_blog_title(file), 'filename': file}]
    print(result)
    write_blog_list_to_file(result, README_FILE)


def get_blog_title(filename):
    with open(filename, 'r') as f:
        for line in islice(f, 1, 2):
            return re.findall('title:\\s*\'(.*)\'', line)[0]


def write_blog_list_to_file(result, filename):
    '''
    ## Node
    * [Loopback 게시판 만들기 (1)](https://github.com/cheese10yun/blog-sample/tree/master/loopback-boards)

    :param filename:
    :return:
    '''
    shutil.copyfile(README_HEADER_FILE, README_FILE)

    # write header to the file
    with open(filename, 'a') as out_file:
        out_file.write('\n\n')
        for category, data in result.items():
            out_file.write('## {}\n'.format(category))
            for title_file in data:
                out_file.write('* [{}]({})\n'.format(
                    title_file.get('title'),
                    os.path.splitext(title_file.get('filename'))[0].replace(
                        '/Users/ykoh/WebstormProjects/advenoh.pe.kr/content/blog', BLOG_HOME_URL)
                ))

            out_file.write('\n')


def replace_pathname(org_str, repl_str):
    return str.replace(org_str, repl_str)


def get_all_files_with_extension(path, extensions):
    filenames_with_extension = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            ext = os.path.splitext(filename)[-1]
            for extension in extensions:
                if ext == '.' + extension:
                    filenames_with_extension.append(os.path.join(dirpath, filename))
    return filenames_with_extension


################################################################################################
# Main function
#
################################################################################################

def main():
    parser = argparse.ArgumentParser(description="Maintenance script for my blog")

    parser.add_argument("-g", "--generate", action='store_true',
                        help="Generate blog list for my blog in the readme file")

    if len(sys.argv[1:]) == 0:
        parser.print_help()
        parser.exit()

    args = parser.parse_args()

    print('args', args)

    if args.generate:
        generate_blog_list()


if __name__ == "__main__":
    sys.exit(main())
