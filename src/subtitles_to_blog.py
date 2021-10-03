import os


class FileIO:
    def __init__(self):
        self.temp_directory = ''
        self.default_directory = 'C:\\'
        self.file_path = ''
        self.blog_post_file_name = 'blog_post.txt'

    def get_srt_file_path(self, path: str):
        """Given a folder with SRT files containing subtitles
        sets file_path to path to the first found SRT file"""
        for file in os.listdir(path):
            if file[-4:] == '.srt':
                self.file_path = os.path.join(path, file)
                break
