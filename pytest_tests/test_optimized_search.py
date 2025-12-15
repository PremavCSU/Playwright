import pytest
from playwright.sync_api import expect

def search(page, term):
    page.locator('#twotabsearchtextbox').fill(term)
    page.locator('#twotabsearchtextbox').press('Enter')
    page.wait_for_load_state('networkidle')

def test_amazon_multi_product_search(amazon_page):
    search(amazon_page, 'phone')
    expect(amazon_page).to_have_url(lambda url: 's?k=phone' in url)
    expect(amazon_page.locator('[data-component-type="s-search-result"]')).to_be_visible()
    
    search(amazon_page, 'laptop')
    expect(amazon_page).to_have_url(lambda url: 's?k=laptop' in url)
    expect(amazon_page.locator('[data-component-type="s-search-result"]')).to_be_visible()
    
    search(amazon_page, 'TV')
    expect(amazon_page).to_have_url(lambda url: 's?k=TV' in url)
    expect(amazon_page.locator('[data-component-type="s-search-result"]')).to_be_visible()