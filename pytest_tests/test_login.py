import pytest
import re
from playwright.sync_api import Page, expect

def test_amazon_login_page_elements(page: Page):
    page.goto("https://amazon.com")
    
    page.click("#nav-link-accountList")
    page.wait_for_load_state("networkidle")
    
    expect(page.locator("#ap_email")).to_be_visible()
    expect(page.locator("#continue")).to_be_visible()
    expect(page).to_have_title(re.compile("Sign"))

def test_login_form_validation(page: Page):
    page.goto("https://amazon.com/ap/signin")
    
    page.click("#continue")
    
    expect(page.locator(".a-alert-error")).to_be_visible()