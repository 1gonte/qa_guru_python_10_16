import pytest
from selene import browser, have


@pytest.mark.parametrize('browser_management_desktop_and_mobile',
                         [(1920, 1080), (1366, 800), (1280, 1024)],
                         indirect=True)
def test_github_desktop(browser_management_desktop_and_mobile):
    browser.open('/')

    browser.element('.HeaderMenu-link--sign-in').click()

    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))


@pytest.mark.parametrize('browser_management_desktop_and_mobile',
                         [(375, 667), (414, 736), (360, 700)],
                         indirect=True)
def test_github_mobile(browser_management_desktop_and_mobile):
    browser.open('/')

    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()

    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))
