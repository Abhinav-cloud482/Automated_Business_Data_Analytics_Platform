# Automated_Business_Data_Analytics_Platform
The Automated Business Data Analytics Platform is a production-grade Django web application enabling users to upload CSV/Excel files, automatically clean data, perform EDA, generate interactive charts, and export professional PDF/Excel analytical reports securely.

# Automated Business Data Analytics Platform

[![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11-blue.svg)](https://www.python.org/)
[![Django Version](https://img.shields.io/badge/django-4.2-emerald.svg)](https://www.djangoproject.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

An enterprise-ready, production-grade automated data analytics platform built with **Python, Django, Pandas, and Bootstrap 5**. This platform allows non-technical business owners, analysts, and data scientists to upload raw CSV/Excel datasets and instantly run data quality audits, automated cleaning, exploratory data analysis (EDA), dynamic visualizations, and executive PDF/CSV report generation.

---

##  Key Features

###  1. Authentication & Multi-Tenant Data Security
- User registration, login/logout, and profile management.
- Multi-tenant data isolation: users can only view, manage, and process their own datasets.
- CSRF protection, secure password hashing, and session management.

###  2. Flexible Dataset Ingestion
- Upload `.csv`, `.xlsx`, and `.xls` files with drag-and-drop support.
- File size and type validation.
- Automated instant metrics: row/column counts, data type inference, missing value count, memory usage, and duplicate record detection.

###  3. Intelligent Automated Data Cleaning
- **Missing Value Imputation**: Impute numerical values via Mean or Median; impute categorical values using Mode; or drop missing rows.
- **Duplicate Removal**: Detect and strip duplicate rows with full audit logging.
- **Text Normalization**: Automatic whitespace trimming and string standardization.
- **Outlier Handling**: Detect statistical outliers using Interquartile Range (IQR) and Z-score methods.
- **Preserved Lineage**: Never overwrites original files; creates and tracks a separate `cleaned_file` version with before-and-after audit logs.

###  4. Exploratory Data Analysis (EDA) & Insights Engine
- **Numerical Statistics**: Mean, Standard Deviation, Min, Median, Max, Quartiles (Q1/Q3), and Skewness calculations.
- **Categorical Breakdown**: Unique values, frequency counts, and category percentage distributions.
- **Correlation Matrix**: Automated Pearson correlation matrix.
- **Automated Insights**: Rule-based data observations highlighting anomalies, skewed distributions, and high-performing segments.

###  5. Visual Studio & Dynamic Charting
- Interactive visual creation (Bar, Line, Scatter, Pie, Donut, Area).
- Dynamic X/Y axis selection, metric aggregations (Sum, Mean, Count, Min, Max), and custom grouping.
- One-click PNG chart export capability.

###  6. Executive Reporting & Multi-Format Exports
- Generate printable Executive Audit Reports.
- Export cleaned datasets in standard `.csv` format.

---

##  Tech Stack

| Domain | Technology / Library |
| :--- | :--- |
| **Backend Framework** | Django 4.2+, Python 3.10+ |
| **Data Engine** | Pandas, NumPy, OpenPyXL, XlsxWriter |
| **Database** | SQLite (Development) / PostgreSQL (Production) |
| **Frontend UI** | HTML5, CSS3, JavaScript (ES6+), Bootstrap 5, Tailwind CSS |
| **Charting Engine** | Chart.js / Plotly.js |
| **Report Generation** | ReportLab / Native Print PDF Engine |

---

##  Repository Project Structure

```text
automated_business_data_analytics/
├── manage.py
├── requirements.txt
├── .env.example
├── README.md
├── sample_datasets/
│   ├── sales_dataset.csv
│   └── customer_churn.csv
└── business_analytics/
    ├── config/             # Root project configuration & settings
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── accounts/           # User authentication & profile management
    ├── dashboard/          # Analytics workspace dashboard
    ├── datasets/           # File ingestion, file storage, and meta parsing
    ├── data_cleaning/      # Pandas data preprocessing pipeline engine
    ├── analytics/          # EDA statistics & correlation analysis engine
    ├── visualizations/     # Chart configurator and visualization views
    ├── reports/            # Multi-format report export handlers
    └── core/               # Shared HTML base templates and static assets
```

---

##  Quick Start & Local Installation

### Prerequisites
- **Python 3.10+**
- **Git**
- **pip** (Python package installer)

### 1. Clone the Repository
```bash
git clone https://github.com/Abhinav-cloud482/automated-business-data-analytics.git
cd automated-business-data-analytics
```

### 2. Set Up a Virtual Environment
```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory (or copy from `.env.example`):
```bash
cp .env.example .env
```

### 5. Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser (Optional for Admin Access)
```bash
python manage.py createsuperuser
```

### 7. Run Development Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

---

## Running Sample Datasets

The repository includes pre-packaged test datasets located inside `sample_datasets/`:
- `sales_dataset.csv`: Retail performance data containing missing values and numerical metrics.
- `customer_churn.csv`: SaaS customer metrics with missing values, spending outliers, and churn flags.

To test:
1. Log in to your account.
2. Click **Upload Dataset** and select any file from `sample_datasets/`.
3. Preview the data, run **1-Click Auto Clean**, inspect the **EDA Page**, build **Charts**, and **Download Cleaned CSV**.

---

##  Security Practices
- **Input Validation**: All incoming upload files undergo MIME type verification and structure validation.
- **Path Traversal Protection**: Uploaded files are stored using hashed/sanitized paths.
- **SQL Injection & XSS Prevention**: Built using Django ORM parametrized queries and auto-escaped template rendering.

---

##  License
Distributed under the MIT License. 
