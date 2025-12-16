import pytest
from playwright.sync_api import expect

def test_access_account_menu(amazon_page):
    amazon_page.locator('#nav-link-accountList').hover()
    amazon_page.wait_for_timeout(2000)
    
    assert amazon_page.locator('#nav-flyout-accountList, .nav-flyout-content').first.is_visible()
    assert amazon_page.locator('a[data-nav-role="signin"], a:has-text("Sign in")').first.is_visible()