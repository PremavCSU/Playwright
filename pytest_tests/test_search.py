import pytest
from playwright.sync_api import expect

def test_amazon_phone_search(amazon_page):
    """Test Amazon phone search functionality"""
    amazon_page.locator("#twotabsearchtextbox").fill("phone")
    amazon_page.locator("#twotabsearchtextbox").press("Enter")
    amazon_page.wait_for_load_state("networkidle")
    
    expect(amazon_page).to_have_url(r".*s\?k=phone.*")
    expect(amazon_page.locator('[data-component-type="s-search-result"]')).to_be_visible()

def test_optimized_multi_search(amazon_page):
    """Test multiple product searches"""
    search_terms = ["phone", "laptop", "TV"]
    
    for term in search_terms:
        amazon_page.locator("#twotabsearchtextbox").fill(term)
        amazon_page.locator("#twotabsearchtextbox").press("Enter")
        amazon_page.wait_for_load_state("networkidle")
        
        expect(amazon_page).to_have_url(f".*s\\?k={term}.*")
        expect(amazon_page.locator('[data-component-type="s-search-result"]')).to_be_visible()