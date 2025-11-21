import { test, expect } from '@playwright/test';

test('Amazon phone search', async ({ page }) => {
  test.setTimeout(60000);
  
  await page.goto('https://amazon.com');
  
  const searchBox = page.getByRole('searchbox', { name: 'Search Amazon' });
  await searchBox.fill('phone');
  await searchBox.press('Enter');
  
  await page.waitForLoadState('networkidle');
  await page.getByRole('link', { name: 'SAMSUNG Galaxy S25 Ultra' }).first().click();
})