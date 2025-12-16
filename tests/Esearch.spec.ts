import { test, expect } from '@playwright/test';

test('Amazon Electronics items search', async ({ page }) => {
  test.setTimeout(60000);

  await page.goto('https://amazon.com');
  
  // Search for phone
  await page.locator('#twotabsearchtextbox').fill('phone');
  await page.locator('#twotabsearchtextbox').press('Enter');
  await page.waitForTimeout(3000);
  await expect(page).toHaveURL(/s\?k=phone/);
  
  // Search for TV
  await page.locator('#twotabsearchtextbox').fill('TV');
  await page.locator('#twotabsearchtextbox').press('Enter');
  await page.waitForTimeout(3000);
  await expect(page).toHaveURL(/s\?k=TV/);
  
  // Search for Laptop
  await page.locator('#twotabsearchtextbox').fill('Laptop');
  await page.locator('#twotabsearchtextbox').press('Enter');
  await page.waitForTimeout(3000);
  await expect(page).toHaveURL(/s\?k=Laptop/);
});