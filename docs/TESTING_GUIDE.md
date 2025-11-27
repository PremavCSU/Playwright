# Testing Guide

## Test Categories

### Search Tests
- Basic search functionality
- Multi-product search
- Category-specific search
- Search with filters

### E-commerce Tests
- Add to cart
- Wishlist management
- Product details viewing
- Review access

### Navigation Tests
- Menu navigation
- Category browsing
- Account access
- Service pages

## Test Patterns

### Standard Test Structure
```typescript
test('feature description', async ({ page }) => {
  // 1. Setup/Navigation
  await page.goto('https://amazon.com');
  
  // 2. Action
  await page.locator('#selector').click();
  
  // 3. Wait
  await page.waitForLoadState('networkidle');
  
  // 4. Assertion
  await expect(page).toHaveURL(/pattern/);
});
```

### Reusable Helper Functions
```typescript
const search = async (page: Page, term: string) => {
  await page.locator('#twotabsearchtextbox').fill(term);
  await page.locator('#twotabsearchtextbox').press('Enter');
  await page.waitForLoadState('networkidle');
};
```

## Selector Strategy

### Priority Order
1. ID selectors: `#elementId`
2. Data attributes: `[data-testid="value"]`
3. Semantic roles: `page.getByRole('button')`
4. Text content: `page.getByText('text')`
5. CSS selectors: `.className`

### Amazon-Specific Selectors
```typescript
// Search
'#twotabsearchtextbox'

// Results
'[data-component-type="s-search-result"]'

// Navigation
'#nav-hamburger-menu'
'#nav-link-accountList'

// Product
'#productTitle'
'#add-to-cart-button'
'.a-price'
```

## Wait Strategies

### Network Stability
```typescript
await page.waitForLoadState('networkidle');
```

### Element Visibility
```typescript
await page.waitForSelector('#element');
```

### URL Changes
```typescript
await page.waitForURL(/pattern/);
```

## Error Handling

### Timeout Issues
```typescript
test.setTimeout(120000); // Increase timeout
await page.waitForSelector('#element', { timeout: 10000 });
```

### Element Not Found
```typescript
const element = page.locator('#element');
await expect(element).toBeVisible({ timeout: 5000 });
```

### Network Failures
```typescript
await page.goto(url, { waitUntil: 'networkidle' });
```