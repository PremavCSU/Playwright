import pytest
from playwright.sync_api import expect

def test_sort_search_results(amazon_page):
    amazon_page.locator('#twotabsearchtextbox').fill('shoes')
    amazon_page.locator('#twotabsearchtextbox').press('Enter')
    amazon_page.wait_for_load_state('networkidle')
    
    sort_dropdown = amazon_page.locator('select[name="s"], .s-sort-menu select').first
    if sort_dropdown.is_visible():
        sort_dropdown.select_option('price-asc-rank')
        amazon_page.wait_for_load_state('networkidle')
        expect(amazon_page).to_have_url(lambda url: 'price-asc-rank' in url)
    else:
        expect(amazon_page).to_have_url(lambda url: 's?k=shoes' in url)