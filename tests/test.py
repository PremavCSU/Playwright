from fpdf import FPDF

content = """
Reference Material Package

1. Uploaded File: Playwright-search-code.png
This image contains an example Playwright script that automates performing a product search on Amazon.

2. Playwright Documentation
https://playwright.dev/docs/intro

3. Amazon Q
https://aws.amazon.com/q/

4. Model Context Protocol
https://modelcontextprotocol.io/docs/getting-started/intro

5. Playwright Code Sample
await page.getByRole('searchbox', { name: 'Search Amazon' }).click();
await page.getByRole('searchbox', { name: 'Search Amazon' }).fill('phone');
await page.getByRole('searchbox', { name: 'Search Amazon' }).press('Enter');
await page.getByRole('button', { name: 'Go', exact: true }).click();
await page.getByRole('link', { name: 'Samsung Galaxy A16 5G A' }).click();
"""

pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", size=12)

for line in content.split("\n"):
    pdf.multi_cell(0, 10, line)

pdf_path = "/mnt/data/reference_material.pdf"
pdf.output(pdf_path)

print("PDF generated at:", pdf_path)
