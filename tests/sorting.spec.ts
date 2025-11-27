import { test, expect } from '@playwright/test';

test('Sort search results', async ({ page }) => {
  await page.goto('https://amazon.com');
  
  await page.locator('#twotabsearchtextbox').fill('shoes');
  await page.locator('#twotabsearchtextbox').press('Enter');
  await page.waitForLoadState('networkidle');
  
  await page.locator('select[name="s"]').selectOption('price-asc-rank');
  await page.waitForLoadState('networkidle');
  
  await expect(page).toHaveURL(/price-asc-rank/);
});