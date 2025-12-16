# MCP Integration Guide

## Overview
Model Context Protocol (MCP) server enables AI-powered test execution and management through Amazon Q Developer integration.

## MCP Server Architecture

### Server Configuration
```javascript
// mcp-server.js
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';

const server = new Server({
  name: 'playwright-mcp-server',
  version: '1.0.0',
}, {
  capabilities: { tools: {} },
});
```

### Available Tools

#### run_playwright_test
Execute Playwright tests through MCP interface.

**Input Schema:**
```json
{
  "type": "object",
  "properties": {
    "testFile": {
      "type": "string",
      "description": "Test file to run (optional, defaults to 'tests/')"
    }
  }
}
```

**Usage Examples:**
```javascript
// Run all tests
await callTool('run_playwright_test', {});

// Run specific test file
await callTool('run_playwright_test', {
  testFile: 'tests/search.spec.ts'
});

// Run specific test suite
await callTool('run_playwright_test', {
  testFile: 'tests/account.spec.ts'
});
```

## Server Management

### Starting the Server
```bash
# Start MCP server
npm run mcp-server

# Alternative direct execution
node mcp-server.js
```

### Server Status
The server runs on stdio transport and listens for MCP protocol messages.

**Expected Output:**
```
Server listening on stdio
```

### Stopping the Server
- Use `Ctrl+C` to stop the server
- Server automatically closes connections on shutdown

## Integration with Amazon Q

### Setup Process
1. **Install Amazon Q Developer extension** in your IDE
2. **Start MCP server**: `npm run mcp-server`
3. **Configure MCP connection** in Amazon Q settings
4. **Use natural language** to execute tests

### Amazon Q Commands
```
# Natural language test execution
"Run the search tests"
"Execute all Amazon cart tests"
"Test the product details functionality"
"Run tests for the navigation module"

# Specific file execution
"Run tests/search.spec.ts"
"Execute pytest_tests/test_cart.py"
```

### AI-Powered Features
- **Test Generation**: Ask Amazon Q to create new tests
- **Code Optimization**: Get suggestions for test improvements
- **Debugging**: AI-assisted error analysis
- **Refactoring**: Automated test code improvements

## MCP Protocol Details

### Request Format
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "run_playwright_test",
    "arguments": {
      "testFile": "tests/search.spec.ts"
    }
  }
}
```

### Response Format
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "Test execution output..."
      }
    ]
  }
}
```

## Error Handling

### Common Errors
1. **Port in use**: MCP server port 9323 already occupied
2. **Tool not found**: Invalid tool name in request
3. **Execution failure**: Test execution errors

### Error Resolution
```bash
# Check port usage
netstat -ano | findstr :9323

# Kill process using port
taskkill /PID <PID> /F

# Restart server
npm run mcp-server
```

### Error Response Format
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -32000,
    "message": "Tool execution failed",
    "data": {
      "details": "Error details..."
    }
  }
}
```

## Advanced Configuration

### Custom Tool Implementation
```javascript
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;
  
  switch (name) {
    case 'run_playwright_test':
      return await executePlaywrightTest(args);
    case 'custom_tool':
      return await executeCustomTool(args);
    default:
      throw new Error(`Unknown tool: ${name}`);
  }
});
```

### Adding New Tools
```javascript
// Add to tools list
{
  name: 'run_pytest_test',
  description: 'Run Python Playwright tests',
  inputSchema: {
    type: 'object',
    properties: {
      testFile: { type: 'string' },
      markers: { type: 'string' }
    }
  }
}

// Implement handler
case 'run_pytest_test':
  const command = `python -m pytest ${args.testFile} ${args.markers ? `-m ${args.markers}` : ''}`;
  return await executeCommand(command);
```

## Security Considerations

### Input Validation
```javascript
if (name === 'run_playwright_test') {
  const testFile = args?.testFile || 'tests/';
  
  // Validate file path
  if (!testFile.match(/^[a-zA-Z0-9\/\-_.]+$/)) {
    throw new Error('Invalid test file path');
  }
  
  // Prevent directory traversal
  if (testFile.includes('..')) {
    throw new Error('Directory traversal not allowed');
  }
}
```

### Command Injection Prevention
```javascript
// Use parameterized commands
const { spawn } = require('child_process');

const child = spawn('npx', ['playwright', 'test', testFile], {
  stdio: 'pipe'
});
```

## Monitoring and Logging

### Server Logging
```javascript
server.onerror = (error) => {
  console.error('MCP Server Error:', error);
};

// Request logging
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  console.log('Tool called:', request.params.name);
  // ... tool execution
});
```

### Performance Monitoring
```javascript
const startTime = Date.now();
// ... execute test
const duration = Date.now() - startTime;
console.log(`Test execution took ${duration}ms`);
```

## Troubleshooting

### Debug Mode
```javascript
// Enable debug logging
process.env.DEBUG = 'mcp:*';

// Verbose output
console.log('Request received:', JSON.stringify(request, null, 2));
```

### Connection Issues
1. **Check server status**: Ensure server is running
2. **Verify transport**: Confirm stdio transport is working
3. **Test connectivity**: Send simple ping request
4. **Check logs**: Review server and client logs

### Performance Optimization
- **Batch requests**: Group multiple test executions
- **Async execution**: Use non-blocking operations
- **Resource cleanup**: Properly close connections
- **Caching**: Cache test results when appropriate