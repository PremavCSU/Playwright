# Playwright Test Suite - Project Reference Documentation

## Table of Contents
- [Project Structure](#project-structure)
- [Test Files Reference](#test-files-reference)
- [Configuration Files](#configuration-files)
- [MCP Integration](#mcp-integration)
- [Amazon Q Integration](#amazon-q-integration)
- [Commands Reference](#commands-reference)
- [Selectors Guide](#selectors-guide)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)

## Project Structure

```
Playwright/
├── tests/                      # Test specification files
│   ├── search.spec.ts         # Basic search functionality
│   ├── amazon-search.spec.ts  # TV search test
│   ├── optimized-search.spec.ts # Multi-product search
│   ├── Esearch.spec.ts        # Electronics search
│   ├── cart.spec.ts           # Shopping cart tests
│   ├── navigation.spec.ts     # Category navigation
│   ├── filters.spec.ts        # Search filters
│   ├── product-details.spec.ts # Product page tests
│   ├── wishlist.spec.ts       # Wishlist functionality
│   ├── sorting.spec.ts        # Result sorting
│   ├── reviews.spec.ts        # Product reviews
│   ├── account.spec.ts        # Account menu
│   ├── prime.spec.ts          # Prime membership
│   └── deals.spec.ts          # Deals page
├── docs/                      # Documentation
├── playwright.config.ts       # Playwright configuration
├── mcp-server.js             # MCP server implementation
├── package.json              # Dependencies and scripts
└── README.md                 # Project overview
```

## Test Files Reference

### Core Search Tests
- **search.spec.ts**: Basic Amazon search functionality
- **amazon-search.spec.ts**: TV-specific search test
- **optimized-search.spec.ts**: Multi-product search with reusable function
- **Esearch.spec.ts**: Electronics category search

### E-commerce Functionality Tests
- **cart.spec.ts**: Add items to shopping cart
- **wishlist.spec.ts**: Add items to wishlist
- **product-details.spec.ts**: Product page validation
- **reviews.spec.ts**: Product reviews access

### Navigation & Discovery Tests
- **navigation.spec.ts**: Category menu navigation
- **filters.spec.ts**: Search result filtering
- **sorting.spec.ts**: Search result sorting
- **deals.spec.ts**: Deals page browsing

### Account & Services Tests
- **account.spec.ts**: Account menu accessibility
- **prime.spec.ts**: Prime membership page

## Configuration Files

### playwright.config.ts
```typescript
// Test configuration with 60s timeout
// Chromium browser (default)
// Network idle wait strategy
```

### package.json Scripts
```json
{
  "test": "npx playwright test",
  "test:ui": "npx playwright test --ui",
  "mcp-server": "node mcp-server.js"
}
```

## MCP Integration

### Server Configuration
- **Port**: 9323 (default)
- **Transport**: stdio
- **Protocol**: Model Context Protocol

### Available Tools
- `run_playwright_test`: Execute Playwright tests via MCP

### Starting MCP Server
```bash
npm run mcp-server
```

### Port Conflict Resolution
```bash
# Find process using port 9323
netstat -ano | findstr :9323

# Kill process
taskkill /PID <PID> /F
```

## Amazon Q Integration

### Features
- AI-powered test generation
- Code optimization suggestions
- Automated debugging assistance
- Test refactoring recommendations

### Usage Patterns
```
@workspace - Include project context
@file - Include specific files
@folder - Include directory context
```

### Integration Workflow
1. Install Amazon Q Developer extension
2. Start MCP server
3. Use context annotations
4. Request AI assistance

## Commands Reference

### Test Execution
```bash
# Run all tests
npx playwright test

# Run specific test file
npx playwright test tests/search.spec.ts

# Run with UI mode
npx playwright test --ui

# Run specific test by name
npx playwright test --grep "Amazon search"

# Run tests in headed mode
npx playwright test --headed

# Generate test report
npx playwright show-report
```

### Development Commands
```bash
# Install dependencies
npm install

# Start MCP server
npm run mcp-server

# Debug specific test
npx playwright test tests/cart.spec.ts --debug
```

## Selectors Guide

### Primary Selectors
```typescript
// Search box
'#twotabsearchtextbox'

// Search results
'[data-component-type="s-search-result"]'

// Add to cart button
'#add-to-cart-button'

// Navigation menu
'#nav-hamburger-menu'

// Account menu
'#nav-link-accountList'

// Price elements
'.a-price'

// Product title
'#productTitle'
```

### Selector Hierarchy
1. **ID selectors** (most reliable): `#elementId`
2. **Data attributes**: `[data-testid="value"]`
3. **Class selectors**: `.className`
4. **Text content**: `text="Button Text"`
5. **CSS selectors**: `button.primary`

## Best Practices

### Test Structure
```typescript
import { test, expect } from '@playwright/test';

test('Test description', async ({ page }) => {
  // Navigate
  await page.goto('https://amazon.com');
  
  // Interact
  await page.locator('#selector').click();
  
  // Wait for stability
  await page.waitForLoadState('networkidle');
  
  // Assert
  await expect(page).toHaveURL(/expected-pattern/);
});
```

### Reusable Functions
```typescript
const search = async (page: Page, term: string) => {
  await page.locator('#twotabsearchtextbox').fill(term);
  await page.locator('#twotabsearchtextbox').press('Enter');
  await page.waitForLoadState('networkidle');
};
```

### Wait Strategies
- `waitForLoadState('networkidle')`: Network requests complete
- `waitForSelector()`: Element appears
- `waitForURL()`: URL matches pattern

## Troubleshooting

### Common Issues

#### Test Timeouts
```typescript
// Increase timeout for slow operations
test.setTimeout(120000); // 2 minutes
```

#### Element Not Found
```typescript
// Add explicit waits
await page.waitForSelector('#element', { timeout: 10000 });
```

#### Network Issues
```typescript
// Wait for network stability
await page.waitForLoadState('networkidle');
```

### MCP Server Issues
- Check port 9323 availability
- Verify Node.js version compatibility
- Restart server if connection fails

### Amazon Q Integration Issues
- Ensure extension is installed
- Verify MCP server is running
- Check workspace context inclusion

## Dependencies

### Core Dependencies
```json
{
  "@playwright/test": "^1.x.x",
  "@modelcontextprotocol/sdk": "^1.x.x"
}
```

### Browser Requirements
- Chromium (default)
- Firefox (optional)
- WebKit (optional)

## Performance Considerations

### Test Optimization
- Use `page.waitForLoadState('networkidle')` for stability
- Implement Page Object Model for reusability
- Group related tests in single files
- Use reliable selectors (IDs preferred)

### Resource Management
- 60-second test timeout
- Network idle wait strategy
- Minimal DOM queries
- Efficient selector usage

## Security Notes

### Test Data
- Use placeholder data for sensitive information
- Avoid real credentials in test files
- Implement test data factories

### Network Security
- MCP server runs on localhost
- No external API calls in tests
- Secure test environment isolation