import { test, expect, Page } from '@playwright/test';

const search = async (page: Page, term: string) => {
  await page.locator('#twotabsearchtextbox').fill(term);
  await page.locator('#twotabsearchtextbox').press('Enter');
  await page.waitForLoadState('networkidle');
};

test('Amazon multi-product search', async ({ page }) => {
  await page.goto('https://amazon.com');
  
  await search(page, 'phone');
  await expect(page).toHaveURL(/s\?k=phone/);
  await expect(page.locator('[data-component-type="s-search-result"]')).toBeVisible();
  
  await search(page, 'laptop');
  await expect(page).toHaveURL(/s\?k=laptop/);
  await expect(page.locator('[data-component-type="s-search-result"]')).toBeVisible();
  
  await search(page, 'TV');
  await expect(page).toHaveURL(/s\?k=TV/);
  await expect(page.locator('[data-component-type="s-search-result"]')).toBeVisible();
});