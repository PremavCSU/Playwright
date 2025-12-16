import pytest
from playwright.sync_api import expect

def test_prime_membership_page(page):
    page.goto('https://amazon.com/prime')
    page.wait_for_timeout(3000)
    
    assert 'prime' in page.url
    assert page.locator('h1, [data-testid="prime-title"], .prime-header').first.is_visible()