import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language= ru or en")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    option = Options()
    option.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=option)
    yield browser
    browser.quit()