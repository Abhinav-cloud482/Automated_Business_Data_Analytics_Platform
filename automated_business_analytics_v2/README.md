# Automated Business Data Analytics Platform (Version 2.0)

An enterprise-grade Django SaaS platform combining Automated Data Cleaning, Multi-Dimensional Data Quality Scoring, Isolation Forest Anomaly Detection, Exploratory Data Analysis, Conversational AI Analytics, Executive Summaries, and Professional Report Generation.

## Key Modules
1. **User Authentication & Data Isolation**: Secure multi-tenant user sessions.
2. **Dataset Management**: Drag-and-drop CSV & Excel ingestion with instant profiling.
3. **Automated Data Cleaning Engine**: Mean/Median/Mode imputation, duplicate removal, whitespace normalization.
4. **Data Quality Assessment Engine**: Completeness, Uniqueness, Validity, Consistency, and Accuracy Proxy scoring (0-100 scale).
5. **Intelligent Anomaly Detection**: IQR, Z-Score, and Isolation Forest anomaly isolation.
6. **Exploratory Data Analysis (EDA)**: Descriptive stats, correlation matrices, and automated insights.
7. **AI-Powered Data Analyst**: Natural-language conversational analytics with safe allowlisted execution.
8. **Automated Executive Summaries**: KPI extraction, business trends, and evidence-based recommendations.
9. **Multi-Format Reports**: PDF executive briefs, formatted Excel workbooks, and cleaned CSV exports.

## Local Quick Start
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
