import pytest
from playwright.sync_api import expect

def test_search_for_tv_on_amazon(amazon_page):
    amazon_page.fill('#twotabsearchtextbox', 'TV')
    amazon_page.click('#nav-search-submit-button')
    
    expect(amazon_page).to_have_title(lambda title: 'TV' in title)