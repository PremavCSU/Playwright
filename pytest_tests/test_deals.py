import pytest
from playwright.sync_api import expect

def test_browse_deals_page(page):
    page.goto('https://amazon.com/deals')
    page.wait_for_load_state('networkidle')
    
    expect(page).to_have_url(lambda url: 'deals' in url)
    expect(page.locator('[data-testid="deal-card"], .DealCard, .a-section').first).to_be_visible()