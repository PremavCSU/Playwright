import pytest
from playwright.sync_api import expect

def test_view_product_details(amazon_page):
    amazon_page.locator('#twotabsearchtextbox').fill('kindle')
    amazon_page.locator('#twotabsearchtextbox').press('Enter')
    amazon_page.wait_for_timeout(3000)
    
    amazon_page.locator('[data-component-type="s-search-result"] h2 a').first.click()
    amazon_page.wait_for_timeout(3000)
    
    assert amazon_page.locator('#productTitle, [data-testid="product-title"]').first.is_visible()
    assert amazon_page.locator('.a-price, [data-testid="price"]').first.is_visible()