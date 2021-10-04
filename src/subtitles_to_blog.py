import os


class FileIO:
    def __init__(self):
        self.temp_dir = ''
        self.default_dir = ''
        self.file_path = ''
        self.blog_post_file_name = 'blog_post.txt'
        self.encoding = 'utf8'
        self.default_dir_file = 'default_dir.txt'
        self.read_from_default_dir = True

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
        with open(self.file_path, 'r', encoding=self.encoding) as file:
            return [(line.strip()) for line in file]

    def get_def_dir_from_config_file(self):
        """Reads default_dir.txt provided in src to
        assign default directory for SRT files to default_dir"""
        with open(self.default_dir_file, 'r', encoding=self.encoding) as file:
            self.default_dir = file.read()

    def print_dir_question(self):
        print(
            "\nDo you want to use the default directory" +
            " as defined in {}?".format(self.default_dir_file)
        )

    def get_user_input_on_preferred_dir(self):
        answer = ''
        question = "(y)es or (n)o?: "
        while answer != 'y' or answer != 'n':
            answer = input(question)
            if answer == 'y':
                self.read_from_default_dir = True
                break
            elif answer == 'n':
                self.read_from_default_dir = False
                break
            else:
                continue

    def get_temp_dir_from_user(self):
        self.temp_dir = input(
            'Provide temporary directory for this execution: '
        )

    def choose_dir(self):
        self.print_dir_question()
        self.get_user_input_on_preferred_dir()

    def check_dir_to_save(self):
        if self.read_from_default_dir:
            return os.path.join(
                self.default_dir,
                self.blog_post_file_name)
        else:
            return os.path.join(
                self.temp_dir,
                self.blog_post_file_name)

    def print_success(self):
        print(
            '\nSuccessfully saved to:\n{}'.format(self.check_dir_to_save())
        )

    @staticmethod
    def print_failure(self):
        print(
            'File NOT SAVED. Something went wrong :('
        )

    def save(self, text: str):
        try:
            with open(self.check_dir_to_save(), 'w') as file:
                file.write(text)
            self.print_success()
        except Exception:
            # I know it's broad
            # but in case of an error I haven't foreseen:
            self.print_failure()


class LineConverter:
    def __init__(self):
        self.line_list = []
        self.text = ''
        self.current_line = ''
        self.current_line_nr = 1

    @staticmethod
    def is_not_empty(s: str) -> bool:
        """Checks if string is empty"""
        return s != ''

    @staticmethod
    def is_not_timestamp(s: str) -> bool:
        """Checks if string contains characters
        suggesting it's a timestamp line"""
        return "-->" not in s

    @staticmethod
    def all_conditions_are_true(*args):
        return all([*args])

    def expand_text_with_new_line(self, line: str):
        self.text = self.text + line + ' '

    def go_to_next_line(self):
        self.current_line_nr = self.current_line_nr + 1

    def concat_lines(self, lines_list: list):
        """Given a list of strings
        returns one concatenated string of non technical ones"""
        for line in lines_list:
            if self.current_line_nr != 1:
                previous_line = self.current_line
                self.current_line = line
                if self.all_conditions_are_true(
                        self.is_not_empty(self.current_line),
                        self.is_not_empty(previous_line),
                        self.is_not_timestamp(self.current_line),
                        self.current_line_nr != 1
                ):
                    self.expand_text_with_new_line(self.current_line)
            self.go_to_next_line()


def print_hello():
    print("""
    >>> SubtitlesToBlog
    >>> Created by: Kajo Rudziński
    
    SubtitlesToBlog converts .srt files to .txt files
    in order to turn subtitles into almost ready blog post.
    """)