import { test, expect } from '@playwright/test';

test('Apply search filters', async ({ page }) => {
  await page.goto('https://amazon.com');
  
  await page.locator('#twotabsearchtextbox').fill('headphones');
  await page.locator('#twotabsearchtextbox').press('Enter');
  await page.waitForLoadState('networkidle');
  
  await page.locator('span:has-text("Prime")').first().click();
  await page.waitForLoadState('networkidle');
  
  await expect(page).toHaveURL(/prime/);
});