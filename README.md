# Playwright Test Suite with Amazon Q & MCP Integration

## Overview
Automated testing suite for Amazon.com using Playwright framework, integrated with Amazon Q Developer and Model Context Protocol (MCP) server for enhanced AI-powered testing capabilities.

## Setup
```bash
npm install
```

## Running Tests

### Playwright Tests (TypeScript)
```bash
# Run all tests
npx playwright test

# Run specific test
npx playwright test tests/search.spec.ts

# Run with UI
npx playwright test --ui
```

### Pytest Tests (Python)
```bash
# Install Python dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install

# Run all pytest tests
python -m pytest pytest_tests/ -v

# Run specific test
python -m pytest pytest_tests/test_search.py -v

# Run with HTML report
python -m pytest pytest_tests/ --html=pytest_reports/report.html

# Run using the runner script
python pytest_tests/run_tests.py
python pytest_tests/run_tests.py search
```

## Test Files

### Playwright Tests (TypeScript)
- `search.spec.ts` - Amazon search functionality tests
- `amazon-search.spec.ts` - TV search test
- `optimized-search.spec.ts` - Optimized multi-product search
- `Esearch.spec.ts` - Electronics items search test
- `account.spec.ts` - User account functionality tests
- `cart.spec.ts` - Shopping cart operations
- `deals.spec.ts` - Deals and promotions testing
- `filters.spec.ts` - Product filtering functionality
- `navigation.spec.ts` - Site navigation tests
- `prime.spec.ts` - Amazon Prime features
- `product-details.spec.ts` - Product page testing
- `reviews.spec.ts` - Product reviews functionality
- `sorting.spec.ts` - Product sorting options
- `wishlist.spec.ts` - Wishlist functionality

### Pytest Tests (Python)
- `test_search.py` - Amazon search functionality tests
- `test_amazon_search.py` - TV search test
- `test_optimized_search.py` - Optimized multi-product search
- `test_esearch.py` - Electronics items search test
- `test_account.py` - User account functionality tests
- `test_cart.py` - Shopping cart operations
- `test_deals.py` - Deals and promotions testing
- `test_filters.py` - Product filtering functionality
- `test_navigation.py` - Site navigation tests
- `test_prime.py` - Amazon Prime features
- `test_product_details.py` - Product page testing
- `test_reviews.py` - Product reviews functionality
- `test_sorting.py` - Product sorting options
- `test_wishlist.py` - Wishlist functionality

## MCP Server Integration

### Starting MCP Server
```bash
npm run mcp-server
```

### MCP Server Features
- **Tool**: `run_playwright_test` - Execute Playwright tests via MCP
- **Port**: 9323 (default)
- **Transport**: stdio
- **Integration**: Works with Amazon Q Developer

### Troubleshooting MCP Server
If port 9323 is in use:
```bash
# Find process using port
netstat -ano | findstr :9323

# Kill process (replace PID)
taskkill /PID <PID> /F
```

## Amazon Q Developer Integration

### Features
- AI-powered test generation
- Code optimization suggestions
- Automated debugging assistance
- Test refactoring recommendations

### Usage with Amazon Q
1. Install Amazon Q Developer extension in your IDE
2. Start MCP server: `npm run mcp-server`
3. Use `@workspace` to include project context
4. Ask Amazon Q to generate, optimize, or debug tests

## Configuration
- `playwright.config.ts` - Test configuration
- `mcp-server.js` - MCP server implementation
- Multiple browser support: Chromium, Firefox, WebKit
- Parallel test execution enabled
- HTML reporter with trace collection
- CI/CD optimized settings

## Documentation
Comprehensive documentation available in `/docs` folder:
- `PROJECT_REFERENCE.md` - Complete project structure and file descriptions

## Dependencies
- `@playwright/test` ^1.40.0 - Testing framework
- `@modelcontextprotocol/sdk` ^0.4.0 - MCP integration

## Reports

### Playwright Reports
- HTML reports generated in `playwright-report/`
- Test results and traces in `test-results/`
- View reports: `npx playwright show-report`

### Pytest Reports
- HTML reports generated in `pytest_reports/`
- View reports: Open `pytest_reports/report.html` in browser

## Best Practices
- Use reliable selectors (IDs over roles)
- Add proper waits (`waitForLoadState`)
- Implement Page Object Model for reusability
- Leverage Amazon Q for test optimization