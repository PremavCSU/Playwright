import { test, expect } from '@playwright/test';

test('View product reviews', async ({ page }) => {
  await page.goto('https://amazon.com');
  
  await page.locator('#twotabsearchtextbox').fill('tablet');
  await page.locator('#twotabsearchtextbox').press('Enter');
  await page.waitForTimeout(3000);
  
  await page.locator('[data-component-type="s-search-result"] h2 a').first().click();
  await page.waitForTimeout(3000);
  
  const reviewsLink = page.locator('a[href*="product-reviews"], a:has-text("See all reviews")').first();
  if (await reviewsLink.isVisible()) {
    await reviewsLink.click();
    await page.waitForTimeout(3000);
    await expect(page.locator('[data-hook="review-body"], .review-text').first()).toBeVisible();
  } else {
    await expect(page.locator('#productTitle')).toBeVisible();
  }
});