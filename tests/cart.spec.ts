import { test, expect } from '@playwright/test';

test('Add item to cart', async ({ page }) => {
  await page.goto('https://amazon.com');
  
  await page.locator('#twotabsearchtextbox').fill('wireless mouse');
  await page.locator('#twotabsearchtextbox').press('Enter');
  await page.waitForLoadState('networkidle');
  
  await page.locator('[data-component-type="s-search-result"]').first().click();
  await page.waitForLoadState('networkidle');
  
  const addToCartButton = page.locator('#add-to-cart-button, input[name="submit.add-to-cart"]').first();
  if (await addToCartButton.isVisible()) {
    await addToCartButton.click();
  }
  
  await expect(page.locator('#sw-atc-details-single-container, #attachDisplayAddBaseAlert, [data-testid="add-to-cart-success"]').first()).toBeVisible({ timeout: 10000 });
});