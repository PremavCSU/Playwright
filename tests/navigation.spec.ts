import { test, expect } from '@playwright/test';

test('Navigate through categories', async ({ page }) => {
  await page.goto('https://amazon.com');
  
  await page.locator('#nav-hamburger-menu').click();
  await page.waitForLoadState('networkidle');
  
  await page.locator('a[href*="electronics"]').first().click();
  await page.waitForLoadState('networkidle');
  
  await expect(page).toHaveURL(/electronics/);
  await expect(page.locator('h1')).toContainText('Electronics');
});