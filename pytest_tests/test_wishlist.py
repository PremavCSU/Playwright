import pytest
from playwright.sync_api import expect

def test_add_to_wishlist(amazon_page):
    amazon_page.locator('#twotabsearchtextbox').fill('books')
    amazon_page.locator('#twotabsearchtextbox').press('Enter')
    amazon_page.wait_for_load_state('networkidle')
    
    amazon_page.locator('[data-component-type="s-search-result"] h2 a').first.click()
    amazon_page.wait_for_load_state('networkidle')
    
    wishlist_button = amazon_page.locator('#add-to-wishlist-button-submit, [data-action="add-to-wishlist"]').first
    if wishlist_button.is_visible():
        wishlist_button.click()
    
    expect(amazon_page.locator('#productTitle')).to_be_visible()