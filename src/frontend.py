import backend as b
import os

temp_path = ''
default_path = 'default_path.txt'
file_name = 'blog_post.txt'


def print_hello():
    print(
        "\nSubtitlesToBlog converts .srt files to .txt files\n" +
        "in order to turn subtitles into almost ready blog post.\n"
    )


def print_default_path_question():
    print(
        "Do you want to use the default path" +
        " as defined in {}?".format(default_path)
    )


def print_result(path: str):
    print(
        "The file {} ".format(file_name) +
        "was successfully saved to {}.".format(path)
    )


def print_closing_message():
    input(
        "\nThank you for using Subtitles To Blog!" +
        "\n\nPress any key to close"
    )


def print_default_path():
    with open(default_path, 'r') as p:
        print("[This is currently: " + p.read() + "]")


def print_initial_messages():
    print_hello()
    print_default_path_question()
    print_default_path()


def use_default_path() -> bool:
    answer = ''
    question = "(y)es or (n)o?: "
    while answer != 'y' or answer != 'n':
        answer = input(question)
        if answer == 'y':
            return True
        elif answer == 'n':
            return False
        else:
            continue


def define_temp_path() -> str:
    global temp_path
    answer = ''
    question = '\nProvide an existing path to be used this time: '
    while not os.path.isdir(answer):
        answer = input(question)
        if os.path.isdir(answer):
            temp_path = answer
            return answer
        else:
            continue


def prep_text_with_default_path() -> str:
    with open(default_path, 'r') as path:
        return b.prepare_text(path.read())


def prep_text_with_temp_path() -> str:
    return b.prepare_text(define_temp_path())


def create_text_with_default_path():
    b.write_file(
        default_path + file_name,
        prep_text_with_default_path()
    )


def create_text_with_temp_path():
    b.write_file(
        temp_path + file_name,
        prep_text_with_default_path()
    )


if __name__ == '__main__':

    print_initial_messages()

    if use_default_path():
        create_text_with_default_path()
        print_result(default_path)
    else:
        create_text_with_temp_path()
        print_result(temp_path)

    print_closing_message()
