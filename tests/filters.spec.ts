import { test, expect } from '@playwright/test';

test('Apply search filters', async ({ page }) => {
  await page.goto('https://amazon.com');
  
  await page.locator('#twotabsearchtextbox').fill('headphones');
  await page.locator('#twotabsearchtextbox').press('Enter');
  await page.waitForTimeout(3000);
  
  const primeFilter = page.locator('[data-cy="prime-filter"], input[name="s-ref-checkbox-Prime"], span:has-text("Prime")').first();
  if (await primeFilter.isVisible()) {
    await primeFilter.click();
    await page.waitForTimeout(3000);
  }
  
  await expect(page).toHaveURL(/s\?k=headphones/);
});