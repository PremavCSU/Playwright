import { test, expect } from '@playwright/test';

test('Browse deals page', async ({ page }) => {
  await page.goto('https://amazon.com/deals');
  await page.waitForTimeout(3000);
  
  await expect(page).toHaveURL(/deals/);
  await expect(page.locator('[data-testid="deal-card"], .DealCard, .a-section').first()).toBeVisible();
});