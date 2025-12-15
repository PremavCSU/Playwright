import pytest
from playwright.sync_api import expect

def test_diabetic_friendly_food_search(amazon_page):
    """Test search for diabetic-friendly food products"""
    search_terms = [
        "rice porridge", 
        "whole grain", 
        "low GI food", 
        "diabetic friendly", 
        "sugar control"
    ]
    
    for term in search_terms:
        amazon_page.locator("#twotabsearchtextbox").fill(term)
        amazon_page.locator("#twotabsearchtextbox").press("Enter")
        amazon_page.wait_for_load_state("networkidle")
        
        expect(amazon_page).to_have_url(f".*s\\?k={term.replace(' ', '+')}.*")
        expect(amazon_page.locator('[data-component-type="s-search-result"]')).to_be_visible()

def test_health_monitoring_devices(amazon_page):
    """Test search for glucose monitoring devices"""
    amazon_page.locator("#twotabsearchtextbox").fill("glucometer")
    amazon_page.locator("#twotabsearchtextbox").press("Enter")
    amazon_page.wait_for_load_state("networkidle")
    
    expect(amazon_page).to_have_url(r".*s\?k=glucometer.*")
    expect(amazon_page.locator('[data-component-type="s-search-result"]')).to_be_visible()

def test_fiber_rich_products(amazon_page):
    """Test search for fiber-rich food products"""
    amazon_page.locator("#twotabsearchtextbox").fill("fiber rich food")
    amazon_page.locator("#twotabsearchtextbox").press("Enter")
    amazon_page.wait_for_load_state("networkidle")
    
    expect(amazon_page).to_have_url(r".*s\?k=fiber\+rich\+food.*")
    expect(amazon_page.locator('[data-component-type="s-search-result"]')).to_be_visible()