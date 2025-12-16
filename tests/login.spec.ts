import { test, expect } from '@playwright/test';

test('Amazon login page elements', async ({ page }) => {
  await page.goto('https://amazon.com');
  
  await page.click('#nav-link-accountList');
  await page.waitForLoadState('networkidle');
  
  await expect(page.locator('#ap_email')).toBeVisible();
  await expect(page.locator('#continue')).toBeVisible();
  await expect(page).toHaveTitle(/Sign/);
});

test('login form validation', async ({ page }) => {
  await page.goto('https://amazon.com/ap/signin');
  
  await page.click('#continue');
  
  await expect(page.locator('.a-alert-error')).toBeVisible();
});