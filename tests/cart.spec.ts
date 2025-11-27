import { test, expect } from '@playwright/test';

test('Add item to cart', async ({ page }) => {
  await page.goto('https://amazon.com');
  
  await page.locator('#twotabsearchtextbox').fill('wireless mouse');
  await page.locator('#twotabsearchtextbox').press('Enter');
  await page.waitForLoadState('networkidle');
  
  await page.locator('[data-component-type="s-search-result"]').first().click();
  await page.waitForLoadState('networkidle');
  
  await page.locator('#add-to-cart-button').click();
  await expect(page.locator('#attachDisplayAddBaseAlert')).toBeVisible();
});