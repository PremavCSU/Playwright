# Configuration Reference

## Playwright Configuration

### playwright.config.ts
```typescript
import { defineConfig } from '@playwright/test';

export default defineConfig({
  timeout: 60000,
  use: {
    baseURL: 'https://amazon.com',
    headless: true,
    screenshot: 'only-on-failure',
    video: 'retain-on-failure'
  },
  projects: [
    { name: 'chromium', use: { ...devices['Desktop Chrome'] } }
  ],
  reporter: [['html'], ['json']]
});
```

### Key Settings
```typescript
timeout: 60000              // Test timeout (60s)
headless: true              // Run without UI
screenshot: 'only-on-failure' // Capture on fail
video: 'retain-on-failure'  // Record on fail
workers: 1                  // Parallel execution
```

## Package Configuration

### package.json
```json
{
  "scripts": {
    "test": "npx playwright test",
    "test:ui": "npx playwright test --ui",
    "test:headed": "npx playwright test --headed",
    "mcp-server": "node mcp-server.js",
    "report": "npx playwright show-report"
  },
  "dependencies": {
    "@playwright/test": "^1.40.0",
    "@modelcontextprotocol/sdk": "^1.0.0"
  }
}
```

## MCP Server Configuration

### mcp-server.js
```javascript
import { Server } from '@modelcontextprotocol/sdk/server/index.js';

const server = new Server({
  name: "playwright-test-server",
  version: "1.0.0"
});

const PORT = process.env.MCP_PORT || 9323;
```

### Environment Variables
```bash
MCP_PORT=9323
MCP_HOST=localhost
NODE_ENV=development
```

## Amazon Q Configuration

### IDE Settings
```json
{
  "amazonq.mcp.servers": [{
    "name": "playwright-server",
    "command": "node",
    "args": ["mcp-server.js"],
    "cwd": "./Playwright"
  }]
}
```

## Test Configuration Options

### Global Setup
```typescript
// Global timeout
test.setTimeout(120000);

// Test describe configuration
test.describe.configure({ mode: 'serial' });

// Before each test
test.beforeEach(async ({ page }) => {
  await page.goto('https://amazon.com');
});
```

### Reporter Configuration
```typescript
reporter: [
  ['html', { outputFolder: 'playwright-report' }],
  ['json', { outputFile: 'test-results.json' }],
  ['junit', { outputFile: 'results.xml' }]
]
```

## Browser Configuration

### Single Browser
```typescript
use: {
  browserName: 'chromium',
  headless: true,
  viewport: { width: 1280, height: 720 }
}
```

### Multiple Browsers
```typescript
projects: [
  { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
  { name: 'firefox', use: { ...devices['Desktop Firefox'] } },
  { name: 'webkit', use: { ...devices['Desktop Safari'] } }
]
```

## Network Configuration

### Proxy Settings
```typescript
use: {
  proxy: {
    server: 'http://proxy.company.com:8080'
  }
}
```

### Request Interception
```typescript
use: {
  extraHTTPHeaders: {
    'Accept-Language': 'en-US,en;q=0.9'
  }
}
```