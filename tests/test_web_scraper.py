from web_scraper import __version__
from web_scraper.web_scraper import *

def test_version():
    assert __version__ == '0.1.0'



def test_count():

    URL = "https://en.wikipedia.org/wiki/Petra"
    assert get_citations_needed_count(URL) == 5


def test_report():
    URL = "https://en.wikipedia.org/wiki/Petra"
    expected = open("test.txt", "r")

    assert get_citations_needed_report(URL) == expected.read()