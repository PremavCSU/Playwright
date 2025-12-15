# Playwright + MCP Server + Amazon Q Integration Workflow

## Architecture Overview

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Amazon Q      │───▶│   MCP Client    │───▶│   MCP Server    │───▶│   Playwright    │
│   Developer     │    │   (IDE Plugin)  │    │   (Port 9323)   │    │   Test Runner   │
└─────────────────┘    └─────────────────┘    └─────────────────┘    └─────────────────┘
        │                        │                        │                        │
        ▼                        ▼                        ▼                        ▼
   AI Commands            Protocol Bridge         Tool Execution           Test Results
```

## Integration Flow

### 1. Initialization Phase
```bash
# Terminal 1: Start MCP Server
npm run mcp-server

# Terminal 2: Amazon Q connects automatically
# IDE: Amazon Q extension detects MCP server on port 9323
```

### 2. Communication Protocol

#### Amazon Q → MCP Client
```typescript
// User input in Amazon Q
"Run the search test for electronics"

// Amazon Q processes with context
{
  command: "run_playwright_test",
  context: "@workspace",
  parameters: {
    testFile: "tests/Esearch.spec.ts"
  }
}
```

#### MCP Client → MCP Server
```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "params": {
    "name": "run_playwright_test",
    "arguments": {
      "testFile": "tests/Esearch.spec.ts"
    }
  }
}
```

#### MCP Server → Playwright
```javascript
// mcp-server.js execution
const { exec } = require('child_process');

exec(`npx playwright test ${testFile}`, (error, stdout, stderr) => {
  return {
    content: [{
      type: "text",
      text: stdout || stderr
    }]
  };
});
```

### 3. Response Flow

#### Playwright → MCP Server
```
Running 1 test using 1 worker
✓ tests/Esearch.spec.ts:3:1 › Electronics search (2.1s)
1 passed (3.2s)
```

#### MCP Server → MCP Client
```json
{
  "jsonrpc": "2.0",
  "result": {
    "content": [{
      "type": "text", 
      "text": "✓ Electronics search test passed (2.1s)"
    }]
  }
}
```

#### MCP Client → Amazon Q
```
Test execution completed successfully:
✓ Electronics search test passed (2.1s)
```

## Workflow Examples

### Example 1: Run Specific Test
```
User: "Run the cart test"
Amazon Q: Identifies tests/cart.spec.ts
MCP Server: Executes npx playwright test tests/cart.spec.ts
Result: Test results displayed in Amazon Q
```

### Example 2: Generate New Test
```
User: "Create a test for product comparison"
Amazon Q: Generates test code using @workspace context
MCP Server: Validates test structure
Playwright: Executes generated test
Result: New test file created and executed
```

### Example 3: Debug Test Failure
```
User: "Debug the failing navigation test"
Amazon Q: Analyzes test file and error logs
MCP Server: Runs test in debug mode
Playwright: Provides detailed failure information
Result: Debugging suggestions from Amazon Q
```

## Key Integration Points

### 1. Context Sharing
```typescript
// Amazon Q uses workspace context
@workspace → Full project awareness
@file → Specific test file context  
@folder → Directory-level context
```

### 2. Tool Execution
```javascript
// MCP Server tool registry
tools: [{
  name: "run_playwright_test",
  description: "Execute Playwright tests",
  inputSchema: { /* validation */ }
}]
```

### 3. Result Processing
```javascript
// Structured response format
{
  success: boolean,
  output: string,
  duration: number,
  testResults: {
    passed: number,
    failed: number,
    skipped: number
  }
}
```

## Configuration Requirements

### MCP Server Setup
```javascript
// mcp-server.js
const server = new Server({
  name: "playwright-test-server",
  version: "1.0.0"
});

// Port configuration
const PORT = process.env.MCP_PORT || 9323;
```

### Amazon Q Configuration
```json
// IDE settings
{
  "amazonq.mcp.servers": [{
    "name": "playwright-server",
    "command": "node",
    "args": ["mcp-server.js"],
    "cwd": "./Playwright"
  }]
}
```

### Playwright Configuration
```typescript
// playwright.config.ts
export default {
  timeout: 60000,
  use: {
    baseURL: 'https://amazon.com',
    headless: true
  }
};
```

## Error Handling Flow

### Connection Errors
```
Amazon Q → MCP Client: Connection timeout
MCP Client → User: "MCP server not responding"
Solution: Restart MCP server (npm run mcp-server)
```

### Test Execution Errors
```
Playwright → MCP Server: Test failure with stack trace
MCP Server → Amazon Q: Formatted error message
Amazon Q → User: Debugging suggestions and fixes
```

### Port Conflicts
```
MCP Server → System: Port 9323 in use
System → MCP Server: EADDRINUSE error
Solution: Kill conflicting process or use different port
```

## Performance Optimization

### Connection Pooling
- MCP server maintains persistent connections
- Reduces handshake overhead
- Enables faster test execution

### Caching Strategy
```javascript
// Test result caching
const testCache = new Map();
if (testCache.has(testFile)) {
  return testCache.get(testFile);
}
```

### Parallel Execution
```javascript
// Multiple test execution
Promise.all([
  runTest('tests/search.spec.ts'),
  runTest('tests/cart.spec.ts'),
  runTest('tests/navigation.spec.ts')
]);
```

## Security Considerations

### Local Execution Only
- MCP server binds to localhost
- No external network access
- Sandboxed test environment

### Input Validation
```javascript
function validateTestFile(filePath) {
  if (!filePath.startsWith('tests/')) {
    throw new Error('Invalid test path');
  }
  if (filePath.includes('..')) {
    throw new Error('Path traversal not allowed');
  }
}
```

## Troubleshooting Checklist

1. **MCP Server Running**: Check `npm run mcp-server`
2. **Port Available**: Verify port 9323 is free
3. **Amazon Q Connected**: Check IDE extension status
4. **Playwright Installed**: Verify `npx playwright --version`
5. **Test Files Exist**: Confirm test file paths
6. **Permissions**: Check file system access rights