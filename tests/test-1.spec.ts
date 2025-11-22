import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('https://www.amazon.com/');
  await page.getByRole('textbox', { name: 'Search For' }).click();
  await page.getByRole('textbox', { name: 'Search For' }).fill('laptop');
  await page.getByRole('textbox', { name: 'Search For' }).press('Enter');
  await page.getByRole('button', { name: 'Go' }).click();
  await page.getByRole('link', { name: 'Microsoft Surface Laptop (' }).first().click();
  await page.goto('https://www.amazon.com/dp/B0DZBMVVLT/?_encoding=UTF8&pd_rd_i=B0DZBMVVLT&ref_=sbx_be_s_sparkle_ssd_img&qid=1763771593&pd_rd_w=Bw1Kl&content-id=amzn1.sym.9f2b2b9e-47e9-4764-a4dc-2be2f6fca36d%3Aamzn1.sym.9f2b2b9e-47e9-4764-a4dc-2be2f6fca36d&pf_rd_p=9f2b2b9e-47e9-4764-a4dc-2be2f6fca36d&pf_rd_r=TG00RECQARTZ75F16BNN&pd_rd_wg=YlJrl&pd_rd_r=9372d663-fb1a-483b-8628-86138969c96c&pd_rd_plhdr=t&th=1');
  await page.getByRole('radio', { name: 'Snapdragon X Plus (8 core)', exact: true }).click();
  await page.getByRole('link', { name: 'Amazon', exact: true }).click();
  await page.getByRole('searchbox', { name: 'Search Amazon' }).click();
  await page.getByRole('searchbox', { name: 'Search Amazon' }).fill('TV');
  await page.getByRole('searchbox', { name: 'Search Amazon' }).press('Enter');
  await page.getByRole('button', { name: 'Go', exact: true }).click();
  await page.getByRole('link', { name: 'Sponsored Ad - Amazon Fire TV 40" 2-Series, HD smart TV with Fire TV Alexa' }).click();
  await page.goto('https://www.amazon.com/s?k=TV&crid=29ULPS5SDB3BL&sprefix=tv%2Caps%2C112&ref=nb_sb_noss_1');
  await page.getByRole('link', { name: 'Apply 44 to 49 Inches filter' }).click();
  await page.getByRole('link', { name: 'Apply New filter to narrow' }).click();
  await page.getByRole('link', { name: 'Hisense 50" Class A7 Series (' }).click();
});