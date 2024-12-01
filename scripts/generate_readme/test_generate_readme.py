import os
import re
from unittest import TestCase

from scripts import generate_readme


class MaintenanceTest(TestCase):
  def test_regex_sub(self):
    filename = '/Users/ykoh/WebstormProjects/blog.advenoh.pe.kr/src/content/spring/스프링부트-기본-오류-페이지-변경하기.md'
    print('os.path.splitext(filename)[0]', os.path.splitext(filename)[0])
    result = re.sub(generate_readme.REGEX_SUB_PATTERN, generate_readme.BLOG_HOME_URL, os.path.splitext(filename)[0])
    self.assertEqual(result, 'https://blog.advenoh.pe.kr/spring/스프링부트-기본-오류-페이지-변경하기')
