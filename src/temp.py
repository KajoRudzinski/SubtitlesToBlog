def concat_lines(list_of_lines: list) -> str:
    # tbd

    """Given a list of lines with subtitles
    returns a concatenated string of all non technical lines
    (like times, empty lines, subtitle ordinal positions)

    The example SRT is below inside --
    --
    1
    00:00:04,212 --> 00:00:09,432
    na pierwszą część wywiadu z Tomaszem Zarzyką,
    projektantem systemów informatycznych
    --
    It is a possibility that an actual subtitle line would be a number,
    hence I will only eliminate numbers when previous line is empty
    """
    text = ''
    current_line = ''
    previous_line = ''
    line_nr = 0
    for i in list_of_lines:
        line_nr = line_nr + 1
        # first two lines are technical
        if line_nr > 2:
            current_line = i
            pass
    return ''