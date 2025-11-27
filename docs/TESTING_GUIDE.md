# Testing Guide

## Test Categories

### Search Tests (4 files)
- **search.spec.ts**: Basic Amazon search functionality
- **amazon-search.spec.ts**: TV-specific search test
- **optimized-search.spec.ts**: Multi-product search with reusable helper
- **Esearch.spec.ts**: Electronics category search

### E-commerce Tests (4 files)
- **cart.spec.ts**: Add items to shopping cart
- **wishlist.spec.ts**: Add items to wishlist
- **product-details.spec.ts**: Product page validation
- **reviews.spec.ts**: Product reviews access

### Navigation Tests (4 files)
- **navigation.spec.ts**: Category menu navigation
- **filters.spec.ts**: Search result filtering
- **sorting.spec.ts**: Search result sorting
- **deals.spec.ts**: Deals page browsing

### Account & Services Tests (2 files)
- **account.spec.ts**: Account menu accessibility
- **prime.spec.ts**: Prime membership page

## Test Patterns

### Standard Test Structure
```typescript
import { test, expect } from '@playwright/test';

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
import { Page } from '@playwright/test';

const search = async (page: Page, term: string) => {
  await page.locator('#twotabsearchtextbox').fill(term);
  await page.locator('#twotabsearchtextbox').press('Enter');
  await page.waitForLoadState('networkidle');
};

const addToCart = async (page: Page) => {
  await page.locator('#add-to-cart-button').click();
  await expect(page.locator('#attachDisplayAddBaseAlert')).toBeVisible();
};

const navigateToCategory = async (page: Page, category: string) => {
  await page.locator('#nav-hamburger-menu').click();
  await page.waitForLoadState('networkidle');
  await page.locator(`a[href*="${category}"]`).first().click();
};
```

## Selector Strategy

### Priority Order
1. **ID selectors**: `#elementId` (most reliable)
2. **Data attributes**: `[data-testid="value"]`
3. **Semantic roles**: `page.getByRole('button')`
4. **Text content**: `page.getByText('text')`
5. **CSS selectors**: `.className`

### Amazon-Specific Selectors
```typescript
// Search Elements
'#twotabsearchtextbox'                    // Main search box
'[data-component-type="s-search-result"]' // Search results
'select[name="s"]'                        // Sort dropdown

// Navigation Elements
'#nav-hamburger-menu'                     // Menu button
'#nav-link-accountList'                   // Account menu
'#nav-flyout-accountList'                 // Account dropdown

// Product Elements
'#productTitle'                           // Product title
'#add-to-cart-button'                     // Add to cart
'#add-to-wishlist-button-submit'          // Add to wishlist
'.a-price'                                // Price display
'[data-hook="review-body"]'               // Review content

// Filter Elements
'span:has-text("Prime")'                  // Prime filter
'[data-testid="deal-card"]'               // Deal cards
```

## Wait Strategies

### Network Stability (Recommended)
```typescript
await page.waitForLoadState('networkidle');
```

### Element Visibility
```typescript
await page.waitForSelector('#element');
await expect(page.locator('#element')).toBeVisible();
```

### URL Changes
```typescript
await page.waitForURL(/pattern/);
await expect(page).toHaveURL(/pattern/);
```

### Custom Waits
```typescript
// Wait for specific content
await page.waitForFunction(() => 
  document.querySelectorAll('[data-component-type="s-search-result"]').length > 0
);

// Wait with timeout
await page.waitForSelector('#element', { timeout: 10000 });
```

## Error Handling

### Timeout Issues
```typescript
// Global timeout increase
test.setTimeout(120000); // 2 minutes

// Specific element timeout
await page.waitForSelector('#element', { timeout: 10000 });

// Action timeout
await page.locator('#button').click({ timeout: 5000 });
```

### Element Not Found
```typescript
// Check element existence
const element = page.locator('#element');
await expect(element).toBeVisible({ timeout: 5000 });

// Conditional actions
if (await page.locator('#optional-element').isVisible()) {
  await page.locator('#optional-element').click();
}
```

### Network Failures
```typescript
// Retry navigation
for (let i = 0; i < 3; i++) {
  try {
    await page.goto('https://amazon.com', { waitUntil: 'networkidle' });
    break;
  } catch (error) {
    if (i === 2) throw error;
    await page.waitForTimeout(1000);
  }
}
```

## Test Organization

### File Naming Convention
```
[feature].spec.ts
- search.spec.ts
- cart.spec.ts
- navigation.spec.ts
```

### Test Grouping
```typescript
test.describe('Search Functionality', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('https://amazon.com');
  });

  test('basic search', async ({ page }) => {
    // Test implementation
  });

  test('filtered search', async ({ page }) => {
    // Test implementation
  });
});
```

## Amazon Q Integration

### AI-Powered Test Generation
```
// Amazon Q commands
"Generate test for product comparison"
"Create cart functionality test"
"Add test for user login flow"
```

### Context Usage
```
@workspace - Full project context
@file tests/search.spec.ts - Specific file
@folder tests/ - Directory context
```

### Test Optimization
```
"Optimize the search test performance"
"Refactor cart.spec.ts using Page Object Model"
"Debug failing navigation test"
```

## Performance Guidelines

### Test Execution Speed
- Target: < 3 seconds per test
- Use `networkidle` for stability
- Minimize unnecessary waits
- Reuse browser contexts when possible

### Resource Management
```typescript
// Efficient selector usage
const searchBox = page.locator('#twotabsearchtextbox');
await searchBox.fill('laptop');
await searchBox.press('Enter');

// Avoid repeated navigation
test.describe.configure({ mode: 'serial' });
```