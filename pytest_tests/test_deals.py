import pytest
from playwright.sync_api import expect

def test_browse_deals_page(page):
    page.goto('https://amazon.com/deals')
    page.wait_for_timeout(3000)
    
    assert 'deals' in page.url
    assert page.locator('[data-testid="deal-card"], .DealCard, .a-section').first.is_visible()