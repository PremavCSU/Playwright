import pytest
from playwright.sync_api import expect

def test_apply_search_filters(amazon_page):
    amazon_page.locator('#twotabsearchtextbox').fill('headphones')
    amazon_page.locator('#twotabsearchtextbox').press('Enter')
    amazon_page.wait_for_load_state('networkidle')
    
    prime_filter = amazon_page.locator('[data-cy="prime-filter"], input[name="s-ref-checkbox-Prime"], span:has-text("Prime")').first
    if prime_filter.is_visible():
        prime_filter.click()
        amazon_page.wait_for_load_state('networkidle')
    
    expect(amazon_page).to_have_url(lambda url: 's?k=headphones' in url)