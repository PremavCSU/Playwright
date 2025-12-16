# Setup Guide

## Prerequisites
- Node.js 16+ 
- Python 3.8+
- Git

## Installation

### 1. Clone and Navigate
```bash
cd c:\Users\Prema\Documents\Playwright
```

### 2. Install Node.js Dependencies
```bash
npm install
```

### 3. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 4. Install Playwright Browsers
```bash
# For TypeScript tests
npx playwright install

# For Python tests
playwright install
```

## Configuration

### Playwright Configuration
The `playwright.config.ts` file includes:
- Test directory: `./tests`
- Parallel execution enabled
- HTML reporter
- Cross-browser support (Chromium, Firefox, WebKit)
- Trace collection on retry

### Pytest Configuration
The `pytest.ini` file includes:
- Test directory: `pytest_tests`
- HTML reporting
- Parallel execution support
- Custom markers for test categorization

### MCP Server Setup
```bash
# Start MCP server
npm run mcp-server
```

## Environment Setup

### IDE Configuration
1. Install Amazon Q Developer extension
2. Configure workspace settings
3. Set up debugging configurations

### Browser Configuration
Browsers are automatically downloaded during installation:
- Chromium (default)
- Firefox
- WebKit (Safari engine)

## Verification

### Test Installation
```bash
# Run sample TypeScript test
npx playwright test tests/search.spec.ts

# Run sample Python test
python -m pytest pytest_tests/test_search.py -v
```

### MCP Server Verification
```bash
# Check if server starts without errors
npm run mcp-server
# Should show: Server listening on stdio
```

## Directory Structure After Setup
```
Playwright/
├── node_modules/           # Node.js dependencies
├── test-results/          # Test execution results
├── playwright-report/     # HTML reports
├── pytest_reports/       # Python test reports
└── .playwright/          # Browser binaries
```

## Troubleshooting

### Common Issues
1. **Port 9323 in use**: Kill existing process or change port in mcp-server.js
2. **Browser installation fails**: Run `npx playwright install --force`
3. **Python module not found**: Ensure virtual environment is activated
4. **Permission errors**: Run terminal as administrator on Windows

### Verification Commands
```bash
# Check Playwright installation
npx playwright --version

# Check Python Playwright
python -c "import playwright; print(playwright.__version__)"

# List installed browsers
npx playwright install --dry-run
```