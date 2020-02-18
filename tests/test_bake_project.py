"""Tests for `snakypy` package."""
import pytest
import snakypy
from snakypy.utilities import cleaner, command_real_time
from os import makedirs
from os.path import join
from contextlib import suppress
from snakypy.utilities.bmi import bmi
from unittest.mock import patch
from unittest import TestCase
from . import __tmpdir__


def create_base_tests():
    """Function to create the temporary test base
    """
    with suppress(FileExistsError):
        makedirs(__tmpdir__)


# Creating the temporary test base.
create_base_tests()
# List containing files that will be created in the tests.
lst_files = ['file.txt', 'file.json']


def test_create_file():
    file = 'Hello!'
    forced = snakypy.create.file(file, join(__tmpdir__, lst_files[0]), force=True)
    assert forced is True
    with pytest.raises(FileExistsError):
        assert snakypy.create.file(file, join(__tmpdir__, lst_files[0]), force=False)


def test_error_extension_create_json():
    content = {"Hello": "World!"}
    with pytest.raises(Exception):
        assert snakypy.create.json2(content, join(__tmpdir__, lst_files[0]))


def test_create_json_exists():
    content = {"Hello": "World!"}
    with pytest.raises(FileExistsError):
        assert snakypy.create.json2(content, join(__tmpdir__, lst_files[1]))


def test_read_json_error():
    cleaner(__tmpdir__, lst_files[1])
    with pytest.raises(FileNotFoundError):
        assert snakypy.read.json2(join(__tmpdir__, lst_files[1]))


def test_create_json():
    content = {"Hello": "World!"}
    forced = snakypy.create.json2(content, join(__tmpdir__, lst_files[1]), force=True)
    assert forced is True
    with pytest.raises(Exception):
        snakypy.create.json2(content, join(__tmpdir__, lst_files[1]))


def test_read_json():
    data = snakypy.read.json2(join(__tmpdir__, lst_files[1]))
    assert data['Hello'] == 'World!'


def test_update_json():
    data = snakypy.read.json2(join(__tmpdir__, lst_files[1]))
    data['Hello'] = 'Terra!'
    assert snakypy.update.json2(join(__tmpdir__, lst_files[1]), data) is True


# def test_update_json_not_found():
#     data = snakypy.read.json2(join(__tmpdir__, lst_files[1]))
#     data['Hello'] = 'Marte!'
#     cleaner(__tmpdir__, lst_files[1])
#     with pytest.raises(FileNotFoundError, Exception):
#         assert snakypy.update.json2(join(__tmpdir__, lst_files[1]), data)


def test_get_shell():
    from snakypy.utilities import get_shell

    shells = ['bash', 'zsh', 'sh', 'ksh']
    shell = get_shell()
    assert shell in shells


def test_percentage():
    from snakypy.utilities import percentage

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


def test_command_real_time():
    assert command_real_time('echo') == 0


def test_imc():
    result = bmi('m', 70, 1.73)
    assert result == 'Normal weight.'
    result = bmi('m', 59.2, 1.80)
    assert result == 'Under weight.'
    result = bmi('m', 82.4, 1.69)
    assert result == 'Overweight.'
    result = bmi('m', 90.1, 1.62)
    assert result == 'Obesity.'
    result = bmi('f', 69.5, 1.68)
    assert result == 'Normal weight.'
    result = bmi('f', 45.1, 1.71)
    assert result == 'Under weight.'
    result = bmi('f', 83.7, 1.67)
    assert result == 'Overweight.'
    result = bmi('f', 83.7, 1.58)
    assert result == 'Obesity.'
    result = bmi('', 70, 1.70)
    assert result is False
    result = bmi('', '', 1.60)
    assert result is False
    result = bmi('', '', '')
    assert result is False


class TestBakeProject(TestCase):

    @patch('snakypy.console.pick', return_value='python')
    def test_pick_no_index(self, input):
        from snakypy.console import pick

        title = 'What is your favorite programming language?'
        options = ['C', 'C++', 'Java', 'Javascript', 'Python', 'Ruby']
        self.assertEqual(pick(title, options), 'python')

    @patch('snakypy.console.pick', return_value=(5, 'python'))
    def test_pick_with_index(self, input):
        from snakypy.console import pick

        title = 'What is your favorite programming language?'
        options = ['C', 'C++', 'Java', 'Javascript', 'Python', 'Ruby']
        self.assertEqual(pick(title, options, index=True), (5, 'python'))
