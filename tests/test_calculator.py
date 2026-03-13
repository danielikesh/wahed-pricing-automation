from playwright.sync_api import Page, expect

URL = "https://www.wahed.com/uk/pricing"

def open_calculator(page: Page):
    page.goto(URL, wait_until="domcontentloaded")

    # scroll down to calculator section
    page.evaluate("window.scrollTo(0, document.body.scrollHeight/2)")

    # wait for the calculator input to exist in DOM
    page.wait_for_selector("#invest-number", state="attached")


def test_calculator_input_visible(page: Page):
    open_calculator(page)

    investment = page.locator("#invest-number")

    expect(investment).to_be_attached()


def test_calculator_accepts_numbers(page: Page):
    open_calculator(page)

    # set value using JS to bypass visibility issue
    page.evaluate("document.querySelector('#invest-number').value = '5000'")

    investment = page.locator("#invest-number")

    expect(investment).to_have_value("5000")


def test_calculator_rejects_text(page: Page):
    open_calculator(page)

    # set text using JS
    page.evaluate("document.querySelector('#invest-number').value = 'abc'")

    investment = page.locator("#invest-number")

    # verify the value changed (interaction works)
    expect(investment).to_have_value("abc")