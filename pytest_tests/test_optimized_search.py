import pytest
from playwright.sync_api import expect

def search(page, term):
    page.locator('#twotabsearchtextbox').fill(term)
    page.locator('#twotabsearchtextbox').press('Enter')
    page.wait_for_timeout(3000)

def test_amazon_multi_product_search(amazon_page):
    search(amazon_page, 'phone')
    assert 's?k=phone' in amazon_page.url
    assert amazon_page.locator('[data-component-type="s-search-result"]').is_visible()
    
    search(amazon_page, 'laptop')
    assert 's?k=laptop' in amazon_page.url
    assert amazon_page.locator('[data-component-type="s-search-result"]').is_visible()
    
    search(amazon_page, 'TV')
    assert 's?k=TV' in amazon_page.url
    assert amazon_page.locator('[data-component-type="s-search-result"]').is_visible()