# API Reference Guide

## Playwright Test API

### Core Imports
```typescript
import { test, expect, Page } from '@playwright/test';
```

### Test Functions
```typescript
test('description', async ({ page }) => {
  // Test implementation
});

test.describe('group', () => {
  // Grouped tests
});

test.beforeEach(async ({ page }) => {
  // Setup before each test
});
```

### Page Methods
```typescript
// Navigation
await page.goto(url);
await page.goBack();
await page.reload();

// Locators
page.locator(selector);
page.getByRole(role);
page.getByText(text);

// Actions
await page.click(selector);
await page.fill(selector, text);
await page.press(selector, key);

// Waits
await page.waitForLoadState('networkidle');
await page.waitForSelector(selector);
await page.waitForURL(pattern);
```

### Assertions
```typescript
// Page assertions
await expect(page).toHaveURL(pattern);
await expect(page).toHaveTitle(title);

// Element assertions
await expect(locator).toBeVisible();
await expect(locator).toContainText(text);
await expect(locator).toHaveAttribute(name, value);
```

## MCP Server API

### Tool Definition
```javascript
{
  name: "run_playwright_test",
  description: "Execute Playwright tests",
  inputSchema: {
    type: "object",
    properties: {
      testFile: { type: "string" },
      testName: { type: "string" }
    }
  }
}
```

### Server Implementation
```javascript
server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [/* tool definitions */]
}));

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  // Tool execution logic
});
```

## Amazon Q Integration API

### Context Annotations
- `@workspace` - Include project context
- `@file filename` - Include specific file
- `@folder foldername` - Include directory
- `@prompt promptname` - Include saved prompt

### AI Commands
```
Generate test for [functionality]
Optimize test [filename]
Debug test failure in [testname]
Refactor [filename] using Page Object Model
```