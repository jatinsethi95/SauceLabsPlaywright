# SauceLabsPlaywright

🧪 SauceDemo Playwright Automation Framework

Technology: Playwright (Python, Synchronous)
Pattern: Page Object Model (POM)
Purpose: Automate the end-to-end checkout flow on the Sauce Labs Demo Store.

📌 Overview

This automation framework is designed to validate the successful checkout process on the SauceDemo website (https://www.saucedemo.com).
It follows a modular Page Object Model, is simple to maintain, and includes test reporting using Allure.

🎯 Test Scenario Covered

The framework automates the primary customer journey:

Login using valid credentials

Select 3 random items from the inventory

Add selected items to the shopping cart

Proceed to checkout

Enter customer information

Complete the order

Verify “THANK YOU FOR YOUR ORDER” message

This ensures the most critical purchase flow is functioning properly.

🧱 Framework Architecture (POM)
1. LoginPage

Handles:

Entering username and password

Clicking login

2. InventoryPage

Handles:

Locating all product items

Selecting 3 random items

Adding items to the cart

Navigating to cart

3. CartPage

Handles:

Reading cart items

Proceeding to checkout

4. CheckoutPage

Handles:

Entering first name, last name, postal code

Finishing order

📦 Additional Resources & Dependencies Required

Below is everything required to run the framework successfully.

✅ Additional Resources & Dependencies (Brief)

Python 3.8+

Install required packages:
pip install -r requirements.txt

Install Playwright browsers:
python -m playwright install

Allure CLI (optional for reporting)

Git (if cloning/pushing the repo)

VS Code / any Python-compatible editor (optional)

saucedemo-tests/
│── pages/
│    ├── login_page.py
│    ├── inventory_page.py
│    ├── cart_page.py
│    ├── checkout_page.py
│── tests/
│    └── test_checkout_flow.py
│── requirements.txt
│── pytest.ini

Each page is separated into its own class, improving readability and maintainability.

