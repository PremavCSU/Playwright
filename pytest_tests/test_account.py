import pytest
from playwright.sync_api import expect

def test_access_account_menu(amazon_page):
    amazon_page.locator('#nav-link-accountList').hover()
    amazon_page.wait_for_timeout(2000)
    
    expect(amazon_page.locator('#nav-flyout-accountList, .nav-flyout-content').first).to_be_visible()
    expect(amazon_page.locator('a[data-nav-role="signin"], a:has-text("Sign in")').first).to_be_visible()