# Amazon Q Developer Integration Reference

## Overview
Amazon Q Developer is an AI-powered coding assistant integrated with this Playwright test suite to provide intelligent test generation, optimization, and debugging capabilities through Model Context Protocol (MCP) integration.

## Quick Start

### Prerequisites
1. Install Amazon Q Developer extension in your IDE
2. Start MCP server: `npm run mcp-server`
3. Ensure port 9323 is available

### Basic Usage
```
@workspace - Include entire project context
@file tests/search.spec.ts - Include specific test file
@folder tests/ - Include all test files
```

## Core Features

### 1. AI-Powered Test Generation
Generate new test cases using natural language:

**Example Prompts:**
- "Generate a test for Amazon product filtering by price range"
- "Create a test that validates shopping cart functionality"
- "Write a test for Amazon Prime membership verification"

**Generated Output:**
```typescript
test('Filter products by price range', async ({ page }) => {
  await page.goto('https://amazon.com');
  await page.locator('#twotabsearchtextbox').fill('laptops');
  await page.locator('#twotabsearchtextbox').press('Enter');
  await page.waitForLoadState('networkidle');
  
  // Apply price filter
  await page.locator('[data-cy="price-filter"]').click();
  await page.locator('#low-price').fill('500');
  await page.locator('#high-price').fill('1000');
  await page.locator('#price-filter-submit').click();
  
  await expect(page.locator('.s-result-item')).toBeVisible();
});
```

### 2. Code Optimization
Optimize existing tests for better performance and reliability:

**Before:**
```typescript
test('Basic search', async ({ page }) => {
  await page.goto('https://amazon.com');
  await page.click('#twotabsearchtextbox');
  await page.type('#twotabsearchtextbox', 'laptop');
  await page.click('input[type="submit"]');
});
```

**After Amazon Q Optimization:**
```typescript
test('Optimized search', async ({ page }) => {
  await page.goto('https://amazon.com');
  await page.locator('#twotabsearchtextbox').fill('laptop');
  await page.locator('#twotabsearchtextbox').press('Enter');
  await page.waitForLoadState('networkidle');
  await expect(page.locator('[data-component-type="s-search-result"]')).toBeVisible();
});
```

### 3. Automated Debugging
Identify and fix test failures:

**Common Issues Amazon Q Resolves:**
- Selector reliability problems
- Timing and synchronization issues
- Network request handling
- Element visibility problems

### 4. Test Refactoring
Transform repetitive code into reusable functions:

**Amazon Q Suggestion:**
```typescript
// Reusable search function
const performSearch = async (page: Page, searchTerm: string) => {
  await page.locator('#twotabsearchtextbox').fill(searchTerm);
  await page.locator('#twotabsearchtextbox').press('Enter');
  await page.waitForLoadState('networkidle');
};

// Usage in tests
test('Search for electronics', async ({ page }) => {
  await page.goto('https://amazon.com');
  await performSearch(page, 'electronics');
  await expect(page.locator('.s-result-item')).toBeVisible();
});
```

## MCP Integration Details

### Server Configuration
```javascript
// mcp-server.js
const server = new Server({
  name: "playwright-test-server",
  version: "1.0.0"
}, {
  capabilities: {
    tools: {}
  }
});

server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [{
    name: "run_playwright_test",
    description: "Execute Playwright tests",
    inputSchema: {
      type: "object",
      properties: {
        testFile: { type: "string" },
        testName: { type: "string" }
      }
    }
  }]
}));
```

### Available MCP Tools

#### run_playwright_test
Execute specific Playwright tests through Amazon Q:

**Usage:**
```
Amazon Q: "Run the search test using MCP"
```

**Parameters:**
- `testFile`: Path to test file (e.g., "tests/search.spec.ts")
- `testName`: Specific test name (optional)

## Context Annotations

### @workspace
Includes entire project context for comprehensive analysis:
```
@workspace Generate a comprehensive test suite for Amazon checkout process
```

### @file
Includes specific files for targeted assistance:
```
@file tests/cart.spec.ts Optimize this shopping cart test
```

### @folder
Includes directory contents for batch operations:
```
@folder tests/ Review all test files for best practices
```

## Prompt Templates

### Test Generation
```
@workspace Generate a Playwright test for [functionality] that:
- Uses reliable selectors
- Includes proper waits
- Has meaningful assertions
- Follows project patterns
```

### Code Review
```
@file [test-file] Review this test for:
- Selector reliability
- Performance optimization
- Best practices compliance
- Error handling
```

