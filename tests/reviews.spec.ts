import { test, expect } from '@playwright/test';

test('View product reviews', async ({ page }) => {
  await page.goto('https://amazon.com');
  
  await page.locator('#twotabsearchtextbox').fill('tablet');
  await page.locator('#twotabsearchtextbox').press('Enter');
  await page.waitForLoadState('networkidle');
  
  await page.locator('[data-component-type="s-search-result"]').first().click();
  await page.waitForLoadState('networkidle');
  
  await page.locator('a[href*="product-reviews"]').first().click();
  await page.waitForLoadState('networkidle');
  
  await expect(page.locator('[data-hook="review-body"]')).toBeVisible();
});