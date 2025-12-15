# Documentation Index

## Complete Reference Material

### 📋 Core Documentation
- **[PROJECT_REFERENCE.md](PROJECT_REFERENCE.md)** - Complete project overview and structure
- **[README.md](../README.md)** - Project setup and basic usage

### 🧪 Testing Documentation  
- **[TESTING_GUIDE.md](TESTING_GUIDE.md)** - Comprehensive testing patterns and strategies
- **[TEST_RESULTS.md](TEST_RESULTS.md)** - Result formats, analysis, and reporting

### 🔧 Technical References
- **[API_REFERENCE.md](API_REFERENCE.md)** - Playwright, MCP, and Amazon Q APIs
- **[CONFIGURATION_REFERENCE.md](CONFIGURATION_REFERENCE.md)** - All configuration settings
- **[INTEGRATION_WORKFLOW.md](INTEGRATION_WORKFLOW.md)** - How components work together

### 🚀 Quick Access
- **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** - Commands, selectors, and patterns cheat sheet
- **[TROUBLESHOOTING_REFERENCE.md](TROUBLESHOOTING_REFERENCE.md)** - Common issues and solutions

### 🔗 MCP Integration
- **[MCP_INTEGRATION.md](MCP_INTEGRATION.md)** - Detailed MCP server setup and usage

## Documentation Usage

### For New Developers
1. Start with [PROJECT_REFERENCE.md](PROJECT_REFERENCE.md)
2. Follow [TESTING_GUIDE.md](TESTING_GUIDE.md) 
3. Use [QUICK_REFERENCE.md](QUICK_REFERENCE.md) for daily work

### For Troubleshooting
1. Check [TROUBLESHOOTING_REFERENCE.md](TROUBLESHOOTING_REFERENCE.md)
2. Review [CONFIGURATION_REFERENCE.md](CONFIGURATION_REFERENCE.md)
3. Consult [API_REFERENCE.md](API_REFERENCE.md)

### For Integration Setup
1. Read [INTEGRATION_WORKFLOW.md](INTEGRATION_WORKFLOW.md)
2. Configure using [MCP_INTEGRATION.md](MCP_INTEGRATION.md)
3. Verify with [TEST_RESULTS.md](TEST_RESULTS.md)

## Test Files Overview

### Search Tests (4)
- `search.spec.ts` - Basic search
- `amazon-search.spec.ts` - TV search  
- `optimized-search.spec.ts` - Multi-product
- `Esearch.spec.ts` - Electronics

### E-commerce Tests (4)
- `cart.spec.ts` - Shopping cart
- `wishlist.spec.ts` - Wishlist
- `product-details.spec.ts` - Product pages
- `reviews.spec.ts` - Reviews

### Navigation Tests (4)  
- `navigation.spec.ts` - Categories
- `filters.spec.ts` - Filters
- `sorting.spec.ts` - Sorting
- `deals.spec.ts` - Deals

### Account Tests (2)
- `account.spec.ts` - Account menu
- `prime.spec.ts` - Prime pages

## Quick Commands

```bash
# Run tests
npx playwright test

# Start MCP server  
npm run mcp-server

# View results
npx playwright show-report

# Debug test
npx playwright test --debug
```

## Support Resources

### Internal Documentation
- All `.md` files in `/docs` folder
- Inline code comments
- Configuration files

### External Resources
- [Playwright Documentation](https://playwright.dev)
- [MCP Protocol Specification](https://modelcontextprotocol.io)
- [Amazon Q Developer Guide](https://docs.aws.amazon.com/amazonq)

## Documentation Maintenance

### Update Frequency
- **Weekly**: Test results and performance metrics
- **Monthly**: Configuration and API references  
- **As needed**: Troubleshooting and integration guides

### Version Control
- All documentation versioned with code
- Changes tracked in git commits
- Major updates documented in changelog