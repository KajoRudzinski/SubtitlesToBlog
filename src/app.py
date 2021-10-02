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
    """Increments int by 1"""
    return i + 1


def is_not_empty(s: str) -> bool:
    """Checks if string is empty"""
    return s != ''


def is_not_timestamp(s: str) -> bool:
    """Checks if string contains characters
    suggesting it's a timestamp line"""
    return "-->" not in s


def concat_lines(lines_list: list) -> str:
    """Given a list of strings
    returns one concatenated string of non technical ones"""
    text = ''
    current_line = ''
    line_nr = 1
    for line in lines_list:
        if line_nr != 1:
            previous_line = current_line
            current_line = line
            conditions = [
                is_not_empty(current_line),
                is_not_empty(previous_line),
                is_not_timestamp(current_line),
                line_nr != 1
            ]
            if all(conditions):
                text = text + current_line + ' '
        line_nr = increment_by_1(line_nr)
    return text

