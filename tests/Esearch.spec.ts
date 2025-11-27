import { test, expect } from '@playwright/test';

test('Amazon Electronics items search', async ({ page }) => {
    test.setTimeout(60000);

  await page.goto('https://amazon.com');
  await page.getByRole('searchbox', { name: 'Search Amazon' }).click();
  await page.getByRole('searchbox', { name: 'Search Amazon' }).fill('phone');
  await page.getByRole('searchbox', { name: 'Search Amazon' }).press('Enter');
  await page.getByRole('button', { name: 'Go', exact: true }).click();
  await page.getByRole('link', { name: 'Samsung Galaxy A16 5G A' }).click();
  await page.locator('.page-load-link').first().click();
  await page.getByRole('searchbox', { name: 'Search Amazon' }).fill('TV');
  await page.getByRole('button', { name: 'Go', exact: true }).click();
  await page.getByRole('link', { name: 'Apply 44 to 49 Inches filter' }).click();
  //await page.getByRole('link', { name: 'Sponsored Ad - Hisense 55"' }).click();
  await page.goto('https://www.amazon.com/Hisense-Class-Mini-LED-55U65QF-Built/dp/B0DYWG3BL1/ref=sr_1_1_sspa?crid=2IA954F6LHAML&dib=eyJ2IjoiMSJ9.HuWlg1IUFXJsotCPfav-91BbyPrlD9_ALzLM4pWkHIZ3R0qeqf3YL481mqo7Xxmlj_2_Qy5IRAwE_PbZVPO0xlLOGWMpaE4MpW-NRSigwcs3c_30VycaJgZy4iw1ZEsNIUl2NHCb1P2LMkmfPyavR7WdcgTarVzrZuTtAUSpcWl-WEE4GzFlHDHyR4D2MPyjir40oOZMoLLm_IJv0tVW5WU06tGVkBLd7Lf5rVytMvs.5d_29UCOPOUElQxJqqS1Xcw91okgTrZH2LAp-RcJNp8&dib_tag=se&keywords=TV&qid=1763772952&refinements=p_n_g-1004151129091%3A1232882011&rnid=1232878011&sprefix=tv%2Caps%2C307&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1');
  await page.getByRole('radio', { name: '65 inch $547.99 with 35' }).click();
  await page.getByRole('radio', { name: '75 inch $747.99 with 26' }).click();
  await page.goto('https://www.amazon.com/Hisense-Class-Mini-LED-55U65QF-Built/dp/B0DYWNQMQJ/ref=sr_1_1_sspa?crid=2IA954F6LHAML&dib=eyJ2IjoiMSJ9.HuWlg1IUFXJsotCPfav-91BbyPrlD9_ALzLM4pWkHIZ3R0qeqf3YL481mqo7Xxmlj_2_Qy5IRAwE_PbZVPO0xlLOGWMpaE4MpW-NRSigwcs3c_30VycaJgZy4iw1ZEsNIUl2NHCb1P2LMkmfPyavR7WdcgTarVzrZuTtAUSpcWl-WEE4GzFlHDHyR4D2MPyjir40oOZMoLLm_IJv0tVW5WU06tGVkBLd7Lf5rVytMvs.5d_29UCOPOUElQxJqqS1Xcw91okgTrZH2LAp-RcJNp8&dib_tag=se&keywords=TV&qid=1763772952&refinements=p_n_g-1004151129091%3A1232882011&rnid=1232878011&sprefix=tv%2Caps%2C307&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1');
  await page.getByRole('searchbox', { name: 'Search Amazon' }).click();
  await page.getByRole('searchbox', { name: 'Search Amazon' }).fill('Laptop');
  await page.getByRole('button', { name: 'Go', exact: true }).click();
  //await page.getByRole('link', { name: 'Sponsored Ad - 15.6\'\' IPS FHD' }).click();
  await page.goto('https://www.amazon.com/FHD-Laptop-i5-1135G7-Computer-Warranty-Fingerprint/dp/B0FXM28CK7/ref=sr_1_1_sspa?crid=23CQ271JMQ1QV&dib=eyJ2IjoiMSJ9.HQntUDl3-aPkMjwfefcVP75APu7bMuaeVD96FMI_DAD75s6Ab3kjeyhgIf14aafDCGpJgCDL9FSR06h6NSHcIacBHr4C2d6mw21sip6AZdDl5Iy0cChdtvYEJ_C7W9UX7wBnTC14Yje7prI8NAJxM70fvULF_7n_Ghnk2IfFGO6U6CLaNsPsMch-5ViMriZN0ZPZEUTwxZ-KInEKUk9symfjrvGkjrvnbXB2JTD1qjk.LUW4A-ok3_fEHzl_wq0zKgOPjYHhGxMDLEDjU1fw8nk&dib_tag=se&keywords=Laptop&qid=1763772984&sprefix=laptop%2Caps%2C802&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1');
  await page.getByRole('radio', { name: 'Gray $499.99 with 50 percent' }).click();
  //await page.getByRole('radio', { name: 'Red $499.99 with 50 percent' }).click();
  //await page.getByRole('link', { name: 'items in cart' }).click();
  //await page.getByRole('link', { name: 'Returns & Orders' }).click();
  //await page.getByRole('link', { name: 'Amazon', exact: true }).click();
});