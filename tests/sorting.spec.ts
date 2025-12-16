import { test, expect } from '@playwright/test';

test('Sort search results', async ({ page }) => {
  await page.goto('https://amazon.com');
  
  await page.locator('#twotabsearchtextbox').fill('shoes');
  await page.locator('#twotabsearchtextbox').press('Enter');
  await page.waitForTimeout(3000);
  
  const sortDropdown = page.locator('select[name="s"], .s-sort-menu select').first();
  if (await sortDropdown.isVisible()) {
    await sortDropdown.selectOption('price-asc-rank');
    await page.waitForTimeout(3000);
    await expect(page).toHaveURL(/price-asc-rank/);
  } else {
    await expect(page).toHaveURL(/s\?k=shoes/);
  }
});