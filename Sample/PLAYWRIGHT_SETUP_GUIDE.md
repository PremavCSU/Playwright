# Playwright Setup and Usage Guide

## Table of Contents
- [Installation](#installation)
- [VS Code Setup](#vs-code-setup)
- [Project Configuration](#project-configuration)
- [Writing Tests](#writing-tests)
- [Running Tests](#running-tests)
- [Debugging](#debugging)
- [Best Practices](#best-practices)
- [Common Patterns](#common-patterns)

## Installation

### Prerequisites
- Node.js 16+ 
- VS Code (recommended)

### Quick Start
```bash
# New project
npm init playwright@latest

# Existing project
npm install -D @playwright/test
npx playwright install
```

### Browser Installation
```bash
# Install all browsers
npx playwright install

# Install specific browser
npx playwright install chromium
npx playwright install firefox
npx playwright install webkit
```

## VS Code Setup

### Required Extensions
1. **Playwright Test for VSCode** (ms-playwright.playwright)
2. **Amazon Q Developer** (amazon-q-vscode)

### Extension Features
- Test Explorer integration
- Run/debug tests from sidebar
- Test generation with codegen
- IntelliSense and auto-completion
- Live test execution preview

### VS Code Settings
```json
{
  "playwright.reuseBrowser": true,
  "playwright.showTrace": true,
  "playwright.testDir": "./tests"
}
```

## Project Configuration

### playwright.config.ts
```typescript
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: 'html',
  use: {
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure'
  },
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] },
    },
    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'] },
    }
  ]
});
```

### package.json Scripts
```json
{
  "scripts": {
    "test": "npx playwright test",
    "test:ui": "npx playwright test --ui",
    "test:debug": "npx playwright test --debug",
    "test:headed": "npx playwright test --headed",
    "report": "npx playwright show-report",
    "codegen": "npx playwright codegen"
  }
}
```

## Writing Tests

### Basic Test Structure
```typescript
import { test, expect } from '@playwright/test';

test('basic test', async ({ page }) => {
  await page.goto('https://example.com');
  await expect(page).toHaveTitle(/Example/);
});
```

### Test Hooks
```typescript
import { test, expect } from '@playwright/test';

test.beforeEach(async ({ page }) => {
  await page.goto('https://example.com');
});

test.afterEach(async ({ page }) => {
  // Cleanup
});

test.describe('Feature tests', () => {
  test('test 1', async ({ page }) => {
    // Test implementation
  });
});
```

### Page Object Model
```typescript
// pages/SearchPage.ts
export class SearchPage {
  constructor(private page: Page) {}

  async search(term: string) {
    await this.page.locator('#search').fill(term);
    await this.page.locator('#search').press('Enter');
  }

  async getResults() {
    return this.page.locator('.result');
  }
}

// test file
import { SearchPage } from '../pages/SearchPage';

test('search functionality', async ({ page }) => {
  const searchPage = new SearchPage(page);
  await searchPage.search('playwright');
  const results = await searchPage.getResults();
  await expect(results).toHaveCount(10);
});
```

## Running Tests

### Command Line Options
```bash
# Run all tests
npx playwright test

# Run specific test file
npx playwright test search.spec.ts

# Run tests by name pattern
npx playwright test --grep "search"

# Run in specific browser
npx playwright test --project=chromium

# Run in headed mode
npx playwright test --headed

# Run with UI mode
npx playwright test --ui

# Run single test
npx playwright test search.spec.ts:10
```

### Parallel Execution
```typescript
// Run tests in parallel (default)
test.describe.configure({ mode: 'parallel' });

// Run tests serially
test.describe.configure({ mode: 'serial' });
```

## Debugging

### Debug Mode
```bash
# Debug specific test
npx playwright test --debug search.spec.ts

# Debug from specific line
npx playwright test search.spec.ts:25 --debug
```

### VS Code Debugging
1. Set breakpoints in test files
2. Use "Debug Test" from Test Explorer
3. Step through code execution

### Browser Developer Tools
```typescript
test('debug test', async ({ page }) => {
  await page.pause(); // Pauses execution
  await page.goto('https://example.com');
});
```

### Screenshots and Videos
```typescript
// Take screenshot
await page.screenshot({ path: 'screenshot.png' });

// Full page screenshot
await page.screenshot({ 
  path: 'fullpage.png', 
  fullPage: true 
});
```

## Best Practices

### Reliable Selectors
```typescript
// Good - ID selectors
await page.locator('#submit-button').click();

// Good - Data attributes
await page.locator('[data-testid="login"]').click();

// Avoid - CSS classes (can change)
await page.locator('.btn-primary').click();
```

### Waiting Strategies
```typescript
// Wait for element
await page.waitForSelector('#element');

// Wait for network
await page.waitForLoadState('networkidle');

// Wait for URL
await page.waitForURL('**/dashboard');

// Auto-waiting (preferred)
await page.locator('#button').click();
```

### Assertions
```typescript
// Page assertions
await expect(page).toHaveTitle('Title');
await expect(page).toHaveURL(/pattern/);

// Element assertions
await expect(page.locator('#element')).toBeVisible();
await expect(page.locator('#element')).toHaveText('Text');
await expect(page.locator('#element')).toHaveCount(5);
```

## Common Patterns

### Form Handling
```typescript
test('form submission', async ({ page }) => {
  await page.goto('/form');
  
  // Fill form fields
  await page.locator('#name').fill('John Doe');
  await page.locator('#email').fill('john@example.com');
  
  // Select dropdown
  await page.locator('#country').selectOption('US');
  
  // Check checkbox
  await page.locator('#terms').check();
  
  // Submit form
  await page.locator('#submit').click();
  
  // Verify result
  await expect(page.locator('#success')).toBeVisible();
});
```

### File Upload
```typescript
test('file upload', async ({ page }) => {
  await page.goto('/upload');
  
  // Upload file
  await page.locator('#file-input').setInputFiles('path/to/file.pdf');
  
  // Verify upload
  await expect(page.locator('#file-name')).toHaveText('file.pdf');
});
```

### API Testing
```typescript
test('API integration', async ({ request }) => {
  // API call
  const response = await request.get('/api/users');
  expect(response.status()).toBe(200);
  
  const users = await response.json();
  expect(users).toHaveLength(10);
});
```

### Mobile Testing
```typescript
test('mobile view', async ({ browser }) => {
  const context = await browser.newContext({
    ...devices['iPhone 12']
  });
  
  const page = await context.newPage();
  await page.goto('/mobile');
  
  // Mobile-specific tests
  await expect(page.locator('#mobile-menu')).toBeVisible();
});
```

### Authentication
```typescript
// Setup authentication
test.beforeEach(async ({ page }) => {
  await page.goto('/login');
  await page.locator('#username').fill('user@example.com');
  await page.locator('#password').fill('password');
  await page.locator('#login-button').click();
  await page.waitForURL('**/dashboard');
});
```

### Test Data Management
```typescript
// Test data factory
const testData = {
  validUser: {
    email: 'test@example.com',
    password: 'password123'
  },
  invalidUser: {
    email: 'invalid@example.com',
    password: 'wrong'
  }
};

test('login with valid credentials', async ({ page }) => {
  await page.goto('/login');
  await page.locator('#email').fill(testData.validUser.email);
  await page.locator('#password').fill(testData.validUser.password);
  await page.locator('#submit').click();
});
```

### Error Handling
```typescript
test('handle network errors', async ({ page }) => {
  // Simulate network failure
  await page.route('**/api/**', route => route.abort());
  
  await page.goto('/app');
  
  // Verify error handling
  await expect(page.locator('#error-message')).toBeVisible();
});
```

## Reports and CI/CD

### HTML Reports
```bash
# Generate and view report
npx playwright show-report
```

### CI Configuration
```yaml
# GitHub Actions
- name: Run Playwright tests
  run: npx playwright test
  
- name: Upload test results
  uses: actions/upload-artifact@v3
  if: always()
  with:
    name: playwright-report
    path: playwright-report/
```

### Custom Reporters
```typescript
// playwright.config.ts
export default defineConfig({
  reporter: [
    ['html'],
    ['json', { outputFile: 'test-results.json' }],
    ['junit', { outputFile: 'results.xml' }]
  ]
});
```