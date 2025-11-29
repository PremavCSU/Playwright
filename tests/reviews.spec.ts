import { test, expect } from '@playwright/test';

test('View product reviews', async ({ page }) => {
  await page.goto('https://amazon.com');
  
  await page.locator('#twotabsearchtextbox').fill('tablet');
  await page.locator('#twotabsearchtextbox').press('Enter');
  await page.waitForLoadState('networkidle');
  
  await page.locator('[data-component-type="s-search-result"] h2 a').first().click();
  await page.waitForLoadState('networkidle');
  
  const reviewsLink = page.locator('a[href*="product-reviews"], a:has-text("See all reviews")').first();
  if (await reviewsLink.isVisible()) {
    await reviewsLink.click();
    await page.waitForLoadState('networkidle');
    await expect(page.locator('[data-hook="review-body"], .review-text').first()).toBeVisible();
  } else {
    await expect(page.locator('#productTitle')).toBeVisible();
  }
});