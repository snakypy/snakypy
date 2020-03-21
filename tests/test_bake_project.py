"""Tests for `snakypy` package."""
import pytest
import snakypy
import os
from os.path import join
from contextlib import suppress
from unittest.mock import patch
from unittest import TestCase
from . import __tmpdir__


def create_base_tests():
    """Function to create the temporary test base
    """
    with suppress(FileExistsError):
        os.makedirs(__tmpdir__)


# Creating the temporary test base.
create_base_tests()
# List containing files that will be created in the tests.
lst_files = ['file.txt', 'file.json']


def test_create_file():
    file = 'Test'
    forced = snakypy.file.create(file, join(__tmpdir__, lst_files[0]), force=True)
    assert forced is True
    with pytest.raises(FileExistsError):
        assert snakypy.file.create(file, join(__tmpdir__, lst_files[0]), force=False)
    snakypy.stiff.cleaner(__tmpdir__, lst_files[0])


def test_error_extension_create_json():
    content = {"Hello": "World!"}
    with pytest.raises(Exception):
        assert snakypy.json.create(content, join(__tmpdir__, lst_files[0]))


def test_create_json():
    content = {"Hello": "World!"}
    forced = snakypy.json.create(content, join(__tmpdir__, lst_files[1]), force=True)
    assert forced is True
    with pytest.raises(Exception):
        snakypy.json.create(content, join(__tmpdir__, lst_files[1]))


def test_read_json():
    data = snakypy.json.read(join(__tmpdir__, lst_files[1]))
    assert data['Hello'] == 'World!'


def test_update_json():
    data = snakypy.json.read(join(__tmpdir__, lst_files[1]))
    data['Hello'] = 'Terra!'
    assert snakypy.json.update(join(__tmpdir__, lst_files[1]), data) is True


def test_create_json_exists():
    content = {"Hello": "World!"}
    with pytest.raises(FileExistsError):
        assert snakypy.json.create(content, join(__tmpdir__, lst_files[1]))


def test_read_json_error():
    snakypy.stiff.cleaner(__tmpdir__, lst_files[1])
    with pytest.raises(FileNotFoundError):
        assert snakypy.json.read(join(__tmpdir__, lst_files[1]))


# def test_update_json_not_found():
#     data = snakypy.json.read(join(__tmpdir__, lst_files[1]))
#     data['Hello'] = 'Marte!'
#     snakypy.utils.cleaner(__tmpdir__, lst_files[1])
#     with pytest.raises(FileNotFoundError, Exception):
#         assert snakypy.json.update(join(__tmpdir__, lst_files[1]), data)


def test_get_shell():
    from sys import platform

    if not platform.startswith('win'):
        shells = ['bash', 'zsh', 'sh', 'ksh']
        shell = snakypy.catch.shell()
        assert shell in shells


def test_percentage():
    from snakypy.calc import percentage

    perc = 5  # 5%
    whole = 120
    result_v = percentage(perc, whole)
    result_sum = percentage(5, 120, operation='+')
    result_sub = percentage(5, 120, operation='-')
    result_log_sum = percentage(5, 120, operation='+', log=True)
    result_log_sub = percentage(5, 120, operation='-', log=True)
    assert result_v == 6.0
    assert result_sum == 126.0
    assert result_sub == 114.00
    assert result_log_sum == f'>> {whole} + {perc}% = 126.00'
    assert result_log_sub == f'>> {whole} - {perc}% = 114.00'


def test_file_extension():
    file = '/home/file.tar.gz'
    assert snakypy.catch.extension(file) == '.gz'
    assert snakypy.catch.extension(file, first_dot=True) == 'tar.gz'


def test_command_real_time():
    assert snakypy.console.cmd('echo', ret=True, verbose=True) == 0


def test_imc():
    result = snakypy.calc.bmi('m', 70, 1.73)
    assert result == 'Normal weight.'
    result = snakypy.calc.bmi('m', 59.2, 1.80)
    assert result == 'Under weight.'
    result = snakypy.calc.bmi('m', 82.4, 1.69)
    assert result == 'Overweight.'
    result = snakypy.calc.bmi('m', 90.1, 1.62)
    assert result == 'Obesity.'
    result = snakypy.calc.bmi('f', 69.5, 1.68)
    assert result == 'Normal weight.'
    result = snakypy.calc.bmi('f', 45.1, 1.71)
    assert result == 'Under weight.'
    result = snakypy.calc.bmi('f', 83.7, 1.67)
    assert result == 'Overweight.'
    result = snakypy.calc.bmi('f', 83.7, 1.58)
    assert result == 'Obesity.'
    result = snakypy.calc.bmi('', 70, 1.70)
    assert result is False
    result = snakypy.calc.bmi('', '', 1.60)
    assert result is False
    result = snakypy.calc.bmi('', '', '')
    assert result is False


def test_rmdir_blank():
    paths = (os.path.join(__tmpdir__, "foo"), os.path.join(__tmpdir__, "bar"))
    snakypy.path.create(multidir=paths)
    assert os.path.isdir(paths[0]) is True
    snakypy.utils.os.rmdir_blank(__tmpdir__)
    assert os.path.isdir(paths[0]) is False

class TestBakeProject(TestCase):

    @patch('snakypy.console.pick', return_value='python')
    def test_pick_no_index(self, input):
        title = 'What is your favorite programming language?'
        options = ['C', 'C++', 'Java', 'Javascript', 'Python', 'Ruby']
        self.assertEqual(snakypy.console.pick(title, options), 'python')

    @patch('snakypy.console.pick', return_value=(5, 'python'))
    def test_pick_with_index(self, input):
        title = 'What is your favorite programming language?'
        options = ['C', 'C++', 'Java', 'Javascript', 'Python', 'Ruby']
        self.assertEqual(snakypy.console.pick(title, options, index=True), (5, 'python'))
