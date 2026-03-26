import os
import pathlib

import hamcrest as h
from shelluha.shell import cd


def test_in_contex_manager_positive(get_default_file_path):
    with cd(".."):
        h.assert_that(os.getcwd(), h.equal_to(str(pathlib.Path(get_default_file_path).parent)))


def test_path_does_not_exists(get_default_file_path):
    cd("&^%$@&DG@&D")
    h.assert_that(os.getcwd(), h.equal_to(get_default_file_path))


def test_outside_context_manager(get_default_file_path):
    cd("..")
    h.assert_that(os.getcwd(), h.equal_to(get_default_file_path))
