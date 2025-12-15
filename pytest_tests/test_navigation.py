import pytest
from playwright.sync_api import expect

def test_navigate_categories(amazon_page):
    """Test category navigation"""
    amazon_page.locator("#nav-hamburger-menu").click()
    amazon_page.wait_for_timeout(2000)
    
    electronics_link = amazon_page.locator('a[href*="electronics"], a:has-text("Electronics")').first
    if electronics_link.is_visible():
        electronics_link.click()
        amazon_page.wait_for_load_state("networkidle")
        expect(amazon_page).to_have_url(r".*electronics.*")
    else:
        amazon_page.goto("https://amazon.com/electronics")
    
    expect(amazon_page.locator('h1, [data-testid="page-title"]').first).to_be_visible()

def test_account_menu_access(amazon_page):
    """Test account menu accessibility"""
    amazon_page.locator("#nav-link-accountList").hover()
    amazon_page.wait_for_timeout(2000)
    
    expect(amazon_page.locator('#nav-flyout-accountList, .nav-flyout-content').first).to_be_visible()
    expect(amazon_page.locator('a[data-nav-role="signin"], a:has-text("Sign in")').first).to_be_visible()