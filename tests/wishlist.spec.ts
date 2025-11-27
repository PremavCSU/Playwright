import { test, expect } from '@playwright/test';

test('Add to wishlist', async ({ page }) => {
  await page.goto('https://amazon.com');
  
  await page.locator('#twotabsearchtextbox').fill('books');
  await page.locator('#twotabsearchtextbox').press('Enter');
  await page.waitForLoadState('networkidle');
  
  await page.locator('[data-component-type="s-search-result"]').first().click();
  await page.waitForLoadState('networkidle');
  
  await page.locator('#add-to-wishlist-button-submit').click();
  await page.waitForLoadState('networkidle');
});