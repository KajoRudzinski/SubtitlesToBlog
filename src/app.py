import os


def read_path(path: str) -> str:
    """Given a folder with SRT files containing subtitles
    returns path to first found SRT file"""
    path_content = os.listdir(path)
    srt_file = ''
    for f in path_content:
        if f[-4:] == '.srt':
            srt_file = f
            break
    if srt_file != '':
        return os.path.join(path, srt_file)


def read_file(path: str) -> list:
    """Given a file from path
    returns a list of lines in this file"""
    line_list = []
    with open(path, 'r') as file:
        line_list = [(line.strip()) for line in file]
    return line_list


def increment_by_1(i: int) -> int:
    return i + 1



