import pytest

# project imports
from npl.formatter import raw_text_formatter


def test_tabs_whitespaces():
    t = '  command  uplink\t active! '
    ft = raw_text_formatter(t)
    assert ft == 'command uplink active!'


def test_newline_tabs_newline():
    t = ' marv\n\t\n assembly \n\tcomplete'
    ft = raw_text_formatter(t)
    assert ft == 'marv assembly complete'


def test_single_non_semantic_newlines():
    t = 'without \n music, life\n\twould be a mistake.'
    ft = raw_text_formatter(t)
    assert ft == 'without music, life would be a mistake.'


def test_obsolete_newlines():
    t = ''

