import { test, expect } from '@playwright/test';

test('Prime membership page', async ({ page }) => {
  await page.goto('https://amazon.com/prime');
  await page.waitForTimeout(3000);
  
  await expect(page).toHaveURL(/prime/);
  await expect(page.locator('h1, [data-testid="prime-title"], .prime-header').first()).toBeVisible();
});