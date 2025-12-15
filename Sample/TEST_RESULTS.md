# Test Results Documentation

## Result Formats

### Console Output
```
Running 14 tests using 1 worker

✓ tests/search.spec.ts:3:1 › Amazon search (1.2s)
✓ tests/amazon-search.spec.ts:3:1 › Amazon TV search (2.1s)
✓ tests/optimized-search.spec.ts:8:1 › Amazon multi-product search (3.4s)
✓ tests/Esearch.spec.ts:3:1 › Electronics search (1.8s)
✓ tests/cart.spec.ts:3:1 › Add item to cart (2.5s)
✓ tests/navigation.spec.ts:3:1 › Navigate through categories (1.9s)
✓ tests/filters.spec.ts:3:1 › Apply search filters (1.6s)
✓ tests/product-details.spec.ts:3:1 › View product details (2.2s)
✓ tests/wishlist.spec.ts:3:1 › Add to wishlist (2.0s)
✓ tests/sorting.spec.ts:3:1 › Sort search results (1.4s)
✓ tests/reviews.spec.ts:3:1 › View product reviews (2.8s)
✓ tests/account.spec.ts:3:1 › Access account menu (0.9s)
✓ tests/prime.spec.ts:3:1 › Prime membership page (1.3s)
✓ tests/deals.spec.ts:3:1 › Browse deals page (1.7s)

14 passed (28.8s)
```

### JSON Report Format
```json
{
  "config": {
    "timeout": 60000,
    "workers": 1
  },
  "suites": [
    {
      "title": "search.spec.ts",
      "tests": [
        {
          "title": "Amazon search",
          "status": "passed",
          "duration": 1200,
          "errors": []
        }
      ]
    }
  ],
  "stats": {
    "total": 14,
    "passed": 14,
    "failed": 0,
    "skipped": 0,
    "duration": 28800
  }
}
```

### HTML Report Structure
```html
<!DOCTYPE html>
<html>
<head><title>Test Results</title></head>
<body>
  <div class="summary">
    <h1>Test Results: 14 passed, 0 failed</h1>
    <p>Duration: 28.8s</p>
  </div>
  <div class="test-list">
    <!-- Individual test results -->
  </div>
</body>
</html>
```

## Result Analysis

### Success Metrics
```
Total Tests: 14
Passed: 14 (100%)
Failed: 0 (0%)
Skipped: 0 (0%)
Average Duration: 2.06s per test
Total Execution Time: 28.8s
```

### Performance Breakdown
```
Fastest Tests:
- account.spec.ts: 0.9s
- search.spec.ts: 1.2s
- prime.spec.ts: 1.3s

Slowest Tests:
- optimized-search.spec.ts: 3.4s
- reviews.spec.ts: 2.8s
- cart.spec.ts: 2.5s
```

### Test Categories
```
Search Tests (4): All passed
E-commerce Tests (4): All passed  
Navigation Tests (4): All passed
Account Tests (2): All passed
```

## Failure Documentation

### Common Failure Patterns
```typescript
// Timeout failures
Error: Test timeout of 60000ms exceeded
Location: tests/slow-test.spec.ts:10:5

// Element not found
Error: Locator('#missing-element') not found
Location: tests/broken-test.spec.ts:15:3

// Assertion failures  
Error: Expected URL to match /expected/ but got /actual/
Location: tests/navigation.spec.ts:20:8
```

### Failure Analysis Format
```json
{
  "test": "Add item to cart",
  "file": "tests/cart.spec.ts",
  "error": {
    "type": "TimeoutError",
    "message": "Locator('#add-to-cart-button') not found",
    "line": 12,
    "screenshot": "test-results/cart-failure.png"
  },
  "duration": 60000,
  "retry": 0
}
```

## MCP Integration Results

### Tool Execution Response
```json
{
  "tool": "run_playwright_test",
  "status": "success",
  "result": {
    "testsRun": 14,
    "passed": 14,
    "failed": 0,
    "duration": "28.8s",
    "details": [
      {
        "file": "search.spec.ts",
        "status": "passed",
        "duration": "1.2s"
      }
    ]
  }
}
```

### Amazon Q Result Display
```
✅ Test execution completed successfully

Results Summary:
• 14 tests executed
• 14 passed (100%)
• 0 failed
• Total time: 28.8s

Fastest: account.spec.ts (0.9s)
Slowest: optimized-search.spec.ts (3.4s)

All Amazon.com functionality tests are working correctly.
```

## Report Generation

### Command Line Reports
```bash
# Generate HTML report
npx playwright show-report

# Generate JSON report
npx playwright test --reporter=json

# Generate JUnit XML
npx playwright test --reporter=junit
```

### Custom Reporter Configuration
```typescript
// playwright.config.ts
export default {
  reporter: [
    ['html'],
    ['json', { outputFile: 'test-results.json' }],
    ['junit', { outputFile: 'results.xml' }]
  ]
};
```

## CI/CD Integration

### GitHub Actions Output
```yaml
- name: Run Playwright Tests
  run: npx playwright test
  
- name: Upload Results
  uses: actions/upload-artifact@v3
  with:
    name: playwright-report
    path: playwright-report/
```

### Result Artifacts
```
test-results/
├── test-results.json
├── results.xml  
├── playwright-report/
│   ├── index.html
│   └── screenshots/
└── videos/
```

## Monitoring & Alerts

### Performance Thresholds
```typescript
// Performance monitoring
const PERFORMANCE_THRESHOLDS = {
  maxTestDuration: 5000,    // 5 seconds
  maxSuiteDuration: 60000,  // 1 minute
  minPassRate: 95           // 95% pass rate
};
```

### Alert Conditions
```
- Test duration > 5s
- Suite duration > 60s  
- Pass rate < 95%
- Any test failures
- Timeout errors
```

## Historical Tracking

### Trend Analysis
```json
{
  "date": "2024-01-15",
  "stats": {
    "total": 14,
    "passed": 14,
    "duration": 28.8,
    "passRate": 100
  }
}
```

### Performance Trends
```
Week 1: Avg 2.1s per test
Week 2: Avg 2.0s per test  
Week 3: Avg 2.06s per test
Trend: Stable performance
```