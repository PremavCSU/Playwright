import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=['--disable-web-security', '--disable-features=VizDisplayCompositor'])
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    page = browser.new_page()
    page.set_default_timeout(60000)
    yield page
    page.close()

@pytest.fixture
def amazon_page(page):
    page.goto("https://amazon.com", timeout=60000)
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(3000)
    return page