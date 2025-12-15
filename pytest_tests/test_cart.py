import pytest
from playwright.sync_api import expect

def test_add_item_to_cart(amazon_page):
    """Test adding item to shopping cart"""
    amazon_page.locator("#twotabsearchtextbox").fill("wireless mouse")
    amazon_page.locator("#twotabsearchtextbox").press("Enter")
    amazon_page.wait_for_load_state("networkidle")
    
    amazon_page.locator('[data-component-type="s-search-result"] h2 a').first.click()
    amazon_page.wait_for_load_state("networkidle")
    
    add_to_cart_button = amazon_page.locator('#add-to-cart-button, input[name="submit.add-to-cart"]').first
    if add_to_cart_button.is_visible():
        add_to_cart_button.click()
    
    expect(amazon_page.locator('#sw-atc-details-single-container, #attachDisplayAddBaseAlert, [data-testid="add-to-cart-success"]').first).to_be_visible(timeout=10000)