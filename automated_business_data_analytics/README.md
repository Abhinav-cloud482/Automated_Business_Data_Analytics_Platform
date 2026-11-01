# Automated Business Data Analytics Platform

A enterprise-grade Django web application that allows users to upload CSV and Excel datasets, clean data automatically, perform Exploratory Data Analysis (EDA), visualize dynamic charts, and export PDF/Excel reports.

## System Features
- Multi-tenant authentication & dataset privacy
- Drag-and-drop CSV & Excel (.xlsx, .xls) file ingestion
- Data cleaning engine (Missing values, duplicates, IQR/Z-score outlier isolation)
- Automated statistical analysis & rule-based business insights
- Visualizations hub (Plotly / Chart.js integration)
- Export reports to PDF, Excel, and cleaned CSV formats

## Local Setup Instructions

1. Clone repository & create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Setup environment variables:
   ```bash
   cp .env.example .env
   ```

4. Run database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Launch application server:
   ```bash
   python manage.py runserver
   ```
