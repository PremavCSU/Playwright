import { test, expect } from '@playwright/test';

test('search for TV on Amazon', async ({ page }) => {
  await page.goto('https://amazon.com');
  
  await page.fill('#twotabsearchtextbox', 'TV');
  await page.click('#nav-search-submit-button');
  
  await expect(page).toHaveTitle(/TV/);
});