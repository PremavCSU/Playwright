import pytest
from playwright.sync_api import expect

def test_view_product_details(amazon_page):
    amazon_page.locator('#twotabsearchtextbox').fill('kindle')
    amazon_page.locator('#twotabsearchtextbox').press('Enter')
    amazon_page.wait_for_load_state('networkidle')
    
    amazon_page.locator('[data-component-type="s-search-result"] h2 a').first.click()
    amazon_page.wait_for_load_state('networkidle')
    
    expect(amazon_page.locator('#productTitle, [data-testid="product-title"]').first).to_be_visible()
    expect(amazon_page.locator('.a-price, [data-testid="price"]').first).to_be_visible()