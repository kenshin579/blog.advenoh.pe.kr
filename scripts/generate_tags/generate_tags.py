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

class GeneratorTags:
    def __init__(self):
        pass

    def update_tags(self):
        '''

        :return:
        '''
        pass

    def __generate_tags_from_chatgpt(self):
        '''

        :return:
        '''
        pass


################################################################################################
# Main function
#
################################################################################################


def main():
    parser = argparse.ArgumentParser(description="Generate tags for blog posts")

    parser.add_argument("-f", "--file", action='store', help="file path", required=False)
    parser.add_argument("-t", "--today", action='store_true', help="generate tags for all today's blogs ", required=False)

    if len(sys.argv[1:]) == 0:
        parser.print_help()
        parser.exit()

    args = parser.parse_args()
    logging.debug("args: %s", args)

    if args.today:
        generator = GeneratorTags()
        generator.update_tags()


if __name__ == "__main__":
    fmt = '[%(asctime)s,%(msecs)d] [%(levelname)-4s] %(filename)s:%(funcName)s:%(lineno)d %(message)s'
    logging.basicConfig(format=fmt, level=logging.INFO,
                        datefmt='%Y-%m-%d:%H:%M:%S')
    sys.exit(main())
