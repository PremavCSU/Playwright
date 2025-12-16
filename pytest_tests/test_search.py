import pytest
from playwright.sync_api import expect

def test_amazon_phone_search(amazon_page):
    amazon_page.locator('#twotabsearchtextbox').fill('phone')
    amazon_page.locator('#twotabsearchtextbox').press('Enter')
    amazon_page.wait_for_timeout(3000)
    
    assert 's?k=phone' in amazon_page.url
    assert amazon_page.locator('[data-component-type="s-search-result"]').is_visible()

def test_optimized_multi_search(amazon_page):
    search_terms = ['phone', 'laptop', 'TV']
    
    for term in search_terms:
        amazon_page.locator('#twotabsearchtextbox').fill(term)
        amazon_page.locator('#twotabsearchtextbox').press('Enter')
        amazon_page.wait_for_timeout(3000)
        
        assert f's?k={term}' in amazon_page.url
        assert amazon_page.locator('[data-component-type="s-search-result"]').is_visible()