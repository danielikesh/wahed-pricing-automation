from playwright.sync_api import Page, expect

URL = "https://www.wahed.com/uk/pricing"

def test_page_load(page: Page):
    page.goto(URL, wait_until="domcontentloaded")

    # Verify the main heading
    expect(page.get_by_role("heading", name="Pricing")).to_be_visible()


def test_navigation_bar(page: Page):
    page.goto(URL, wait_until="domcontentloaded")

    # Check Pricing link in navigation
    expect(page.get_by_role("link", name="Pricing")).to_be_visible()


def test_faq_section(page: Page):
    page.goto(URL, wait_until="domcontentloaded")

    # Scroll down to FAQ area
    page.mouse.wheel(0, 4000)

    expect(page.get_by_text("Frequently asked questions")).to_be_visible()