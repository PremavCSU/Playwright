# Troubleshooting Reference

## Common Issues & Solutions

### Test Execution Issues

#### Timeout Errors
```
Error: Test timeout of 60000ms exceeded
```
**Solutions:**
```typescript
// Increase test timeout
test.setTimeout(120000);

// Increase action timeout
await page.click('#button', { timeout: 10000 });

// Wait for network stability
await page.waitForLoadState('networkidle');
```

#### Element Not Found
```
Error: Locator('#element') not found
```
**Solutions:**
```typescript
// Add explicit wait
await page.waitForSelector('#element');

// Use expect with timeout
await expect(page.locator('#element')).toBeVisible({ timeout: 5000 });

// Check if element exists
if (await page.locator('#element').isVisible()) {
  await page.locator('#element').click();
}
```

#### Navigation Failures
```
Error: Navigation timeout exceeded
```
**Solutions:**
```typescript
// Retry navigation
for (let i = 0; i < 3; i++) {
  try {
    await page.goto('https://amazon.com');
    break;
  } catch (error) {
    if (i === 2) throw error;
    await page.waitForTimeout(1000);
  }
}
```

### MCP Server Issues

#### Port Already in Use
```
Error: EADDRINUSE: address already in use :::9323
```
**Solutions:**
```bash
# Find process using port
netstat -ano | findstr :9323

# Kill the process
taskkill /PID <PID> /F

# Use different port
MCP_PORT=9324 npm run mcp-server
```

#### Server Connection Failed
```
Error: MCP server not responding
```
**Solutions:**
```bash
# Check if server is running
npm run mcp-server

# Verify port accessibility
telnet localhost 9323

# Restart server
taskkill /F /IM node.exe
npm run mcp-server
```

### Amazon Q Integration Issues

#### Extension Not Connected
**Solutions:**
1. Verify Amazon Q extension is installed
2. Check MCP server is running
3. Restart IDE
4. Reconfigure MCP settings

#### Context Not Loading
**Solutions:**
```
# Use explicit context
@workspace
@file tests/search.spec.ts
@folder tests/

# Clear and reload context
Restart Amazon Q extension
```

### Browser Issues

#### Browser Launch Failed
```
Error: Failed to launch browser
```
**Solutions:**
```bash
# Install browsers
npx playwright install

# Install specific browser
npx playwright install chromium

# Check system dependencies
npx playwright install-deps
```

#### Headless Mode Issues
**Solutions:**
```typescript
// Run in headed mode for debugging
use: { headless: false }

// Enable slow motion
use: { slowMo: 1000 }
```

### Performance Issues

#### Slow Test Execution
**Solutions:**
```typescript
// Optimize waits
await page.waitForLoadState('networkidle');

// Use efficient selectors
page.locator('#id')  // Fast
page.locator('.class')  // Slower

// Reduce timeouts
test.setTimeout(30000);
```

#### Memory Issues
**Solutions:**
```typescript
// Close pages after use
await page.close();

// Limit parallel workers
workers: 1
```

### Selector Issues

#### Selector Not Working
**Solutions:**
```typescript
// Try different selector strategies
'#id'                           // ID (best)
'[data-testid="value"]'         // Data attribute
'text="Button Text"'            // Text content
'.class'                        // Class name

// Debug selector
await page.locator('#element').highlight();
```

#### Dynamic Content
**Solutions:**
```typescript
// Wait for content to load
await page.waitForFunction(() => 
  document.querySelectorAll('.item').length > 0
);

// Use more specific selectors
'[data-component-type="s-search-result"]:first-child'
```

## Debugging Commands

### Test Debugging
```bash
# Debug specific test
npx playwright test search.spec.ts --debug

# Run with trace
npx playwright test --trace on

# Generate trace viewer
npx playwright show-trace trace.zip
```

### Browser Debugging
```typescript
// Pause execution
await page.pause();

// Take screenshot
await page.screenshot({ path: 'debug.png' });

// Console logging
page.on('console', msg => console.log(msg.text()));
```

### Network Debugging
```typescript
// Monitor requests
page.on('request', request => 
  console.log(request.url())
);

// Monitor responses
page.on('response', response => 
  console.log(response.status())
);
```

## Log Analysis

### Common Log Patterns
```
✓ Passed test
✗ Failed test
⚠ Timeout warning
ℹ Info message
```

### Error Log Locations
```
test-results/
├── test-failed-1.png      # Screenshots
├── test-failed-1.webm     # Videos
└── trace.zip              # Execution trace
```

## Recovery Procedures

### Complete Reset
```bash
# Clean installation
rm -rf node_modules
npm install
npx playwright install

# Reset MCP server
taskkill /F /IM node.exe
npm run mcp-server

# Clear browser data
npx playwright test --headed --global-setup=./clear-data.js
```

### Partial Reset
```bash
# Restart MCP server only
npm run mcp-server

# Clear test artifacts
rm -rf test-results/
rm -rf playwright-report/
```