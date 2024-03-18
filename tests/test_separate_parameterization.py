from selene import browser, have


def test_github_desktop(browser_management_desktop):
    browser.open('/')

    browser.element('.HeaderMenu-link--sign-in').click()

    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))


def test_github_mobile(browser_management_mobile):
    browser.open('/')

    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()

    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))
