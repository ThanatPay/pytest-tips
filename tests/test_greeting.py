import pytest
from greeting import my_name

@pytest.fixture
def boom():
    return "My name is : Boom"

@pytest.fixture
def boo():
    return "My name is : Boo"

def test_my_name(boom):
    assert boom == my_name("Boom")

def test_my_name2(boo):
    assert boo == my_name("Boo")