import { test, expect } from '@playwright/test';

test('Browse deals page', async ({ page }) => {
  await page.goto('https://amazon.com');
  
  await page.locator('a[href*="deals"]').first().click();
  await page.waitForLoadState('networkidle');
  
  await expect(page).toHaveURL(/deals/);
  await expect(page.locator('[data-testid="deal-card"]')).toBeVisible();
});