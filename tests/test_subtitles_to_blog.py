from unittest import TestCase
from src import subtitles_to_blog as stb
import os

test_file = 'test.srt'
test_file_2 = 'test_2.srt'
lines_test_file = 'line_test.srt'


def create_line_test_file(f):
    with open(f, 'w') as file:
        file.write('1\n2')


def create_test_srt_file(f):
    with open(f, 'w', encoding='utf8') as file:
        file.write(
           '0\n' +
           '00:00:00,000 --> 00:00:04,132\n' +
           'line 1\n' +
           'line 2\n' +
           '\n' +
           '1\n' +
           '00:00:04,212 --> 00:00:09,432\n' +
           '1\n' +
           '2\n' +
           '\n' +
           '2\n' +
           '00:00:10,000 --> 00:00:14,132\n' +
           'line 1\n' +
           '\n' +
           '3\n' +
           '00:00:24,212 --> 00:00:29,432\n' +
           '1\n'
        )


def remove_test_files(f):
    try:
        os.remove(f)
    except FileNotFoundError:
        pass


class TestFileIO(TestCase):
    def test_init_temp_directory(self):
        self.assertEqual(stb.FileIO().temp_directory, '')

    def test_init_default_directory(self):
        self.assertEqual(stb.FileIO().default_directory, 'C:\\')

    def test_init_file_path(self):
        self.assertEqual(stb.FileIO().file_path, '')

    def test_init_file_name(self):
        self.assertEqual(stb.FileIO().blog_post_file_name, 'blog_post.txt')

    def test_init_line_list(self):
        self.assertEqual(stb.FileIO().line_list, [])

    def test_init_file_text(self):
        self.assertEqual(stb.FileIO().file_text, '')

    def test_get_srt_file_path_with_srt(self):
        global test_file
        global test_file_2
        create_test_srt_file(test_file)
        create_test_srt_file(test_file_2)
        f = stb.FileIO()
        f.get_srt_file_path(os.getcwd())
        self.assertEqual(
            f.file_path, os.path.join(
                os.getcwd(), test_file
            )
        )
        remove_test_files(test_file)
        remove_test_files(test_file_2)

    def test_get_srt_file_path_without_srt(self):
        f = stb.FileIO()
        f.get_srt_file_path(os.getcwd())
        self.assertEqual(f.file_path, '')

    def test_get_line_list(self):
        global lines_test_file
        create_line_test_file(lines_test_file)
        f = stb.FileIO()
        f.get_srt_file_path(os.getcwd())
        f.get_line_list()
        self.assertEqual(f.line_list, ['1', '2'])
        remove_test_files(lines_test_file)
