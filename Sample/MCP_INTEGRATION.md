# MCP Integration Documentation

## Overview
Model Context Protocol (MCP) integration enables AI-powered test execution and management through standardized communication protocols.

## Server Configuration

### Port Settings
- Default Port: 9323
- Protocol: stdio
- Transport: TCP/HTTP

### Server Startup
```bash
npm run mcp-server
node mcp-server.js
```

### Environment Variables
```bash
MCP_PORT=9323
MCP_HOST=localhost
```

## Available Tools

### run_playwright_test
Execute Playwright tests via MCP interface.

**Input Schema:**
```json
{
  "type": "object",
  "properties": {
    "testFile": {
      "type": "string",
      "description": "Path to test file"
    },
    "testName": {
      "type": "string", 
      "description": "Specific test name (optional)"
    },
    "options": {
      "type": "object",
      "description": "Test execution options"
    }
  }
}
```

**Usage Examples:**
```javascript
// Run specific test file
{
  "testFile": "tests/search.spec.ts"
}

// Run specific test
{
  "testFile": "tests/cart.spec.ts",
  "testName": "Add item to cart"
}

// Run with options
{
  "testFile": "tests/navigation.spec.ts",
  "options": { "headed": true }
}
```

## Server Implementation

### Basic Structure
```javascript
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';

const server = new Server({
  name: "playwright-test-server",
  version: "1.0.0"
});
```

### Tool Registration
```javascript
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

### Tool Execution
```javascript
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "run_playwright_test") {
    const { testFile, testName, options } = request.params.arguments;
    
    // Execute Playwright test
    const result = await executeTest(testFile, testName, options);
    
    return {
      content: [{
        type: "text",
        text: result.output
      }]
    };
  }
});
```

## Client Integration

### Amazon Q Connection
1. Start MCP server
2. Configure Amazon Q to connect to localhost:9323
3. Use `@workspace` context for project awareness

### Communication Flow
```
Amazon Q → MCP Client → MCP Server → Playwright → Test Results → Amazon Q
```

## Troubleshooting

### Port Conflicts
```bash
# Check port usage
netstat -ano | findstr :9323

# Kill conflicting process
taskkill /PID <PID> /F
```

### Connection Issues
- Verify server is running
- Check firewall settings
- Confirm port accessibility

### Tool Execution Errors
- Validate input schema
- Check test file paths
- Verify Playwright installation

## Security Considerations

### Local Execution
- Server runs on localhost only
- No external network access
- Sandboxed test environment

### Input Validation
```javascript
function validateInput(args) {
  if (!args.testFile || typeof args.testFile !== 'string') {
    throw new Error('Invalid testFile parameter');
  }
  
  if (args.testFile.includes('..')) {
    throw new Error('Path traversal not allowed');
  }
}
```

## Performance Optimization

### Connection Pooling
- Reuse server connections
- Minimize startup overhead
- Cache test results

### Resource Management
- Limit concurrent test execution
- Monitor memory usage
- Clean up temporary files