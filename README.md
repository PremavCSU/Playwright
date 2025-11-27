# Playwright Test Suite with Amazon Q & MCP Integration

## Overview
Automated testing suite for Amazon.com using Playwright framework, integrated with Amazon Q Developer and Model Context Protocol (MCP) server for enhanced AI-powered testing capabilities.

## Setup
```bash
npm install
```

## Running Tests
```bash
# Run all tests
npx playwright test

# Run specific test
npx playwright test tests/search.spec.ts

# Run with UI
npx playwright test --ui
```

## Test Files
- `search.spec.ts` - Amazon search functionality tests
- `amazon-search.spec.ts` - TV search test
- `optimized-search.spec.ts` - Optimized multi-product search
- `Esearch.spec.ts` - Electronics items search test

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
- Timeout: 60 seconds per test
- Browser: Chromium (default)

## Dependencies
- `@playwright/test` - Testing framework
- `@modelcontextprotocol/sdk` - MCP integration

## Best Practices
- Use reliable selectors (IDs over roles)
- Add proper waits (`waitForLoadState`)
- Implement Page Object Model for reusability
- Leverage Amazon Q for test optimization