import pytest
from selene import browser, have


def test_github_desktop(browser_management_desktop_and_mobile):
    if browser.config.window_width < 1000 and browser.config.window_height < 800:
        pytest.skip("Передано значение mobile расширения")
    else:
        browser.open('/')

        browser.element('.HeaderMenu-link--sign-in').click()

        browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))


def test_github_mobile(browser_management_desktop_and_mobile):
    if browser.config.window_width > 1000 and browser.config.window_height >= 800:
        pytest.skip("Передано значение desktop расширения")
    else:
        browser.open('/')

        browser.element('.Button-label').click()
        browser.element('.HeaderMenu-link--sign-in').click()

        browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))
