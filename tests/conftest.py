import pytest

from selene import browser


@pytest.fixture(params=[(1920, 1080), (1366, 800), (1280, 1024)], scope='function')
def browser_management_desktop(request):
    browser.config.base_url = 'https://github.com'
    [width, height] = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    yield browser

    browser.quit()


@pytest.fixture(params=[(375, 667), (414, 736), (360, 700)], scope='function')
def browser_management_mobile(request):
    browser.config.base_url = 'https://github.com'
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    yield browser

    browser.quit()


@pytest.fixture(params=[(1920, 1080), (1366, 800), (1280, 1024),
                        (375, 667), (414, 736), (360, 700)],
                scope='function')
def browser_management_desktop_and_mobile(request):
    browser.config.base_url = 'https://github.com'
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    yield browser

    browser.quit()
