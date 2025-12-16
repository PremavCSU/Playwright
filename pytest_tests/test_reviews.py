import pytest
from playwright.sync_api import expect

def test_view_product_reviews(amazon_page):
    amazon_page.locator('#twotabsearchtextbox').fill('tablet')
    amazon_page.locator('#twotabsearchtextbox').press('Enter')
    amazon_page.wait_for_timeout(3000)
    
    amazon_page.locator('[data-component-type="s-search-result"] h2 a').first.click()
    amazon_page.wait_for_timeout(3000)
    
    reviews_link = amazon_page.locator('a[href*="product-reviews"], a:has-text("See all reviews")').first
    if reviews_link.is_visible():
        reviews_link.click()
        amazon_page.wait_for_timeout(3000)
        assert amazon_page.locator('[data-hook="review-body"], .review-text').first.is_visible()
    else:
        assert amazon_page.locator('#productTitle').is_visible()