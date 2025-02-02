from unittest import TestCase

from peewee import SqliteDatabase

from generate_tags import GeneratorTags, UpdatedTags


class TestGeneratorTags(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_db = SqliteDatabase(':memory:')

        # Bind the models to the test database
        cls.test_db.bind([UpdatedTags], bind_refs=False, bind_backrefs=False)

        # Initialize the GeneratorTags class with the test database
        cls.generator = GeneratorTags(cls.test_db)

    @classmethod
    def tearDownClass(cls):
        cls.test_db.drop_tables([UpdatedTags])
        cls.test_db.close()

    def test_update_tags_by_today(self):
        test_date = '2024-10-21'
        self.generator.update_tags_by_date(test_date)

    def test_update_tags_by_file(self):
        file_path = 'file_path.txt'
        self.generator.update_tags_by_file(file_path)