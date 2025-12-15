import pytest
from playwright.sync_api import expect

@pytest.mark.timeout(60)
def test_amazon_electronics_items_search(amazon_page):
    amazon_page.get_by_role('searchbox', name='Search Amazon').click()
    amazon_page.get_by_role('searchbox', name='Search Amazon').fill('phone')
    amazon_page.get_by_role('searchbox', name='Search Amazon').press('Enter')
    amazon_page.get_by_role('button', name='Go', exact=True).click()
    amazon_page.get_by_role('link', name='Samsung Galaxy A16 5G A').click()
    amazon_page.locator('.page-load-link').first.click()
    amazon_page.get_by_role('searchbox', name='Search Amazon').fill('TV')
    amazon_page.get_by_role('button', name='Go', exact=True).click()
    amazon_page.get_by_role('link', name='Apply 44 to 49 Inches filter').click()
    
    amazon_page.goto('https://www.amazon.com/Hisense-Class-Mini-LED-55U65QF-Built/dp/B0DYWG3BL1/ref=sr_1_1_sspa?crid=2IA954F6LHAML&dib=eyJ2IjoiMSJ9.HuWlg1IUFXJsotCPfav-91BbyPrlD9_ALzLM4pWkHIZ3R0qeqf3YL481mqo7Xxmlj_2_Qy5IRAwE_PbZVPO0xlLOGWMpaE4MpW-NRSigwcs3c_30VycaJgZy4iw1ZEsNIUl2NHCb1P2LMkmfPyavR7WdcgTarVzrZuTtAUSpcWl-WEE4GzFlHDHyR4D2MPyjir40oOZMoLLm_IJv0tVW5WU06tGVkBLd7Lf5rVytMvs.5d_29UCOPOUElQxJqqS1Xcw91okgTrZH2LAp-RcJNp8&dib_tag=se&keywords=TV&qid=1763772952&refinements=p_n_g-1004151129091%3A1232882011&rnid=1232878011&sprefix=tv%2Caps%2C307&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1')
    amazon_page.get_by_role('radio', name='65 inch $547.99 with 35').click()
    amazon_page.get_by_role('radio', name='75 inch $747.99 with 26').click()
    
    amazon_page.goto('https://www.amazon.com/Hisense-Class-Mini-LED-55U65QF-Built/dp/B0DYWNQMQJ/ref=sr_1_1_sspa?crid=2IA954F6LHAML&dib=eyJ2IjoiMSJ9.HuWlg1IUFXJsotCPfav-91BbyPrlD9_ALzLM4pWkHIZ3R0qeqf3YL481mqo7Xxmlj_2_Qy5IRAwE_PbZVPO0xlLOGWMpaE4MpW-NRSigwcs3c_30VycaJgZy4iw1ZEsNIUl2NHCb1P2LMkmfPyavR7WdcgTarVzrZuTtAUSpcWl-WEE4GzFlHDHyR4D2MPyjir40oOZMoLLm_IJv0tVW5WU06tGVkBLd7Lf5rVytMvs.5d_29UCOPOUElQxJqqS1Xcw91okgTrZH2LAp-RcJNp8&dib_tag=se&keywords=TV&qid=1763772952&refinements=p_n_g-1004151129091%3A1232882011&rnid=1232878011&sprefix=tv%2Caps%2C307&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1')
    amazon_page.get_by_role('searchbox', name='Search Amazon').click()
    amazon_page.get_by_role('searchbox', name='Search Amazon').fill('Laptop')
    amazon_page.get_by_role('button', name='Go', exact=True).click()
    
    amazon_page.goto('https://www.amazon.com/FHD-Laptop-i5-1135G7-Computer-Warranty-Fingerprint/dp/B0FXM28CK7/ref=sr_1_1_sspa?crid=23CQ271JMQ1QV&dib=eyJ2IjoiMSJ9.HQntUDl3-aPkMjwfefcVP75APu7bMuaeVD96FMI_DAD75s6Ab3kjeyhgIf14aafDCGpJgCDL9FSR06h6NSHcIacBHr4C2d6mw21sip6AZdDl5Iy0cChdtvYEJ_C7W9UX7wBnTC14Yje7prI8NAJxM70fvULF_7n_Ghnk2IfFGO6U6CLaNsPsMch-5ViMriZN0ZPZEUTwxZ-KInEKUk9symfjrvGkjrvnbXB2JTD1qjk.LUW4A-ok3_fEHzl_wq0zKgOPjYHhGxMDLEDjU1fw8nk&dib_tag=se&keywords=Laptop&qid=1763772984&sprefix=laptop%2Caps%2C802&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1')
    amazon_page.get_by_role('radio', name='Gray $499.99 with 50 percent').click()