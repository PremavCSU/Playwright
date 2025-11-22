#!/usr/bin/env node

import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import { CallToolRequestSchema, ListToolsRequestSchema } from '@modelcontextprotocol/sdk/types.js';
import { exec } from 'child_process';

const server = new Server(
  {
    name: 'playwright-mcp-server',
    version: '1.0.0',
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: 'run_playwright_test',
        description: 'Run Playwright tests',
        inputSchema: {
          type: 'object',
          properties: {
            testFile: {
              type: 'string',
              description: 'Test file to run',
            },
          },
        },
      },
    ],
  };
});

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;
  
  if (name === 'run_playwright_test') {
    const testFile = args?.testFile || 'tests/';
    
    return new Promise((resolve) => {
      exec(`npx playwright test ${testFile}`, (error, stdout, stderr) => {
        resolve({
          content: [
            {
              type: 'text',
              text: stdout || stderr || error?.message || 'Test completed',
            },
          ],
        });
      });
    });
  }
  
  throw new Error(`Unknown tool: ${name}`);
});

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

main().catch(console.error);