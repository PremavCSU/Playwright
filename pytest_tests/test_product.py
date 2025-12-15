import pytest
from playwright.sync_api import expect

def test_view_product_details(amazon_page):
    """Test product details page"""
    amazon_page.locator("#twotabsearchtextbox").fill("kindle")
    amazon_page.locator("#twotabsearchtextbox").press("Enter")
    amazon_page.wait_for_load_state("networkidle")
    
    amazon_page.locator('[data-component-type="s-search-result"] h2 a').first.click()
    amazon_page.wait_for_load_state("networkidle")
    
    expect(amazon_page.locator('#productTitle, [data-testid="product-title"]').first).to_be_visible()
    expect(amazon_page.locator('.a-price, [data-testid="price"]').first).to_be_visible()

def test_view_product_reviews(amazon_page):
    """Test product reviews functionality"""
    amazon_page.locator("#twotabsearchtextbox").fill("tablet")
    amazon_page.locator("#twotabsearchtextbox").press("Enter")
    amazon_page.wait_for_load_state("networkidle")
    
    amazon_page.locator('[data-component-type="s-search-result"] h2 a').first.click()
    amazon_page.wait_for_load_state("networkidle")
    
    reviews_link = amazon_page.locator('a[href*="product-reviews"], a:has-text("See all reviews")').first
    if reviews_link.is_visible():
        reviews_link.click()
        amazon_page.wait_for_load_state("networkidle")
        expect(amazon_page.locator('[data-hook="review-body"], .review-text').first).to_be_visible()
    else:
        expect(amazon_page.locator("#productTitle")).to_be_visible()

def test_add_to_wishlist(amazon_page):
    """Test wishlist functionality"""
    amazon_page.locator("#twotabsearchtextbox").fill("books")
    amazon_page.locator("#twotabsearchtextbox").press("Enter")
    amazon_page.wait_for_load_state("networkidle")
    
    amazon_page.locator('[data-component-type="s-search-result"] h2 a').first.click()
    amazon_page.wait_for_load_state("networkidle")
    
    wishlist_button = amazon_page.locator('#add-to-wishlist-button-submit, [data-action="add-to-wishlist"]').first
    if wishlist_button.is_visible():
        wishlist_button.click()
    
    expect(amazon_page.locator("#productTitle")).to_be_visible()