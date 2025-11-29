import { test, expect } from '@playwright/test';

test('Access account menu', async ({ page }) => {
  await page.goto('https://amazon.com');
  
  await page.locator('#nav-link-accountList').hover();
  await page.waitForTimeout(2000);
  
  await expect(page.locator('#nav-flyout-accountList, .nav-flyout-content').first()).toBeVisible();
  await expect(page.locator('a[data-nav-role="signin"], a:has-text("Sign in")').first()).toBeVisible();
});