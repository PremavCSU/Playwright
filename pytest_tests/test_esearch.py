import pytest
from playwright.sync_api import expect

def test_amazon_electronics_items_search(amazon_page):
    # Search for phone
    amazon_page.locator('#twotabsearchtextbox').fill('phone')
    amazon_page.locator('#twotabsearchtextbox').press('Enter')
    amazon_page.wait_for_timeout(3000)
    
    assert 's?k=phone' in amazon_page.url
    
    # Search for TV
    amazon_page.locator('#twotabsearchtextbox').fill('TV')
    amazon_page.locator('#twotabsearchtextbox').press('Enter')
    amazon_page.wait_for_timeout(3000)
    
    assert 's?k=TV' in amazon_page.url
    
    # Search for Laptop
    amazon_page.locator('#twotabsearchtextbox').fill('Laptop')
    amazon_page.locator('#twotabsearchtextbox').press('Enter')
    amazon_page.wait_for_timeout(3000)
    
    assert 's?k=Laptop' in amazon_page.url