# Test Plan: Swag Labs (SauceDemo) E-Commerce Platform

**Application Under Test (AUT)**: Swag Labs ([https://www.saucedemo.com](https://www.saucedemo.com))  
**Document Version**: 1.0.0  
**Author**: QA / SDET Engineer  
**Date**: August 2026  

---

## 1. Overview & Objectives
This Test Plan outlines the testing strategy, scope, environment, test cases, and risk analysis for the Swag Labs e-commerce platform. The primary goal is to ensure end-to-end functionality, high usability, robust negative/error handling, and cross-browser stability across all core user flows.

---

## 2. Scope of Testing

### 2.1 In-Scope Features
1. **User Authentication & Session Management**:
   - Valid credential login for multiple user roles (`standard_user`, `problem_user`, `performance_glitch_user`, `error_user`, `visual_user`).
   - Locked-out account handling (`locked_out_user`).
   - Empty/invalid field validation and error message rendering.
   - Logout functionality and session invalidation.
2. **Product Catalog & Inventory Browsing**:
   - Inventory item display (title, description, price, product image).
   - Sorting functionality (Name A to Z, Name Z to A, Price Low to High, Price High to Low).
   - Individual product detail page navigation.
3. **Shopping Cart Functionality**:
   - Adding items to cart from the inventory page and product details page.
   - Removing items from cart across different pages.
   - Real-time shopping cart badge counter updates.
   - Persistence of cart state across page navigations.
4. **Checkout Workflow**:
   - Step 1: Customer Information input (First Name, Last Name, Postal Code validation).
   - Step 2: Overview calculation (Item total, Tax calculation, Total amount, item summary).
   - Step 3: Order confirmation / completion screen and resetting cart.

### 2.2 Out-of-Scope Features
- Real payment gateway integrations (the site is a simulated sandbox).
- Multi-currency conversions or international shipping rules.
- Third-party OAuth authentication (Google, Facebook logins).

---

## 3. Types of Testing

| Testing Type | Description & Purpose |
| :--- | :--- |
| **Functional Testing** | Validate that user journeys (Login, Add to Cart, Checkout, Logout) behave according to functional specifications. |
| **UI / Visual Testing** | Verify UI layouts, alignment, image asset loading, responsive display, and button states. |
| **Negative Testing** | Test edge inputs, blank required fields, invalid postal codes, unauthorized route navigation, and locked accounts. |
| **Edge Case Testing** | Browser back/forward button clicks during checkout, double-clicking action buttons, rapid sorting changes. |
| **Cross-Browser Testing** | Ensure consistent behavior across Google Chrome, Mozilla Firefox, and Microsoft Edge. |
| **Performance Testing** | Evaluate application resilience and responsiveness under delayed network responses (`performance_glitch_user`). |

---

## 4. Test Environment & Configurations

### 4.1 Browsers & Platforms
- **Browsers**: Google Chrome (v120+), Mozilla Firefox (v122+), Microsoft Edge (v120+).
- **Operating Systems**: Windows 11 / macOS / Linux.
- **Screen Resolutions**: Desktop (1920x1080, 1366x768), Tablet viewport (768x1024), Mobile viewport (375x812).

### 4.2 Test Data Matrix

| Username | Password | Persona & Expected Behavior |
| :--- | :--- | :--- |
| `standard_user` | `secret_sauce` | Normal, functional happy path user. |
| `locked_out_user` | `secret_sauce` | Blocked user; must display locked-out error banner. |
| `problem_user` | `secret_sauce` | Simulated buggy user persona (broken images, broken inputs, broken buttons). |
| `performance_glitch_user`| `secret_sauce` | User with artificial server latency to test page load timeouts. |
| `error_user` | `secret_sauce` | Triggers client/server errors during checkout interactions. |
| `visual_user` | `secret_sauce` | Layout misalignment and visual distortion test persona. |

---

## 5. Detailed Test Cases

### Test Case 1: TC_AUTH_01 — Valid User Authentication
- **Module**: Authentication
- **Priority / Severity**: High / Critical
- **Preconditions**: User is on the login page (`https://www.saucedemo.com`).
- **Test Data**: Username: `standard_user`, Password: `secret_sauce`
- **Steps to Execute**:
  1. Navigate to `https://www.saucedemo.com`.
  2. Enter `standard_user` in the Username input field.
  3. Enter `secret_sauce` in the Password input field.
  4. Click the "Login" button.
- **Expected Result**: User is successfully logged in and redirected to `/inventory.html`. The page header displays "Swag Labs", the inventory container is populated with 6 items, and the shopping cart icon is visible.

---

### Test Case 2: TC_AUTH_02 — Locked-Out User Authentication Prevention
- **Module**: Authentication (Negative)
- **Priority / Severity**: High / Major
- **Preconditions**: User is on the login page.
- **Test Data**: Username: `locked_out_user`, Password: `secret_sauce`
- **Steps to Execute**:
  1. Navigate to `https://www.saucedemo.com`.
  2. Enter `locked_out_user` in the Username field.
  3. Enter `secret_sauce` in the Password field.
  4. Click the "Login" button.
- **Expected Result**: User remains on the login page. A prominent red error container appears with the text: `"Epic sadface: Sorry, this user has been locked out."`. Password and username fields are highlighted with red error icons.

---

### Test Case 3: TC_CART_01 — Add Single & Multiple Items to Cart and Verify Badge Count
- **Module**: Shopping Cart
- **Priority / Severity**: High / Major
- **Preconditions**: User is logged in as `standard_user` on `/inventory.html`.
- **Test Data**: "Sauce Labs Backpack", "Sauce Labs Bike Light"
- **Steps to Execute**:
  1. Locate "Sauce Labs Backpack" and click "Add to cart".
  2. Observe the button state and shopping cart badge.
  3. Locate "Sauce Labs Bike Light" and click "Add to cart".
  4. Click on the Shopping Cart icon at the top right.
- **Expected Result**:
  - The "Add to cart" buttons toggle to "Remove".
  - Shopping cart badge displays `1` after step 1, and updates to `2` after step 3.
  - On `/cart.html`, both items are listed with correct titles, descriptions, and prices ($29.99 and $9.99).

---

### Test Case 4: TC_CHECKOUT_01 — End-to-End Checkout Workflow
- **Module**: Checkout
- **Priority / Severity**: High / Critical
- **Preconditions**: User has at least one item added to the cart and is on `/cart.html`.
- **Test Data**: First Name: `Jane`, Last Name: `Doe`, Postal Code: `90210`
- **Steps to Execute**:
  1. Click the "Checkout" button on `/cart.html`.
  2. On `/checkout-step-one.html`, enter First Name: `Jane`.
  3. Enter Last Name: `Doe`.
  4. Enter Postal Code: `90210`.
  5. Click "Continue".
  6. On `/checkout-step-two.html`, verify Item Total, Tax, and Final Total calculation.
  7. Click "Finish".
- **Expected Result**:
  - Step 1 navigates to Step 2 overview without errors.
  - Tax and Total are mathematically accurate (`Total = Item Total + Tax`).
  - Step 3 displays `/checkout-complete.html` with `"Thank you for your order!"` header.
  - The shopping cart badge is cleared (empty).

---

### Test Case 5: TC_CHECKOUT_02 — Checkout Form Validation on Missing Fields (Negative)
- **Module**: Checkout (Negative)
- **Priority / Severity**: Medium / Major
- **Preconditions**: User has items in cart and is on `/checkout-step-one.html`.
- **Test Data**: First Name: `""` (Empty), Last Name: `Doe`, Postal Code: `90210`
- **Steps to Execute**:
  1. Leave the "First Name" input field blank.
  2. Enter `Doe` in the Last Name field.
  3. Enter `90210` in Postal Code field.
  4. Click the "Continue" button.
- **Expected Result**: The form is not submitted. A validation error message appears stating `"Error: First Name is required"`, and the First Name field is highlighted with an error icon.

---

### Test Case 6: TC_INVENTORY_01 — Product Sorting by Price (Low to High & High to Low)
- **Module**: Product Catalog
- **Priority / Severity**: Medium / Medium
- **Preconditions**: User is logged in on `/inventory.html`.
- **Test Data**: Sorting dropdown options: `Price (low to high)`, `Price (high to low)`
- **Steps to Execute**:
  1. Click the sorting dropdown menu.
  2. Select `"Price (low to high)"`.
  3. Verify the prices of the displayed products from top to bottom.
  4. Select `"Price (high to low)"`.
  5. Verify the prices again.
- **Expected Result**:
  - When sorted Low to High, prices ascend monotonically ($7.99 -> $9.99 -> $15.99 -> $15.99 -> $29.99 -> $49.99).
  - When sorted High to Low, prices descend monotonically ($49.99 -> $29.99 -> ... -> $7.99).

---

## 6. Risk Assessment & Mitigation

| Identified Risk | Likelihood | Impact | Mitigation Strategy |
| :--- | :---: | :---: | :--- |
| **Session & Route Insecurity**: Unauthenticated users directly accessing `/inventory.html` or `/checkout-step-one.html` via direct URL navigation. | Medium | High | Perform negative route security testing; verify session guard redirects back to `/` with error. |
| **Cart State Desync / Concurrency**: Users adding/removing items in multiple browser tabs simultaneously. | Low | Medium | Test tab concurrency and verify local/session storage consistency. |
| **Slow API / Network Latency**: UI freezing or duplicate order placements when clicking "Finish" on high latency. | High | High | Test with `performance_glitch_user`, implement button disabling on click, and test explicit automation wait conditions. |
| **Form Input Sanitization**: Special characters or script tags in customer names causing layout breaking or XSS. | Medium | High | Perform boundary value analysis (BVA) and negative string testing on checkout fields. |

---

## 7. Deliverables & Exit Criteria
- 100% of critical automation test scripts pass consistently in CI/test runs.
- All high-severity bugs documented with clear steps to reproduce and impact ratings.
- Test coverage across all supported user roles and error boundary scenarios.
