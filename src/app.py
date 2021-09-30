import os


def read_path(path: str):
    """Reads folder with SRT files containing subtitles
    and returns path to first found SRT file"""
    path_content = os.listdir(path)
    srt_file = ''
    for f in path_content:
        if f[-4:] == '.srt':
            srt_file = f
            break
    if srt_file != '':
        return os.path.join(path, srt_file)


def read_file(path: str) -> list:
    """Reads SRT file from path
    and returns a list of lines in this file"""
    line_list = []
    if path is not None:
        with open(path, 'r') as file:
            line_list = [(line.strip()) for line in file]
    return line_list


