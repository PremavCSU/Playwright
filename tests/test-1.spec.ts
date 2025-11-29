import { test, expect } from '@playwright/test';

test('Simple Amazon search test', async ({ page }) => {
  await page.goto('https://amazon.com');
  
  await page.locator('#twotabsearchtextbox').fill('laptop');
  await page.locator('#twotabsearchtextbox').press('Enter');
  await page.waitForLoadState('networkidle');
  
  await expect(page).toHaveURL(/s\?k=laptop/);
  await expect(page.locator('[data-component-type="s-search-result"]')).toBeVisible();
});