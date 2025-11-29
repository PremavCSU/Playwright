# Playwright API Reference

## Core APIs

### Page API
```typescript
// Navigation
await page.goto(url, options?)
await page.goBack()
await page.goForward()
await page.reload()

// Content
await page.content()
await page.setContent(html)
await page.title()
await page.url()

// Screenshots
await page.screenshot(options?)
await page.pdf(options?)

// Evaluation
await page.evaluate(pageFunction, arg?)
await page.evaluateHandle(pageFunction, arg?)

// Waiting
await page.waitForLoadState(state?)
await page.waitForURL(url, options?)
await page.waitForSelector(selector, options?)
await page.waitForFunction(pageFunction, arg?, options?)
```

### Locator API
```typescript
// Finding elements
page.locator(selector)
page.getByRole(role, options?)
page.getByText(text, options?)
page.getByLabel(text, options?)
page.getByPlaceholder(text, options?)
page.getByAltText(text, options?)
page.getByTitle(text, options?)
page.getByTestId(testId)

// Actions
await locator.click(options?)
await locator.dblclick(options?)
await locator.fill(value, options?)
await locator.type(text, options?)
await locator.press(key, options?)
await locator.check(options?)
await locator.uncheck(options?)
await locator.selectOption(values, options?)
await locator.hover(options?)
await locator.focus(options?)
await locator.blur()

// Properties
await locator.textContent()
await locator.innerText()
await locator.innerHTML()
await locator.getAttribute(name)
await locator.inputValue()
await locator.isVisible()
await locator.isHidden()
await locator.isEnabled()
await locator.isDisabled()
await locator.isChecked()
```

### Expect API
```typescript
// Page expectations
await expect(page).toHaveTitle(titleOrRegExp)
await expect(page).toHaveURL(urlOrRegExp)

// Locator expectations
await expect(locator).toBeVisible()
await expect(locator).toBeHidden()
await expect(locator).toBeEnabled()
await expect(locator).toBeDisabled()
await expect(locator).toBeChecked()
await expect(locator).toBeFocused()
await expect(locator).toHaveText(expected)
await expect(locator).toContainText(expected)
await expect(locator).toHaveValue(value)
await expect(locator).toHaveAttribute(name, value)
await expect(locator).toHaveClass(expected)
await expect(locator).toHaveCount(count)
```

## Selectors

### CSS Selectors
```typescript
// ID
page.locator('#my-id')

// Class
page.locator('.my-class')

// Attribute
page.locator('[data-testid="submit"]')

// Descendant
page.locator('div .child')

// Child
page.locator('ul > li')

// Pseudo-selectors
page.locator('input:checked')
page.locator('li:first-child')
page.locator('tr:nth-child(2)')
```

### Built-in Selectors
```typescript
// Text content
page.locator('text=Submit')
page.locator('text=/Submit/i')

// Roles
page.getByRole('button', { name: 'Submit' })
page.getByRole('textbox', { name: 'Username' })
page.getByRole('checkbox', { checked: true })

// Labels
page.getByLabel('Username')
page.getByLabel(/password/i)

// Placeholders
page.getByPlaceholder('Enter email')

// Test IDs
page.getByTestId('submit-button')
```

## Configuration Options

### Test Configuration
```typescript
export default defineConfig({
  // Test directory
  testDir: './tests',
  
  // Timeout
  timeout: 30000,
  
  // Expect timeout
  expect: { timeout: 5000 },
  
  // Parallel execution
  fullyParallel: true,
  workers: 4,
  
  // Retries
  retries: 2,
  
  // Reporter
  reporter: [['html'], ['json']],
  
  // Global setup/teardown
  globalSetup: './global-setup.ts',
  globalTeardown: './global-teardown.ts',
  
  // Use options
  use: {
    baseURL: 'http://localhost:3000',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
    headless: true,
    viewport: { width: 1280, height: 720 },
    ignoreHTTPSErrors: true,
    acceptDownloads: true
  }
});
```

### Browser Context Options
```typescript
const context = await browser.newContext({
  viewport: { width: 1280, height: 720 },
  userAgent: 'custom-agent',
  locale: 'en-US',
  timezoneId: 'America/New_York',
  permissions: ['geolocation'],
  geolocation: { latitude: 41.889, longitude: 12.492 },
  colorScheme: 'dark',
  reducedMotion: 'reduce',
  forcedColors: 'active'
});
```

## Advanced Features

### Network Interception
```typescript
// Route handling
await page.route('**/api/**', route => {
  route.fulfill({
    status: 200,
    contentType: 'application/json',
    body: JSON.stringify({ data: 'mocked' })
  });
});

// Request/Response modification
await page.route('**/api/users', async route => {
  const response = await route.fetch();
  const json = await response.json();
  json.modified = true;
  route.fulfill({ response, json });
});
```

