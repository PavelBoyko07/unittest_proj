import pytest
def get_val(collection, key, default='git'):
    pass

def test_existing_key():
    data = {"vcs": "mercurial", "language": "python"}
    assert get_val(data, "vcs") == "mercurial"

def test_non_existing_key_with_default():
    data = {"language": "python"}
    assert get_val(data, "vcs", "git") == "git"

def test_empty_dict_custom_default():
    data = {}
    assert get_val(data, "vcs", "bazaar") == "bazaar"

def test_non_existing_key_default_param():
    data = {}
    assert get_val(data, "vcs") == "git"