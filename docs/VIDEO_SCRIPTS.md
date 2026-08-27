# Loom Video Recording Scripts & Presentation Guide

This guide gives you an exact minute-by-minute outline and talking script for recording your two 5–8 minute Loom demonstration videos.

---

## 🎥 Video 1: Test Plan & Automation Overview (5–8 Minutes)

### Goal:
Present your testing strategy, explain your code architecture, and execute the automated PyTest test suite live.

### Recommended Screen Setup:
- Split screen or VS Code open with the project structure and terminal ready.
- Have `docs/TEST_PLAN.md` open in preview mode.

### Minute-by-Minute Script:

#### 1. Introduction (0:00 – 1:00)
- **What to say**: *"Hi everyone, my name is [Your Name]. In this video, I will walk you through my comprehensive test strategy and the Selenium automation framework I built for the Swag Labs (SauceDemo) e-commerce platform."*
- **Show on screen**: Brief view of the website and project folder in VS Code.

#### 2. Test Plan Walkthrough (1:00 – 2:45)
- **What to say**: *"Let's start with the Test Plan. I structured our testing across the entire customer journey—Authentication, Product Catalog, Cart State, and Checkout flow.*
  *I designed test scenarios covering positive functional flows, negative error validations, edge cases, and cross-browser considerations.*
  *I also performed a risk assessment targeting session persistence, cart state mutations, and high-latency response handling using the different user personas provided by SauceDemo (like `problem_user` and `performance_glitch_user`)."*
- **Show on screen**: Scroll through `docs/TEST_PLAN.md`, highlighting the Scope, Test Data matrix, and Test Cases table.

#### 3. Automation Architecture & Code Structure (2:45 – 4:30)
- **What to say**: *"For automation, I used Python with Selenium WebDriver and PyTest, structured around the industry-standard Page Object Model (POM) pattern.*
  *In the `pages/` directory:*
  - *`base_page.py` encapsulates all explicit wait conditions (`WebDriverWait`) to ensure zero flakiness.*
  - *`login_page.py`, `inventory_page.py`, `cart_page.py`, and `checkout_page.py` decouple UI locators from test logic.*
  *In `tests/conftest.py`, I created a reusable PyTest fixture that initializes and tears down Chrome WebDriver cleanly before and after each test."*
- **Show on screen**: Click into `pages/base_page.py`, `pages/checkout_page.py`, and `tests/test_checkout.py`.

#### 4. Live Test Execution (4:30 – 6:30)
- **What to say**: *"Now, let's run our automated test suite live. We have 3 critical flows automated: valid user login, complete end-to-end checkout, and locked-out user error validation."*
- **Action**: Open terminal and run:
  ```bash
  pytest -v --tb=short
  ```
- **What to say while it runs**: *"As you can see in the terminal, all 3 tests are executing sequentially. The tests verify element visibility, dynamic cart badge updates, form submissions, and text assertions."*
- **Show on screen**: Point to the terminal output showing `3 passed in X.XXs` with 100% pass rate.

#### 5. Conclusion (6:30 – 7:00)
- **What to say**: *"The framework is clean, modular, easily extensible for CI/CD integration, and adheres strictly to QA best practices. Thank you!"*

---

## 🎥 Video 2: Manual Bug Discovery Demo (5–8 Minutes)

### Goal:
Live screen demonstration of the 5 hard-to-find, distinct bugs found during manual exploratory testing on `https://www.saucedemo.com`.

### Recommended Screen Setup:
- Browser open on `https://www.saucedemo.com`.
- Have `docs/BUG_REPORTS.md` open for reference.

### Minute-by-Minute Script:

#### 1. Introduction (0:00 – 0:45)
- **What to say**: *"Hi, in this second video, I will demonstrate 5 distinct and critical defects I identified on the Swag Labs e-commerce platform through manual exploratory testing, explaining their severity, user impact, and reproduction steps."*

#### 2. Bug 1: Broken Catalog Image Assets (0:45 – 2:00)
- **Action**: Log in as `problem_user` with password `secret_sauce`.
- **Show on screen**: Point out that every product card shows the same picture of a dog.
- **What to say**: *"Bug 1 (SWAG-BUG-001): When logging in with `problem_user`, all product images fail to load their unique images and instead fall back to the same placeholder dog image (`sl-404.jpg`).*
  *Severity: Medium. Impact: It damages user trust, confuses buyers, and leads to accidental wrong purchases."*

#### 3. Bug 2: Checkout Last Name Input Failure (2:00 – 3:30)
- **Action**: Add an item to cart -> Go to cart -> Click Checkout -> Type in First Name -> Click Last Name and type -> Click Continue.
- **Show on screen**: The field fails / throws `"Error: Last Name is required"`.
- **What to say**: *"Bug 2 (SWAG-BUG-002): In Step One of Checkout, the 'Last Name' input field fails to bind state or process input. When the customer clicks Continue, the system throws an unhandled validation error.*
  *Severity: Critical / Blocker. Impact: Complete loss of conversion. No customer experiencing this bug can ever complete an order."*

#### 4. Bug 3: Malfunctioning 'Add to Cart' and Broken 'Remove' Buttons (3:30 – 4:45)
- **Action**: Go back to inventory -> Click "Add to cart" on items like Bolt T-Shirt or Fleece Jacket (showing that it is unresponsive / requires multiple clicks). For an added item, click "Remove" on the inventory page and in `/cart.html` (showing that clicking "Remove" fails to remove the product or decrement the cart count).
- **Show on screen**: The "Add to cart" button failing to respond, and the "Remove" button failing to remove items or update the cart counter.
- **What to say**: *"Bug 3 (SWAG-BUG-003): The cart interaction state has two major flaws with `problem_user`. First, the 'Add to cart' button is unresponsive or fails intermittently on certain products. Second, once an item is added, clicking the 'Remove' button—both on the inventory page and in the cart—fails to remove the item or decrement the badge count.*
  *Severity: High. Impact: Users cannot reliably add items, and are prevented from modifying their cart before checkout, causing severe friction and cart abandonment."*

#### 5. Bug 4: Product Detail Link Navigation Mismatch (4:45 – 6:00)
- **Action**: Click on the title link of "Sauce Labs Fleece Jacket" or "Sauce Labs Onesie".
- **Show on screen**: The opened details page shows a completely different product (e.g. Backpack details).
- **What to say**: *"Bug 4 (SWAG-BUG-004): Clicking specific product title links navigates to an incorrect product ID parameter, showing the wrong product details and price.*
  *Severity: High. Impact: Misleads customers with incorrect specifications and pricing."*

#### 6. Bug 5: Order Completion Failure on Step Two (6:00 – 7:15)
- **Action**: Demonstrate the Finish button behavior on Checkout Step Two with `error_user` or `problem_user`.
- **Show on screen**: Clicking "Finish" fails to proceed to the order confirmation page.
- **What to say**: *"Bug 5 (SWAG-BUG-005): On the final payment overview step, clicking 'Finish' fails to complete the transaction, leaving the user stranded without confirmation.*
  *Severity: Critical. Impact: Failed order fulfillment and lost revenue."*

#### 7. Conclusion (7:15 – 7:45)
- **What to say**: *"To summarize, these bugs represent critical UX, state management, and business logic flaws. All steps to reproduce, impact assessments, and technical recommendations are detailed in our `BUG_REPORTS.md` document. Thank you!"*
