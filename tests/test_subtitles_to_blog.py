from unittest import TestCase
from src import subtitles_to_blog as stb


class TestFileIO(TestCase):
    def test_default_temp_directory(self):
        self.assertEqual(stb.FileIO().temp_directory, '')
