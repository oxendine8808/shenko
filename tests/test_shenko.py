#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `shenko` package."""

import pytest

from click.testing import CliRunner


import sys
sys.path.append('../shenko')
from shenko import shenko
from shenko import cli


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string

# Removed 'CLI-interface' in version 0.1.25-0.1.26
#def test_command_line_interface():
#    """Test the CLI."""
#    runner = CliRunner()
#    result = runner.invoke(cli.main)
#    assert result.exit_code == 0
#    assert 'shenko.cli.main' in result.output
#    help_result = runner.invoke(cli.main, ['--help'])
#    assert help_result.exit_code == 0
#    assert '--help  Show this message and exit.' in help_result.output
