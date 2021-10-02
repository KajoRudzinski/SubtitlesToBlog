from src import app
import os

has_srt = "has_srt\\"
has_no_srt = "has_no_srt\\"


def test_read_path_no_srt():
    assert app.read_path(
        os.path.join(os.getcwd(), has_no_srt)
    ) is None


def test_read_path_has_srt():
    assert app.read_path(
        os.path.join(os.getcwd(), has_srt)
    ) == os.path.join(os.getcwd(), has_srt, 'test.srt')


def test_read_file():
    assert app.read_file('line_test_file.txt') == ['l1', 'l2', '3']


def test_increment():
    assert app.increment_by_1(1) == 2


def test_is_not_empty():
    assert app.is_not_empty('') is False
    assert app.is_not_empty('i') is True


def test_is_not_timestamp():
    assert app.is_not_timestamp('00:00:04,212 --> 00:00:09,432') is False
    assert app.is_not_timestamp('a') is True


def test_concat_lines():
    test_list = [
        '0'
        , '00:00:00,000 --> 00:00:04,132'
        , '1'
        , '2'
        , '3'
        , ''
        , '1'
        , ',00:00:04,212 --> 00:00:09,432'
        , 'a'
        , ''
        , '2'
        , '00:00:04,212 --> 00:00:09,432'
        , 'a'
    ]
    assert app.concat_lines(test_list) == '1 2 3 a a '
