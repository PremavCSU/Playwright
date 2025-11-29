import { test, expect } from '@playwright/test';

test('Amazon phone search', async ({ page }) => {
  await page.goto('https://amazon.com');
  
  await page.locator('#twotabsearchtextbox').fill('phone');
  await page.locator('#twotabsearchtextbox').press('Enter');
  await page.waitForLoadState('networkidle');
  
  await expect(page).toHaveURL(/s\?k=phone/);
  await expect(page.locator('[data-component-type="s-search-result"]')).toBeVisible();
});