import { test, expect } from '@playwright/test';

test('Navigate through categories', async ({ page }) => {
  await page.goto('https://amazon.com');
  
  await page.locator('#nav-hamburger-menu').click();
  await page.waitForTimeout(2000);
  
  const electronicsLink = page.locator('a[href*="electronics"], a:has-text("Electronics")').first();
  if (await electronicsLink.isVisible()) {
    await electronicsLink.click();
    await page.waitForLoadState('networkidle');
    await expect(page).toHaveURL(/electronics/);
  } else {
    await page.goto('https://amazon.com/electronics');
  }
  
  await expect(page.locator('h1, [data-testid="page-title"]').first()).toBeVisible();
});