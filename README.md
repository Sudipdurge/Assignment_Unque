# Swag Labs (SauceDemo) QA & SDET Test Suite

Comprehensive QA Deliverables and Automated Test Framework for [SauceDemo](https://www.saucedemo.com) built using **Python**, **Selenium WebDriver**, and **PyTest** following the **Page Object Model (POM)** pattern.

---

## 📁 Project Structure

```
saucedemo_qa_assignment/
├── docs/
│   ├── TEST_PLAN.md             # Deliverable 1: QA Strategy, Scope, 5+ Detailed Test Cases & Risk Matrix
│   ├── BUG_REPORTS.md           # Deliverable 2: 5 Distinct Hard-to-find Bug Reports with severity & impact
│   ├── VIDEO_SCRIPTS.md         # Deliverable 4: Loom Video recording walkthrough script (Video 1 & 2)
│   └── PART_1_AUDIO_GUIDE.md    # Part 1: Spoken audio response preparation guide (English/Hindi/Telugu)
├── pages/                       # Page Object Model (POM) encapsulation
│   ├── base_page.py             # Reusable wait helpers, element interactions, and browser wrappers
│   ├── login_page.py            # Authentication page interactions and error validation
│   ├── inventory_page.py        # Product catalog, sorting, and cart badge management
│   ├── cart_page.py             # Shopping cart item verification and actions
│   └── checkout_page.py         # Multi-step checkout workflow and order verification
├── tests/                       # Automated Test Suite
│   ├── conftest.py              # WebDriver fixture initialization and teardown
│   ├── test_login.py            # Flow 1 (Valid Login) & Flow 3 (Locked-Out User Error verification)
│   └── test_checkout.py         # Flow 2 (Add item to cart and complete checkout)
├── pytest.ini                   # PyTest configuration and custom markers
├── requirements.txt             # Project dependencies
└── README.md                    # Setup and execution instructions
```

---

## 🛠️ Tech Stack & Prerequisites

- **Language**: Python 3.10+
- **Test Runner**: PyTest
- **Browser Automation**: Selenium WebDriver 4.x
- **Driver Management**: `webdriver-manager` (automatically handles ChromeDriver downloads)
- **Design Pattern**: Page Object Model (POM) with Explicit Waits (`WebDriverWait`)

---

## 🚀 Setup & Installation Instructions

### 1. Clone or Open the Repository
```bash
cd saucedemo_qa_assignment
```

### 2. Create and Activate Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🧪 Running the Automated Tests

### Run All Automated Tests
```bash
pytest -v --tb=short
```

### Run Tests by Category (Markers)
```bash
# Run only authentication tests (Valid login & Locked-out user)
pytest -m auth -v

# Run only checkout workflow tests
pytest -m checkout -v
```

### Run in Headed Mode (Watch the Browser in Real-time)
In `tests/conftest.py`, simply comment out the headless argument:
```python
# chrome_options.add_argument("--headless=new")
```
Then run `pytest -v`.

---

## 📋 Test Coverage Summary

| Test Case | Method | Description |
| :--- | :--- | :--- |
| **Flow 1: Valid Login** | `test_valid_login` | Logs in with `standard_user`, asserts successful redirect to `/inventory.html` and header verification. |
| **Flow 2: Complete Checkout** | `test_add_item_to_cart_and_complete_checkout` | Adds product to cart, verifies badge count, navigates to cart, fills customer details, and validates order completion. |
| **Flow 3: Locked-Out User** | `test_locked_out_user_login` | Attempts login with `locked_out_user`, asserts error container visibility and exact error message match. |

---

## 📄 Key Documentation Links
- 📘 [Test Plan Document](docs/TEST_PLAN.md)
- 🐞 [Bug Reports (5 Discovered Defects)](docs/BUG_REPORTS.md)
- 🎥 [Loom Video Recording Scripts](docs/VIDEO_SCRIPTS.md)
- 🎙️ [Part 1 Audio Interview Guide](docs/PART_1_AUDIO_GUIDE.md)

---

## 📧 Submission Instructions Checklist
1. **GitHub Repository**: Push this directory to your GitHub account (public or unlisted).
2. **Loom Video Links**: Record Video 1 & Video 2 following `docs/VIDEO_SCRIPTS.md` and obtain shareable links.
3. **Part 1 Audio**: Record the 5 audio answers following `docs/PART_1_AUDIO_GUIDE.md`.
4. **Email Recipients**: `krishna@unque.me`, `k.shree@unque.me`
5. **Email Subject**: `Interest: SDET Assignment – [Your Full Name]`
