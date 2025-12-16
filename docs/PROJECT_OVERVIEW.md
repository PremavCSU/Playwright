# Playwright Test Suite - Project Overview

## Project Description
Automated testing suite for Amazon.com using Playwright framework with dual language support (TypeScript and Python), integrated with Amazon Q Developer and Model Context Protocol (MCP) server for AI-powered testing capabilities.

## Architecture

### Core Components
- **Playwright Tests (TypeScript)**: Primary test suite using Playwright's native TypeScript API
- **Pytest Tests (Python)**: Alternative Python implementation using Playwright's Python bindings
- **MCP Server**: Model Context Protocol server for AI integration
- **Amazon Q Integration**: AI-powered test generation and optimization

### Technology Stack
- **Testing Framework**: Playwright v1.40.0
- **Languages**: TypeScript, Python
- **Test Runners**: Playwright Test, Pytest
- **AI Integration**: Amazon Q Developer, MCP SDK v0.4.0
- **Browsers**: Chromium, Firefox, WebKit

## Project Structure
```
Playwright/
├── tests/                    # TypeScript test files
├── pytest_tests/           # Python test files
├── docs/                   # Documentation
├── Sample/                 # Sample documentation
├── playwright-report/      # Test reports
├── .amazonq/              # Amazon Q configuration
├── mcp-server.js          # MCP server implementation
├── playwright.config.ts   # Playwright configuration
├── pytest.ini            # Pytest configuration
├── package.json           # Node.js dependencies
└── requirements.txt       # Python dependencies
```

## Key Features

### Testing Capabilities
- Cross-browser testing (Chromium, Firefox, WebKit)
- Parallel test execution
- Visual regression testing
- Mobile viewport testing
- Network interception
- Screenshot and video recording

### AI Integration
- Automated test generation via Amazon Q
- Code optimization suggestions
- Intelligent debugging assistance
- Test refactoring recommendations

### Reporting
- HTML reports with interactive traces
- Screenshot capture on failures
- Video recording of test runs
- CI/CD integration ready

## Test Coverage Areas
- Search functionality
- User account operations
- Shopping cart management
- Product details and reviews
- Navigation and filtering
- Amazon Prime features
- Deals and promotions
- Wishlist functionality

## Getting Started
1. Install dependencies: `npm install` and `pip install -r requirements.txt`
2. Install browsers: `playwright install`
3. Run tests: `npx playwright test` or `python -m pytest pytest_tests/`
4. Start MCP server: `npm run mcp-server`
5. View reports: `npx playwright show-report`

## Documentation Index
- [Setup Guide](SETUP_GUIDE.md)
- [Testing Guide](TESTING_GUIDE.md)
- [API Reference](API_REFERENCE.md)
- [MCP Integration](MCP_INTEGRATION.md)
- [Amazon Q Integration](AMAZON_Q_INTEGRATION.md)
- [Configuration Reference](CONFIGURATION_REFERENCE.md)
- [Troubleshooting](TROUBLESHOOTING.md)