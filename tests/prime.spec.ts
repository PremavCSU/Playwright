import { test, expect } from '@playwright/test';

test('Prime membership page', async ({ page }) => {
  await page.goto('https://amazon.com');
  
  await page.locator('a[href*="prime"]').first().click();
  await page.waitForLoadState('networkidle');
  
  await expect(page).toHaveURL(/prime/);
  await expect(page.locator('h1')).toContainText('Prime');
});