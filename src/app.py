import os


def read_path(path: str) -> str:
    """Reads folder with SRT files containing subtitles
    and returns path to first found SRT file"""
    path_content = os.listdir(path)
    srt_file = ''
    for f in path_content:
        if f[-4:] == '.srt':
            srt_file = f
            break

    if srt_file == '':
        return 'No SRT File'
    else:
        return os.path.join(path, srt_file)
