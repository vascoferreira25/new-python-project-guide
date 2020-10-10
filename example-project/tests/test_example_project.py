from example_project import __version__
from example_project import utils


def test_version():
    assert __version__ == '0.1.0'

def test_greet():
    assert utils.greet("Hello", "World") == "Hello, World!"