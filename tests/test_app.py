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


