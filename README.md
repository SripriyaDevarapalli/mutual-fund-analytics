\# Mutual Fund Analytics Platform



\## Project Overview



The Mutual Fund Analytics Platform is an end-to-end data analytics and business intelligence solution developed to analyze mutual fund performance, investor behavior, portfolio risk, and market trends.



The project integrates data engineering, financial analytics, database management, and interactive dashboarding into a single workflow. It processes mutual fund datasets, calculates advanced risk-adjusted performance metrics, and provides actionable insights through Power BI dashboards.



\---



\## Objectives



\* Build an automated ETL pipeline for mutual fund datasets

\* Clean and validate financial data

\* Design an analytical SQLite database using a star schema

\* Compute performance metrics such as CAGR, Sharpe Ratio, Sortino Ratio, Alpha, Beta, VaR, and CVaR

\* Analyze investor transaction behavior

\* Develop a mutual fund recommendation system

\* Create an interactive Power BI dashboard



\---



\## Technologies Used



\### Programming \& Analytics



\* Python

\* Pandas

\* NumPy

\* SciPy

\* Matplotlib



\### Database



\* SQLite

\* SQLAlchemy



\### Visualization



\* Power BI

\* Jupyter Notebook



\### Version Control



\* Git

\* GitHub



\---



\## Project Architecture



Raw CSV Files

↓

Data Ingestion

↓

Live NAV Fetch (MFAPI)

↓

Data Cleaning \& Validation

↓

Processed CSV Files

↓

SQLite Database

↓

Analytics \& Risk Metrics

↓

Power BI Dashboard



\---



\## Folder Structure



```text

mutual-fund-analytics/

│

├── data/

│   ├── raw/

│   ├── processed/

│

├── scripts/

│   ├── etl\_pipeline.py

│   ├── live\_nav\_fetch.py

│   ├── clean\_nav\_history.py

│   ├── clean\_transactions.py

│   ├── clean\_scheme\_performance.py

│

├── sql/

│   ├── schema.sql

│   ├── queries.sql

│

├── reports/

│   ├── var\_cvar\_report.csv

│   ├── fund\_scorecard.csv

│   ├── alpha\_beta.csv

│

├── Advanced\_Analytics.ipynb

├── Performance\_Analytics.ipynb

├── bluestock\_mf.db

└── README.md

```



\---



\## Database Design



\### Dimension Tables



\* dim\_fund

\* dim\_date



\### Fact Tables



\* fact\_nav

\* fact\_transactions

\* fact\_performance

\* fact\_aum



The database follows a Star Schema architecture optimized for analytical queries and dashboard reporting.



\---



\## Key Analytics Implemented



\### Performance Analytics



\* Daily Returns

\* CAGR (1Y, 3Y, 5Y)

\* Sharpe Ratio

\* Sortino Ratio

\* Alpha

\* Beta

\* Maximum Drawdown



\### Risk Analytics



\* Historical VaR (95%)

\* Conditional VaR (CVaR)

\* Rolling 90-Day Sharpe Ratio

\* Sector HHI Concentration Analysis



\### Investor Analytics



\* Cohort Analysis

\* SIP Continuity Analysis

\* State-wise Investment Analysis

\* Transaction Type Analysis



\### Recommendation Engine



The recommendation system suggests funds based on:



\* Risk Appetite

\* Historical Performance

\* Sharpe Ratio

\* Risk Category



\---



\## Dashboard Pages



\### Page 1 – Industry Overview



\* Total AUM

\* SIP Inflows

\* Folio Count

\* Industry Trends



\### Page 2 – Fund Performance



\* Risk vs Return Analysis

\* NAV Trends

\* Fund Scorecard



\### Page 3 – Investor Analytics



\* Transaction Analysis

\* Investor Demographics

\* State-wise Investments



\### Page 4 – SIP \& Market Trends



\* SIP Growth

\* Category Inflows

\* Market Trends



\---



\## Key Insights



\* Small Cap and Mid Cap funds generated the highest returns.

\* SIP investments remain the dominant investment mode.

\* Risk-adjusted metrics identified several consistently outperforming funds.

\* Equity-oriented categories attracted the highest net inflows.

\* Financial Services and Technology sectors dominate portfolio allocations.



\---



\## How to Run



\### Create Virtual Environment



```bash

python -m venv venv

```



\### Activate Environment



```bash

venv\\Scripts\\activate

```



\### Install Dependencies



```bash

pip install -r requirements.txt

```



\### Run ETL Pipeline



```bash

python scripts\\etl\_pipeline.py

```



\### Launch Jupyter Notebook



```bash

jupyter notebook

```



\---



\## Future Enhancements



\* Streamlit Web Application

\* Monte Carlo Simulation

\* Portfolio Optimization

\* Automated Email Reporting

\* Machine Learning-Based Forecasting



\---



\## Author



Devarapalli Sripriya Reddy



B.Tech CSE



IIIT Kottayam



