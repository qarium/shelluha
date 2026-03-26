import os

import pytest


@pytest.fixture
def get_default_file_path():
    default_file_path = os.getcwd()
    yield default_file_path
    os.chdir(default_file_path)
