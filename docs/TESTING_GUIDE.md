# Testing Guide

## Test Execution

### TypeScript Tests (Playwright)

#### Basic Commands
```bash
# Run all tests
npx playwright test

# Run specific test file
npx playwright test tests/search.spec.ts

# Run tests with UI mode
npx playwright test --ui

# Run tests in headed mode
npx playwright test --headed

# Run specific browser
npx playwright test --project=chromium
```

#### Advanced Options
```bash
# Run tests with debugging
npx playwright test --debug

# Run tests with trace
npx playwright test --trace on

# Run tests in parallel
npx playwright test --workers=4

# Run tests with custom timeout
npx playwright test --timeout=60000
```

### Python Tests (Pytest)

#### Basic Commands
```bash
# Run all pytest tests
python -m pytest pytest_tests/ -v

# Run specific test file
python -m pytest pytest_tests/test_search.py -v

# Run specific test function
python -m pytest pytest_tests/test_search.py::test_amazon_phone_search -v

# Run with HTML report
python -m pytest pytest_tests/ --html=pytest_reports/report.html
```

#### Advanced Options
```bash
# Run tests in parallel
python -m pytest pytest_tests/ -n 4

# Run with custom markers
python -m pytest pytest_tests/ -m "not slow"

# Run with verbose output
python -m pytest pytest_tests/ -vv --tb=long

# Run using runner script
python pytest_tests/run_tests.py
python pytest_tests/run_tests.py search
```

## Test Structure

### TypeScript Test Pattern
```typescript
import { test, expect } from '@playwright/test';

test('test description', async ({ page }) => {
  await page.goto('https://amazon.com');
  await page.locator('#selector').fill('text');
  await expect(page.locator('#result')).toBeVisible();
});
```

### Python Test Pattern
```python
import pytest
from playwright.sync_api import expect

def test_function_name(amazon_page):
    amazon_page.locator('#selector').fill('text')
    assert amazon_page.locator('#result').is_visible()
```

## Test Categories

### Search Tests
- `search.spec.ts` / `test_search.py`: Basic search functionality
- `optimized-search.spec.ts` / `test_optimized_search.py`: Multi-product search
- `Esearch.spec.ts` / `test_esearch.py`: Electronics search

### User Interface Tests
- `account.spec.ts` / `test_account.py`: User account operations
- `cart.spec.ts` / `test_cart.py`: Shopping cart functionality
- `navigation.spec.ts` / `test_navigation.py`: Site navigation

### Product Tests
- `product-details.spec.ts` / `test_product_details.py`: Product page testing
- `reviews.spec.ts` / `test_reviews.py`: Product reviews
- `wishlist.spec.ts` / `test_wishlist.py`: Wishlist operations

### Feature Tests
- `prime.spec.ts` / `test_prime.py`: Amazon Prime features
- `deals.spec.ts` / `test_deals.py`: Deals and promotions
- `filters.spec.ts` / `test_filters.py`: Product filtering
- `sorting.spec.ts` / `test_sorting.py`: Product sorting

## Best Practices

### Selector Strategy
1. **Prefer stable selectors**: Use IDs over CSS classes
2. **Use data attributes**: `[data-testid="element"]`
3. **Avoid text-based selectors**: Text can change frequently
4. **Use role-based selectors**: `page.getByRole('button', { name: 'Submit' })`

### Wait Strategies
```typescript
// Wait for network to be idle
await page.waitForLoadState('networkidle');

// Wait for specific element
await page.waitForSelector('#element');

// Wait with timeout
await page.waitForTimeout(3000);
```

### Error Handling
```typescript
try {
  await page.locator('#element').click({ timeout: 5000 });
} catch (error) {
  console.log('Element not found:', error);
}
```

## Debugging

### TypeScript Debugging
```bash
# Run with debug mode
npx playwright test --debug

# Generate trace
npx playwright test --trace on

# Show trace viewer
npx playwright show-trace trace.zip
```

### Python Debugging
```python
# Add breakpoint in test
import pdb; pdb.set_trace()

# Run with debugging
python -m pytest pytest_tests/test_search.py -s --pdb
```

## Reporting

### View Reports
```bash
# Playwright HTML report
npx playwright show-report

# Pytest HTML report
# Open pytest_reports/report.html in browser
```

### Report Contents
- Test execution summary
- Failed test details
- Screenshots and videos
- Trace files for debugging
- Performance metrics

## CI/CD Integration

### GitHub Actions Example
```yaml
- name: Run Playwright tests
  run: npx playwright test
  
- name: Upload test results
  uses: actions/upload-artifact@v3
  with:
    name: playwright-report
    path: playwright-report/
```

### Environment Variables
```bash
# Set headless mode for CI
export CI=true

# Custom timeout
export PLAYWRIGHT_TIMEOUT=60000
```