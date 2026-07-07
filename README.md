# SwagLabs UI Automation Framework 

A professional, industry-grade UI Automation Testing framework built for the **SwagLabs (Saucedemo)** web application.
This framework leverages **Playwright** with **Pytest** using the **Page Object Model (POM)** design pattern,
integrating data-driven testing pipelines and automated HTML reporting with embedded execution state screenshots.

---

## 🛠️ Tech Stack & Tools
* **Language:** Python 3.x
* **Automation Library:** Playwright (Python)
* **Test Runner:** Pytest
* **Design Pattern:** Page Object Model (POM)
* **Data Format:** JSON (Data-Driven Testing)
* **Reporting:** Pytest-HTML with customized Base64 screenshot capturing injection hooks

---

## 📁 Framework Architecture & Folder Structure

Based on the project's codebase tree setup:

```text
📁 SWAGS_LAP_FRAMEWORK/
│
├── 📁 Logs/                  # Stores execution runtime logs (*.log)
├── 📁 Outputs/               # Contains generated SwagLabs_Report.html & embedded assets
│
├── 📁 PageObjects/           # Page Object Model layers (Selectors & Action Methods)
│   ├── 📄 Login_Page.py
│   ├── 📄 Dashbord_page.py
│   └── 📄 Check_Out_Page.py
│
├── 📁 Test_Case/             # Automated test scripts executed via Pytest runner
│   ├── 📄 test_Login.py      # Main Data-Driven automated login suite
│   ├── 📄 test_dashbord.py
│   └── 📄 test_checkout.py
│
├── 📁 Test_Data/             # External JSON payloads for Data-Driven Testing (DDT)
│   └── 📄 test_data.json     # Dynamic test cases (Valid, Invalid, Empty states)
│
├── 📁 Uitilites/             # Reusable core utility wrappers
│   ├── 📄 Custom_Logger.py   # Step-by-step logging utilities
│   ├── 📄 Read_Env.py        # Safe environment configurations (.env) loader
│   └── 📄 ReadJson.py        # Absolute path JSON parser mechanism
│
├── 📄 .env                   # Kept secure local credentials (ignored by git)
├── 📄 .gitignore             # Shields local artifacts from public repository syncing
├── 📄 conftest.py            # Global Pytest fixtures & Base64 failure-screenshot hook
├── 📄 pytest.ini             # Central Pytest execution configurations
└── 📄 requirements.txt       # Framework module dependencies list

#clone
git clone <your-github-repo-url>
cd SWAGS_LAP_FRAMEWORK

# Create a local virtual environment
python -m venv .venv

# Activate the virtual environment
# On Windows:
.venv\Scripts\activate

# Install all framework dependencies
pip install -r requirements.txt

# Install Playwright browser binaries
playwright install

USERNAME=standard_user
PASSWORD=secret_sauce

# Run all automated test suites sequentially
pytest

# Execute specific target test suites directly
pytest Test_Case/test_Login.py
pytest Test_Case/test_dashbord.py
