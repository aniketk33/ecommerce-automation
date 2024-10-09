# **Selenium Automation Framework - E-commerce Website**

This project is an automation framework for an e-commerce website using **Selenium** WebDriver with **Python**. The framework follows the **Page Object Model (POM)** architecture and includes:
- Login, Register, Dashboard, Checkout, and Order Confirmation pages.
- Data-driven testing with Excel.
- Test execution using **PyTest**.
- **Allure Reports** for test reporting.
- Logger integration for monitoring actions and errors.
- Screenshots for failure test cases.

---

## **Table of Contents**

- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Setup and Configuration](#setup-and-configuration)
- [How to Run Tests](#how-to-run-tests)
- [Logging](#logging)
- [Reporting with Allure](#reporting-with-allure)
- [Contributing](#contributing)

---

## **Project Overview**

This framework automates key workflows of an e-commerce website, including user registration, login, browsing the dashboard, checking out products, and confirming orders. The automation tests cover end-to-end scenarios using Selenium WebDriver, and PyTest serves as the test execution tool.

---

## **Tech Stack**

- **Python**: Programming language.
- **Selenium WebDriver**: Browser automation tool.
- **PyTest**: Test framework for writing and executing test cases.
- **Excel**: Used for data-driven testing (reading test data).
- **Allure Reports**: For generating test execution reports.
- **Logging**: Python’s `logging` library for capturing logs.

---

## **Project Structure**

```
.
├── tests/
│   ├── test_login.py           # Login test cases
│   ├── test_register.py        # Registration test cases
│   ├── test_dashboard.py       # Dashboard navigation tests
├── pages/
│   ├── login_page.py           # Page Object for Login
│   ├── register_page.py        # Page Object for Registration
│   ├── dashboard_page.py       # Page Object for Dashboard
│   ├── checkout_page.py        # Page Object for Checkout
├── utilities/
│   ├── excel_util.py           # Excel utility for reading test data
│   ├── logger_util.py          # Logger setup for logging actions
│   ├── screenshot_util.py      # Utility for capturing screenshots
├── locators/
│   └── locators.py             # Centralized file for storing element locators
├── reports/                    # Allure reports generated after test execution
├── logs/                       # Log files
├── allure-results/             # Test results for Allure
├── README.md                   # Project documentation
└── requirements.txt            # Required dependencies
```

---

## **Installation**

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/selenium-ecommerce-automation.git
   cd selenium-ecommerce-automation
   ```

2. **Create a virtual environment (optional but recommended)**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Install Allure** (for generating reports):

   - Download Allure binaries from [Allure Installation Guide](https://docs.qameta.io/allure/#_installing_a_commandline).
   - Add the path to Allure binaries to your system’s `PATH`.

---

## **Setup and Configuration**

### **1. Excel Data File**

Place your Excel test data in a file (e.g., `test_data.xlsx`) and specify the correct file path in the **`excel_util.py`** script for reading data.

---

## **How to Run Tests**

1. **Run All Tests**:

   ```bash
   pytest --alluredir=allure-results
   ```

2. **Run Specific Test File**:

   To run only the login test:
   ```bash
   pytest tests/test_login.py --alluredir=allure-results
   ```

3. **Run Tests with Logging**:

   Test logs will automatically be written to the `logs/` folder:
   ```bash
   pytest --alluredir=allure-results
   ```

4. **Execute Only Login Test**:

   ```bash
   pytest tests/test_login.py --alluredir=allure-results
   ```

---

## **Logging**

- Logs are generated using the `logging` module in Python and are saved in the `logs/` directory.
- Each action, such as entering data, clicking buttons, or checking results, is logged to help trace the execution steps.
- Logs will also indicate test failures and exceptions.

---

## **Reporting with Allure**

1. **Generate Allure Reports**:

   After running the tests, generate the report using the following command:

   ```bash
   allure serve allure-results
   ```

2. **View Reports**:

   This will open an HTML report in your default web browser, showing detailed test execution results and failure screenshots.

---
