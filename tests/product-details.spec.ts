import { test, expect } from '@playwright/test';

test('View product details', async ({ page }) => {
  await page.goto('https://amazon.com');
  
  await page.locator('#twotabsearchtextbox').fill('kindle');
  await page.locator('#twotabsearchtextbox').press('Enter');
  await page.waitForTimeout(3000);
  
  await page.locator('[data-component-type="s-search-result"] h2 a').first().click();
  await page.waitForTimeout(3000);
  
  await expect(page.locator('#productTitle, [data-testid="product-title"]').first()).toBeVisible();
  await expect(page.locator('.a-price, [data-testid="price"]').first()).toBeVisible();
});