import os


class FileIO:
    def __init__(self):
        self.temp_directory = ''
        self.default_directory = 'C:\\'
        self.file_path = ''
        self.blog_post_file_name = 'blog_post.txt'
        self.line_list = []

    def get_srt_file_path(self, path: str):
        """Given a folder with SRT files containing subtitles
        assigns path to the first found SRT file to file_path"""
        for file in os.listdir(path):
            if file[-4:] == '.srt':
                self.file_path = os.path.join(path, file)
                break

    def get_line_list(self):
        """Given a file path to a SRT file
        assigns the list of lines in this file to line_list"""