import sys

from homework4.task3 import my_precious_logger

def test_myoutput(capsys):
    my_precious_logger("error: file not found")
    captured = capsys.readouterr()
    assert captured.out == "error: file not found"


def test_myoutput1(capsys):
    my_precious_logger("OK")
    captured = capsys.readouterr()
    assert captured.out == "OK"