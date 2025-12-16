# API Reference

## Playwright TypeScript API

### Page Object
```typescript
// Navigation
await page.goto(url, options?)
await page.goBack()
await page.goForward()
await page.reload()

// Locators
page.locator(selector)
page.getByRole(role, options?)
page.getByText(text, options?)
page.getByLabel(text, options?)
page.getByTestId(testId)

// Actions
await locator.click(options?)
await locator.fill(value)
await locator.type(text, options?)
await locator.press(key)
await locator.selectOption(values)

// Assertions
await expect(locator).toBeVisible()
await expect(locator).toHaveText(text)
await expect(locator).toHaveValue(value)
await expect(page).toHaveURL(url)
```

### Test Structure
```typescript
import { test, expect } from '@playwright/test';

test.describe('Test Suite', () => {
  test.beforeEach(async ({ page }) => {
    // Setup code
  });

  test('test name', async ({ page }) => {
    // Test implementation
  });

  test.afterEach(async ({ page }) => {
    // Cleanup code
  });
});
```

### Fixtures
```typescript
// Built-in fixtures
test('example', async ({ page, context, browser }) => {
  // page: Page instance
  // context: Browser context
  // browser: Browser instance
});

// Custom fixtures
const test = base.extend<{ amazonPage: Page }>({
  amazonPage: async ({ page }, use) => {
    await page.goto('https://amazon.com');
    await use(page);
  },
});
```

## Python Playwright API

### Page Object
```python
# Navigation
page.goto(url, timeout=30000)
page.go_back()
page.go_forward()
page.reload()

# Locators
page.locator(selector)
page.get_by_role(role, name=None)
page.get_by_text(text, exact=False)
page.get_by_label(text, exact=False)
page.get_by_test_id(test_id)

# Actions
locator.click(timeout=30000)
locator.fill(value)
locator.type(text, delay=None)
locator.press(key)
locator.select_option(value)

# Assertions
expect(locator).to_be_visible()
expect(locator).to_have_text(text)
expect(locator).to_have_value(value)
expect(page).to_have_url(url)
```

### Pytest Structure
```python
import pytest
from playwright.sync_api import Page, expect

class TestAmazon:
    def setup_method(self):
        # Setup code
        pass

    def test_example(self, amazon_page: Page):
        # Test implementation
        pass

    def teardown_method(self):
        # Cleanup code
        pass
```

### Fixtures (conftest.py)
```python
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

@pytest.fixture
def amazon_page(page):
    page.goto("https://amazon.com")
    return page
```

## Common Selectors

### Amazon-Specific Selectors
```typescript
// Search elements
'#twotabsearchtextbox'                    // Search input
'#nav-search-submit-button'               // Search button
'[data-component-type="s-search-result"]' // Search results

// Navigation elements
'#nav-hamburger-menu'                     // Menu button
'#nav-cart'                              // Cart icon
'#nav-link-accountList'                  // Account menu

// Product elements
'#productTitle'                          // Product title
'#priceblock_dealprice'                  // Product price
'#add-to-cart-button'                    // Add to cart
'#buy-now-button'                        // Buy now

// Filter elements
'[data-cy="filter-departments"]'         // Department filter
'[data-cy="filter-price"]'              // Price filter
'[data-cy="filter-brand"]'              // Brand filter
```

### Wait Strategies
```typescript
// Network idle
await page.waitForLoadState('networkidle');

// DOM content loaded
await page.waitForLoadState('domcontentloaded');

// Element visible
await page.waitForSelector('#element', { state: 'visible' });

// Element hidden
await page.waitForSelector('#element', { state: 'hidden' });

// Custom condition
await page.waitForFunction(() => {
  return document.querySelectorAll('.result').length > 0;
});
```

## Error Handling

### TypeScript Error Handling
```typescript
try {
  await page.locator('#element').click({ timeout: 5000 });
} catch (error) {
  if (error.name === 'TimeoutError') {
    console.log('Element not found within timeout');
  }
  throw error;
}
```

### Python Error Handling
```python
from playwright.sync_api import TimeoutError

try:
    page.locator('#element').click(timeout=5000)
except TimeoutError:
    print('Element not found within timeout')
    raise
```

## Configuration Options

### Playwright Config
```typescript
export default defineConfig({
  testDir: './tests',
  fullyParallel: true,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: 'html',
  use: {
    baseURL: 'https://amazon.com',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
  },
  projects: [
    { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
    { name: 'firefox', use: { ...devices['Desktop Firefox'] } },
    { name: 'webkit', use: { ...devices['Desktop Safari'] } },
  ],
});
```

### Pytest Config
```ini
[tool:pytest]
testpaths = pytest_tests
addopts = 
    -v
    --tb=short
    --html=pytest_reports/report.html
    --self-contained-html
markers =
    slow: marks tests as slow running
    integration: marks tests as integration tests
```

## MCP Server API

### Tool Definition
```javascript
{
  name: 'run_playwright_test',
  description: 'Run Playwright tests',
  inputSchema: {
    type: 'object',
    properties: {
      testFile: {
        type: 'string',
        description: 'Test file to run',
      },
    },
  },
}
```

### Usage Example
```javascript
// Execute test via MCP
const result = await callTool('run_playwright_test', {
  testFile: 'tests/search.spec.ts'
});
```