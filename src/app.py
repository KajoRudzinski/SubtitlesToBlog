import subtitles_to_blog as stb

if __name__ == '__main__':
    stb.print_hello()
    file = stb.FileIO()
    file.choose_dir()
    subtitles = []
    if file.read_from_default_dir:
        file.get_def_dir_from_config_file()
        file.get_srt_file_from_path(file.default_dir)
        subtitles = file.get_line_list_from_srt()
    else:
        file.get_temp_dir_from_user()
        file.get_srt_file_from_path(file.temp_dir)
        subtitles = file.get_line_list_from_srt()

    lines = stb.LineConverter()
    lines.concat_lines(subtitles)

    file.save(lines.text)
# save file
