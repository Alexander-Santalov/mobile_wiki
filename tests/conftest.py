import pytest
from selene.support.shared import browser

from wiki_app.fixture.application import Application
from wiki_app.utils import attach


@pytest.fixture()
def app(request):
    env = request.config.getoption("--env")
    fixture = Application(env)
    yield browser
    attach.add_video(browser)
    attach.add_screenshot(browser)
    fixture.destroy()


def pytest_addoption(parser):
    parser.addoption("--env", action='store', default="android")