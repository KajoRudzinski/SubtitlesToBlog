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
