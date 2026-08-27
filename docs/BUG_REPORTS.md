# Defect & Bug Reports: Swag Labs (SauceDemo)

**Target Application**: Swag Labs ([https://www.saucedemo.com](https://www.saucedemo.com))  
**Document Version**: 1.0.0  
**Status**: Open / Ready for Engineering Review  

---

## Summary of Defects Discovered

| Bug ID | Summary / Title | Severity | Priority | Affected Component |
| :--- | :--- | :--- | :--- | :--- |
| **BUG-01** | Inventory images broken and replaced with dog placeholder image | Medium | High | Catalog / UI |
| **BUG-02** | Checkout Step One "Last Name" input fails to accept value / blocks progression | Blocker / Critical | Critical | Checkout / Forms |
| **BUG-03** | "Remove" button fails to remove items from cart or update cart badge | High | High | Cart / State Management |
| **BUG-04** | Inventory item title links redirect to incorrect product details page | High | High | Navigation / Routing |
| **BUG-05** | Checkout Step Two "Finish" button fails to complete transaction | Blocker / Critical | Critical | Checkout / Orders |

---

## Detailed Bug Reports

### BUG-01: Product Catalog Images Fallback to Generic Dog Image
- **Bug ID**: `SWAG-BUG-001`
- **Severity**: **Medium** (UI / Visual Integrity)
- **Priority**: **High**
- **Affected URL**: `https://www.saucedemo.com/inventory.html`
- **User Role**: `problem_user` / `secret_sauce`
- **Preconditions**: User is logged in with `problem_user` credentials.

#### Steps to Reproduce:
1. Navigate to `https://www.saucedemo.com`.
2. Login using `username: problem_user` and `password: secret_sauce`.
3. Observe the product catalog grid on `/inventory.html`.

#### Expected Result:
Each product card should display its respective distinct product photo (e.g., Sauce Labs Backpack, Bike Light, Bolt T-Shirt, Fleece Jacket, Onesie, Red T-Shirt).

#### Actual Result:
Every product card across the entire catalog renders the exact same image asset (`/static/media/sl-404.168b3351.jpg` - picture of a dog wearing sunglasses), ignoring the distinct product image URLs.

#### Business Impact:
Users cannot visually verify the items they intend to purchase. This destroys buyer trust and increases product return rates.

---

### BUG-02: Checkout Step One "Last Name" Input Fails to Register Value
- **Bug ID**: `SWAG-BUG-002`
- **Severity**: **Critical / Blocker** (Core Business Flow Failure)
- **Priority**: **Critical (P0)**
- **Affected URL**: `https://www.saucedemo.com/checkout-step-one.html`
- **User Role**: `problem_user` / `secret_sauce`
- **Preconditions**: User is logged in as `problem_user` and has added at least one item to the cart.

#### Steps to Reproduce:
1. Login as `problem_user` and add "Sauce Labs Backpack" to the cart.
2. Click the cart icon and click the **"Checkout"** button.
3. On `/checkout-step-one.html`, enter a valid "First Name" (e.g., `John`).
4. Click on the **"Last Name"** input field and type `Doe`.
5. Enter Postal Code: `90210`.
6. Click the **"Continue"** button.

#### Expected Result:
The "Last Name" field accepts user input seamlessly, validation passes, and the user proceeds to `/checkout-step-two.html`.

#### Actual Result:
The "Last Name" input component fails to update its state / value correctly or throws an unhandled validation error (`"Error: Last Name is required"`), effectively blocking the user from proceeding with the checkout.

#### Business Impact:
100% loss of conversion for affected users. Customers cannot complete their purchase, causing immediate cart abandonment and revenue loss.

---

### BUG-03: "Remove" Button Unresponsive for Selected Items in Cart / Inventory
- **Bug ID**: `SWAG-BUG-003`
- **Severity**: **High** (Functional Breakdown)
- **Priority**: **High**
- **Affected URL**: `https://www.saucedemo.com/inventory.html` and `https://www.saucedemo.com/cart.html`
- **User Role**: `problem_user` / `secret_sauce`
- **Preconditions**: User is logged in as `problem_user`.

#### Steps to Reproduce:
1. Login as `problem_user`.
2. Click "Add to cart" on "Sauce Labs Backpack" and "Sauce Labs Fleece Jacket".
3. Verify the cart badge shows `2`.
4. Click the "Remove" button on "Sauce Labs Fleece Jacket".
5. Navigate to `/cart.html` and click "Remove" again.

#### Expected Result:
The item is removed from the cart list, the button toggles back to "Add to cart", and the shopping cart badge count decrements by 1.

#### Actual Result:
Clicking the "Remove" button on specific items does not trigger the removal event handler. The button remains in the "Remove" state, the cart badge count does not decrement, and the item persists in the cart.

#### Business Impact:
Customers are unable to modify their cart before purchase, forcing them to buy unwanted items or abandon the entire cart.

---

### BUG-04: Product Title Hyperlink Navigates to Incorrect Item Details
- **Bug ID**: `SWAG-BUG-004`
- **Severity**: **High** (Navigation / Routing Defect)
- **Priority**: **High**
- **Affected URL**: `https://www.saucedemo.com/inventory.html`
- **User Role**: `problem_user` / `secret_sauce`
- **Preconditions**: User is logged in as `problem_user`.

#### Steps to Reproduce:
1. Login as `problem_user`.
2. On `/inventory.html`, click on the title link for **"Sauce Labs Fleece Jacket"** (or "Sauce Labs Onesie").
3. Observe the item title, description, and URL query parameter on the opened details page.

#### Expected Result:
User is navigated to `inventory-item.html?id=5` displaying the "Sauce Labs Fleece Jacket" title, description, and price ($49.99).

#### Actual Result:
The link points to the wrong ID parameter (e.g., `inventory-item.html?id=0` or item ID for Backpack). The page opens displaying a completely different product than the one clicked by the user.

#### Business Impact:
Severe usability defect. Misleading product information leads to accidental purchases of incorrect items and customer dissatisfaction.

---

### BUG-05: Checkout Overview "Finish" Button Fails to Complete Order
- **Bug ID**: `SWAG-BUG-005`
- **Severity**: **Critical / Blocker** (Order Fulfillment Failure)
- **Priority**: **Critical (P0)**
- **Affected URL**: `https://www.saucedemo.com/checkout-step-two.html`
- **User Role**: `problem_user` / `error_user`
- **Preconditions**: User is on Step Two of Checkout (`/checkout-step-two.html`).

#### Steps to Reproduce:
1. Login as `error_user` (or `problem_user` when navigating directly to step two).
2. Add an item and navigate through to `/checkout-step-two.html`.
3. Review the order summary and click the **"Finish"** button.

#### Expected Result:
The order is processed successfully, the cart is cleared, and the user is redirected to `/checkout-complete.html` displaying `"Thank you for your order!"`.

#### Actual Result:
Clicking the "Finish" button triggers a client-side JavaScript exception / error alert (`"Cannot complete order"` or button click is ignored). The page does not redirect, and no order confirmation is generated.

#### Business Impact:
Zero orders can be finalized for users encountering this condition, representing a direct financial failure of the core revenue-generating mechanism of the e-commerce store.

---

## Recommendations for Engineering:
1. **Form State Synchronization**: Review React state bindings for controlled inputs in checkout forms.
2. **Dynamic Route Mapping**: Ensure inventory item IDs are dynamically rendered from the database/API rather than hardcoded index mappings.
3. **Cart Reducer Fix**: Ensure cart state dispatch actions handle item removal keys consistently.
