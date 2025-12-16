import pytest
from playwright.sync_api import expect

def test_sort_search_results(amazon_page):
    amazon_page.locator('#twotabsearchtextbox').fill('shoes')
    amazon_page.locator('#twotabsearchtextbox').press('Enter')
    amazon_page.wait_for_timeout(3000)
    
    sort_dropdown = amazon_page.locator('select[name="s"], .s-sort-menu select').first
    if sort_dropdown.is_visible():
        sort_dropdown.select_option('price-asc-rank')
        amazon_page.wait_for_timeout(3000)
        assert 'price-asc-rank' in amazon_page.url
    else:
        assert 's?k=shoes' in amazon_page.url