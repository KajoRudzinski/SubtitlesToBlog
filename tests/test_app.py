from src import app

import os

has_srt = "has_srt\\"
has_no_srt = "has_no_srt\\"


def test_read_path_no_srt():
    p = os.path.join(os.getcwd(), has_no_srt)
    rp = app.read_path(p)
    assert rp == 'No SRT File'


def test_read_path_has_srt():
    p = os.path.join(os.getcwd(), has_srt)
    rp = app.read_path(p)
    assert rp == os.path.join(os.getcwd(), has_srt, 'test.srt')
