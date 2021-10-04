# SubtitlesToBlog
Python script that helps me convert YouTube subtitles (so .srt file) to a text file almost ready to post to Wordpress blog post.

By almost ready I mean:
- all techincal lines from subtitles are removed (line IDs, empty lines & timestamp lines)
- all lines are concatenated to one string (with spaces)

You can either choose to setup a default directory or provide a temporary one during the execution.
Execution is run for the first found .srt file in chosen directory. Text file is then saved to this directory as well.

In order run the script - run app.py in src folder.

Enjoy :)