### File Operations
```typescript
// File upload
await page.setInputFiles('#file-input', 'path/to/file.pdf');
await page.setInputFiles('#file-input', [
  'file1.pdf',
  'file2.pdf'
]);

// File download
const downloadPromise = page.waitForEvent('download');
await page.click('#download-button');
const download = await downloadPromise;
await download.saveAs('path/to/save/file.pdf');
```

### Authentication
```typescript
// Storage state
await page.context().storageState({ path: 'auth.json' });

// Load storage state
const context = await browser.newContext({
  storageState: 'auth.json'
});

// HTTP authentication
const context = await browser.newContext({
  httpCredentials: {
    username: 'user',
    password: 'pass'
  }
});
```

### Mobile Emulation
```typescript
const iPhone = devices['iPhone 12'];
const context = await browser.newContext({
  ...iPhone
});

// Custom mobile viewport
const context = await browser.newContext({
  viewport: { width: 375, height: 667 },
  userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)',
  isMobile: true,
  hasTouch: true
});
```

## Test Patterns

### Fixtures
```typescript
// Custom fixture
const test = base.extend<{ todoPage: TodoPage }>({
  todoPage: async ({ page }, use) => {
    const todoPage = new TodoPage(page);
    await todoPage.goto();
    await use(todoPage);
  }
});

// Use fixture
test('add todo', async ({ todoPage }) => {
  await todoPage.addTodo('Buy milk');
  await expect(todoPage.todos).toHaveCount(1);
});
```

### Parameterized Tests
```typescript
const browsers = ['chromium', 'firefox', 'webkit'];

browsers.forEach(browserName => {
  test(`test on ${browserName}`, async ({ page }) => {
    // Test implementation
  });
});

// Test data
const testCases = [
  { input: 'test1', expected: 'result1' },
  { input: 'test2', expected: 'result2' }
];

testCases.forEach(({ input, expected }) => {
  test(`test with ${input}`, async ({ page }) => {
    // Test with input and expected
  });
});
```

### Global Setup
```typescript
// global-setup.ts
async function globalSetup() {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  
  // Setup database, start servers, etc.
  await page.goto('/admin/setup');
  await page.fill('#admin-key', process.env.ADMIN_KEY);
  await page.click('#initialize');
  
  await browser.close();
}

export default globalSetup;
```

## Debugging

### Debug Methods
```typescript
// Pause execution
await page.pause();

// Console logging
console.log(await page.title());

// Page console events
page.on('console', msg => console.log(msg.text()));

// Network events
page.on('request', request => 
  console.log(request.method(), request.url())
);

page.on('response', response =>
  console.log(response.status(), response.url())
);
```

### Trace Viewer
```typescript
// Enable tracing
await context.tracing.start({ screenshots: true, snapshots: true });
await page.goto('https://example.com');
await page.click('#button');
await context.tracing.stop({ path: 'trace.zip' });

// View trace
// npx playwright show-trace trace.zip
```

## Error Handling

### Try-Catch Patterns
```typescript
test('handle errors gracefully', async ({ page }) => {
  try {
    await page.goto('/flaky-page');
    await page.waitForSelector('#element', { timeout: 5000 });
  } catch (error) {
    console.log('Element not found, continuing with fallback');
    await page.goto('/fallback-page');
  }
});
```

### Soft Assertions
```typescript
test('soft assertions', async ({ page }) => {
  await expect.soft(page.locator('#element1')).toBeVisible();
  await expect.soft(page.locator('#element2')).toHaveText('Expected');
  
  // Test continues even if soft assertions fail
  await page.click('#continue');
});
```

## Performance

### Performance Metrics
```typescript
test('performance metrics', async ({ page }) => {
  await page.goto('/');
  
  const metrics = await page.evaluate(() => {
    const navigation = performance.getEntriesByType('navigation')[0];
    return {
      domContentLoaded: navigation.domContentLoadedEventEnd - navigation.domContentLoadedEventStart,
      loadComplete: navigation.loadEventEnd - navigation.loadEventStart
    };
  });
  
  expect(metrics.domContentLoaded).toBeLessThan(2000);
});
```

### Resource Monitoring
```typescript
test('monitor resources', async ({ page }) => {
  const responses = [];
  
  page.on('response', response => {
    responses.push({
      url: response.url(),
      status: response.status(),
      size: response.headers()['content-length']
    });
  });
  
  await page.goto('/');
  
  // Analyze responses
  const largeResources = responses.filter(r => 
    parseInt(r.size) > 1000000
  );
  
  expect(largeResources).toHaveLength(0);
});
```