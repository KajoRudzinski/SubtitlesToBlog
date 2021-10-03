import os


class FileIO:
    def __init__(self):
        self.temp_directory = ''
        self.default_directory = 'C:\\'
        self.file_path = ''
        self.blog_post_file_name = 'blog_post.txt'

    def get_srt_file_from_path(self, path: str):
        """Given a folder with SRT files containing subtitles
        assigns path to the first found SRT file to file_path"""
        for file in os.listdir(path):
            if file[-4:] == '.srt':
                self.file_path = os.path.join(path, file)
                break

    def get_line_list_from_srt(self):
        """Given a file path to a SRT file
        returns the list of lines in this file"""
        with open(self.file_path, 'r', encoding='utf8') as file:
            return [(line.strip()) for line in file]


class LineConverter:
    def __init__(self):
        self.line_list = []
        self.text = ''
        self.current_line = ''
        self.current_line_nr = 1

    @staticmethod
    def is_not_empty(s: str) -> bool:
        """Checks if string is empty"""
        return s != ''

    @staticmethod
    def is_not_timestamp(s: str) -> bool:
        """Checks if string contains characters
        suggesting it's a timestamp line"""
        return "-->" not in s

    @staticmethod
    def all_conditions_are_true(*args):
        return all([*args])

    def expand_text_with_new_line(self, line: str):
        self.text = self.text + line + ' '

    def go_to_next_line(self):
        self.current_line_nr = self.current_line_nr + 1

    def concat_lines(self, lines_list: list):
        """Given a list of strings
        returns one concatenated string of non technical ones"""
        for line in lines_list:
            if self.current_line_nr != 1:
                previous_line = self.current_line
                self.current_line = line
                if self.all_conditions_are_true(
                        self.is_not_empty(self.current_line),
                        self.is_not_empty(previous_line),
                        self.is_not_timestamp(self.current_line),
                        self.current_line_nr != 1
                ):
                    self.expand_text_with_new_line(self.current_line)
            self.go_to_next_line()
