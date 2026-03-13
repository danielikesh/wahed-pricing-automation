# Wahed Pricing Automation (QA Assignment)

Automated UI tests for the Wahed Pricing page using **Playwright + Python + Pytest**.

## Project Overview

This project validates key functionality of the Wahed pricing calculator page:

- Page content verification
- Navigation elements
- Calculator interaction
- Input validation behavior

The automation tests simulate user actions and verify expected results on the pricing calculator.

---

## Tech Stack

- Python
- Playwright
- Pytest
- VS Code

---

## Project Structure

wahed-pricing-automation
│
├── tests
│   ├── test_calculator.py
│   └── test_page_content.py
│
├── requirements.txt
├── README.md

---

## Setup Instructions

### 1 Install dependencies

```bash
pip install -r requirements.txt
Install Playwright browsers
playwright install
Run Tests
pytest --headed
Test Scenarios Covered
Page Validation

Pricing page loads successfully

Navigation bar verification

FAQ section visibility

Calculator Validation

Investment input field present

Accepts numeric input

Handles text input

Notes

The Wahed pricing page dynamically loads calculator components.
Tests handle scrolling and DOM attachment to ensure stable automation execution.

Author

Likesh Barve
QA Automation Assignment


## How Tests Work

The automation uses Playwright with Pytest.

Tests automatically:

- Open the Wahed pricing page
- Verify page content (navigation, pricing header, FAQ section)
- Scroll to the calculator section
- Validate the investment input field
- Verify numeric inputs are accepted
- Verify text inputs behavior

The automation waits for dynamic elements and ensures stable execution.




