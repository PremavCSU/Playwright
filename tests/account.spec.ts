import { test, expect } from '@playwright/test';

test('Access account menu', async ({ page }) => {
  await page.goto('https://amazon.com');
  
  await page.locator('#nav-link-accountList').hover();
  await page.waitForLoadState('networkidle');
  
  await expect(page.locator('#nav-flyout-accountList')).toBeVisible();
  await expect(page.locator('a:has-text("Sign in")')).toBeVisible();
});