### Debugging
```
@workspace This test is failing: [error message]
Help me identify and fix the issue
```

### Refactoring
```
@folder tests/ Identify common patterns and suggest reusable functions
```

## Best Practices with Amazon Q

### 1. Provide Clear Context
```
// Good
@workspace Generate a test for Amazon product comparison feature that validates price differences

// Better
@workspace @file tests/product-details.spec.ts Generate a test for Amazon product comparison that:
- Compares 2-3 products
- Validates price display
- Checks feature comparison table
- Uses existing project patterns
```

### 2. Specify Requirements
```
Generate a test that:
- Uses Page Object Model
- Includes error handling
- Has 30-second timeout
- Validates specific elements
```

### 3. Request Incremental Improvements
```
@file tests/search.spec.ts Optimize this test by:
- Improving selector reliability
- Adding better waits
- Enhancing assertions
```

## Integration Workflows

### 1. New Feature Testing
```
1. @workspace Analyze existing test patterns
2. Generate new test: "Create test for [feature]"
3. Review and optimize generated code
4. Integrate with existing test suite
```

### 2. Test Maintenance
```
1. @folder tests/ Identify failing tests
2. Debug specific issues with Amazon Q
3. Apply suggested fixes
4. Validate improvements
```

### 3. Code Quality Improvement
```
1. @workspace Review entire test suite
2. Identify optimization opportunities
3. Implement suggested improvements
4. Verify enhanced reliability
```

## Advanced Features

### 1. Pattern Recognition
Amazon Q learns from your existing test patterns:
- Selector preferences (IDs over classes)
- Wait strategies (networkidle vs. specific elements)
- Assertion patterns
- Error handling approaches

### 2. Cross-File Analysis
Analyzes relationships between test files:
- Shared utilities identification
- Common pattern extraction
- Dependency mapping
- Refactoring opportunities

### 3. Performance Optimization
Suggests improvements for:
- Test execution speed
- Resource utilization
- Parallel execution
- CI/CD optimization

## Troubleshooting Amazon Q Integration

### Common Issues

#### MCP Server Connection
```bash
# Check if server is running
netstat -ano | findstr :9323

# Restart server
npm run mcp-server
```

#### Context Loading Issues
```
# Verify file paths in annotations
@file tests/search.spec.ts  # Correct
@file search.spec.ts        # May not work
```

#### Response Quality
```
# Provide more specific context
@workspace @file playwright.config.ts Generate optimized search test using project configuration
```

### Performance Tips

#### Optimize Context Size
```
# Instead of entire workspace
@workspace

# Use specific files
@file tests/search.spec.ts @file playwright.config.ts
```

#### Batch Related Requests
```
# Single comprehensive request
@folder tests/ Review all tests and suggest:
1. Common utility functions
2. Performance improvements
3. Reliability enhancements
```

## Examples and Use Cases

### Example 1: Generate Complete Test Suite
```
@workspace Generate a complete test suite for Amazon wishlist functionality including:
- Add items to wishlist
- Remove items from wishlist
- View wishlist page
- Share wishlist
- Wishlist privacy settings
```

### Example 2: Debug Failing Test
```
@file tests/cart.spec.ts This test fails with "Element not found" error on line 15. 
The selector '#add-to-cart-button' seems unreliable. Help me fix this.
```

### Example 3: Optimize Test Performance
```
@folder tests/ These tests are running slowly. Suggest optimizations for:
- Faster page loads
- More efficient selectors
- Better wait strategies
- Parallel execution improvements
```

## Integration with CI/CD

### GitHub Actions Integration
```yaml
# .github/workflows/tests.yml
- name: Start MCP Server
  run: npm run mcp-server &
  
- name: Run Amazon Q Optimized Tests
  run: npx playwright test --reporter=html
```

### Test Report Enhancement
Amazon Q can analyze test reports and suggest:
- Flaky test identification
- Performance bottlenecks
- Coverage improvements
- Reliability enhancements

## Security Considerations

### Data Privacy
- Amazon Q processes code locally through MCP
- No sensitive test data transmitted
- Secure localhost communication (port 9323)

### Best Practices
- Avoid real credentials in test files
- Use placeholder data for sensitive information
- Review generated code before implementation

## Future Enhancements

### Planned Features
- Visual test generation from screenshots
- Automated test maintenance
- Performance regression detection
- Cross-browser compatibility analysis

### Community Contributions
- Share optimized test patterns
- Contribute to MCP server improvements
- Enhance Amazon Q integration workflows