import pytest
from playwright.sync_api import expect

def test_prime_membership_page(page):
    page.goto('https://amazon.com/prime')
    page.wait_for_load_state('networkidle')
    
    expect(page).to_have_url(lambda url: 'prime' in url)
    expect(page.locator('h1, [data-testid="prime-title"], .prime-header').first).to_be_visible()