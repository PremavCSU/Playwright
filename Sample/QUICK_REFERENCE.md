# Quick Reference Guide

## Commands Cheat Sheet

### Test Execution
```bash
npx playwright test                    # Run all tests
npx playwright test search.spec.ts    # Run specific file
npx playwright test --ui              # UI mode
npx playwright test --headed          # Show browser
npx playwright test --debug           # Debug mode
npx playwright show-report            # View results
```

### MCP Server
```bash
npm run mcp-server                    # Start server
netstat -ano | findstr :9323         # Check port
taskkill /PID <PID> /F               # Kill process
```

## Selector Quick Reference

```typescript
// Search & Results
'#twotabsearchtextbox'                           // Search box
'[data-component-type="s-search-result"]'        // Results
'select[name="s"]'                               // Sort dropdown

// Navigation
'#nav-hamburger-menu'                            // Menu
'#nav-link-accountList'                          // Account
'a[href*="prime"]'                               // Prime link
'a[href*="deals"]'                               // Deals link

// Product Actions
'#add-to-cart-button'                            // Add to cart
'#add-to-wishlist-button-submit'                 // Wishlist
'#productTitle'                                  // Title
'.a-price'                                       // Price
'[data-hook="review-body"]'                      // Reviews

// Filters
'span:has-text("Prime")'                         // Prime filter
'[data-testid="deal-card"]'                      // Deal cards
```

## Test Pattern Templates

### Basic Test
```typescript
import { test, expect } from '@playwright/test';

test('test name', async ({ page }) => {
  await page.goto('https://amazon.com');
  await page.locator('#selector').click();
  await page.waitForLoadState('networkidle');
  await expect(page).toHaveURL(/pattern/);
});
```

### Search Helper
```typescript
const search = async (page: Page, term: string) => {
  await page.locator('#twotabsearchtextbox').fill(term);
  await page.locator('#twotabsearchtextbox').press('Enter');
  await page.waitForLoadState('networkidle');
};
```

## Amazon Q Commands

```
Run the [testname] test
Generate test for [feature]
Debug failing [testname]
Optimize [filename] performance
Create test for [functionality]
```

## Error Solutions

### Timeout Error
```typescript
test.setTimeout(120000);
await page.waitForSelector('#element', { timeout: 10000 });
```

### Element Not Found
```typescript
await expect(page.locator('#element')).toBeVisible();
```

### Port Conflict
```bash
netstat -ano | findstr :9323
taskkill /PID <PID> /F
```

## File Structure
```
tests/
├── search.spec.ts         # Basic search
├── cart.spec.ts           # Shopping cart
├── navigation.spec.ts     # Menu navigation
├── filters.spec.ts        # Search filters
├── product-details.spec.ts # Product pages
└── [10 more test files]
```