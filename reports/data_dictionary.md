\# Mutual Fund Analytics Project - Data Dictionary



\## Dataset 1: Fund Master



Source: 01\_fund\_master.csv



| Column             | Data Type | Business Definition            |

| ------------------ | --------- | ------------------------------ |

| amfi\_code          | Integer   | Unique AMFI scheme identifier  |

| fund\_house         | Text      | Asset Management Company (AMC) |

| scheme\_name        | Text      | Name of mutual fund scheme     |

| category           | Text      | Broad category (Equity/Debt)   |

| sub\_category       | Text      | SEBI scheme classification     |

| plan               | Text      | Direct or Regular plan         |

| launch\_date        | Date      | Scheme launch date             |

| benchmark          | Text      | Benchmark index                |

| expense\_ratio\_pct  | Float     | Annual expense ratio (%)       |

| exit\_load\_pct      | Float     | Exit load charged (%)          |

| min\_sip\_amount     | Integer   | Minimum SIP investment         |

| min\_lumpsum\_amount | Integer   | Minimum lumpsum investment     |

| fund\_manager       | Text      | Fund manager name              |

| risk\_category      | Text      | Risk level of scheme           |

| sebi\_category\_code | Text      | SEBI classification code       |



\---



\## Dataset 2: NAV History



Source: 02\_nav\_history.csv



| Column    | Data Type | Business Definition  |

| --------- | --------- | -------------------- |

| amfi\_code | Integer   | Scheme identifier    |

| date      | Date      | NAV observation date |

| nav       | Float     | Net Asset Value      |



\---



\## Dataset 3: AUM by Fund House



Source: 03\_aum\_by\_fund\_house.csv



| Column         | Data Type | Business Definition              |

| -------------- | --------- | -------------------------------- |

| date           | Date      | Reporting date                   |

| fund\_house     | Text      | AMC name                         |

| aum\_lakh\_crore | Float     | AUM in lakh crore                |

| aum\_crore      | Integer   | Assets under management in crore |

| num\_schemes    | Integer   | Number of schemes managed        |



\---



\## Dataset 4: Monthly SIP Inflows



Source: 04\_monthly\_sip\_inflows.csv



| Column                    | Data Type | Business Definition              |

| ------------------------- | --------- | -------------------------------- |

| month                     | Date      | Reporting month                  |

| sip\_inflow\_crore          | Integer   | Monthly SIP inflows              |

| active\_sip\_accounts\_crore | Float     | Active SIP accounts              |

| new\_sip\_accounts\_lakh     | Float     | New SIP registrations            |

| sip\_aum\_lakh\_crore        | Float     | SIP assets under management      |

| yoy\_growth\_pct            | Float     | Year-over-year growth percentage |



\---



\## Dataset 5: Category Inflows



Source: 05\_category\_inflows.csv



| Column           | Data Type | Business Definition  |

| ---------------- | --------- | -------------------- |

| month            | Date      | Reporting month      |

| category         | Text      | Mutual fund category |

| net\_inflow\_crore | Float     | Net inflow amount    |



\---



\## Dataset 6: Industry Folio Count



Source: 06\_industry\_folio\_count.csv



| Column              | Data Type | Business Definition   |

| ------------------- | --------- | --------------------- |

| month               | Date      | Reporting month       |

| total\_folios\_crore  | Float     | Total investor folios |

| equity\_folios\_crore | Float     | Equity fund folios    |

| debt\_folios\_crore   | Float     | Debt fund folios      |

| hybrid\_folios\_crore | Float     | Hybrid fund folios    |

| others\_folios\_crore | Float     | Other category folios |



\---



\## Dataset 7: Scheme Performance



Source: 07\_scheme\_performance.csv



| Column             | Data Type | Business Definition              |

| ------------------ | --------- | -------------------------------- |

| amfi\_code          | Integer   | Scheme identifier                |

| scheme\_name        | Text      | Scheme name                      |

| fund\_house         | Text      | AMC name                         |

| category           | Text      | Scheme category                  |

| plan               | Text      | Direct/Regular plan              |

| return\_1yr\_pct     | Float     | One-year return                  |

| return\_3yr\_pct     | Float     | Three-year return                |

| return\_5yr\_pct     | Float     | Five-year return                 |

| benchmark\_3yr\_pct  | Float     | Benchmark return                 |

| alpha              | Float     | Excess return over benchmark     |

| beta               | Float     | Volatility relative to benchmark |

| sharpe\_ratio       | Float     | Risk-adjusted return metric      |

| sortino\_ratio      | Float     | Downside-risk adjusted return    |

| std\_dev\_ann\_pct    | Float     | Annualized volatility            |

| max\_drawdown\_pct   | Float     | Maximum decline from peak        |

| aum\_crore          | Integer   | Scheme AUM                       |

| expense\_ratio\_pct  | Float     | Expense ratio                    |

| morningstar\_rating | Integer   | Morningstar rating               |

| risk\_grade         | Text      | Risk classification              |



\---



\## Dataset 8: Investor Transactions



Source: 08\_investor\_transactions.csv



| Column             | Data Type | Business Definition        |

| ------------------ | --------- | -------------------------- |

| investor\_id        | Text      | Unique investor identifier |

| transaction\_date   | Date      | Transaction date           |

| amfi\_code          | Integer   | Scheme identifier          |

| transaction\_type   | Text      | SIP/Lumpsum/Redemption     |

| amount\_inr         | Integer   | Transaction amount         |

| state              | Text      | Investor state             |

| city               | Text      | Investor city              |

| city\_tier          | Text      | Tier classification        |

| age\_group          | Text      | Investor age bracket       |

| gender             | Text      | Investor gender            |

| annual\_income\_lakh | Float     | Annual income              |

| payment\_mode       | Text      | Payment method             |

| kyc\_status         | Text      | KYC verification status    |



\---



\## Dataset 9: Portfolio Holdings



Source: 09\_portfolio\_holdings.csv



| Column            | Data Type | Business Definition       |

| ----------------- | --------- | ------------------------- |

| amfi\_code         | Integer   | Scheme identifier         |

| stock\_symbol      | Text      | NSE/BSE stock symbol      |

| stock\_name        | Text      | Company name              |

| sector            | Text      | Industry sector           |

| weight\_pct        | Float     | Portfolio weight          |

| market\_value\_cr   | Float     | Market value in crore     |

| current\_price\_inr | Float     | Current stock price       |

| portfolio\_date    | Date      | Portfolio disclosure date |



\---



\## Dataset 10: Benchmark Indices



Source: 10\_benchmark\_indices.csv



| Column      | Data Type | Business Definition  |

| ----------- | --------- | -------------------- |

| date        | Date      | Trading date         |

| index\_name  | Text      | Benchmark index name |

| close\_value | Float     | Closing index value  |



\---



\# Data Quality Summary



\* Total Datasets: 10

\* Total Schemes: 40

\* Total NAV Records: 46,000

\* Total Investor Transactions: 32,778

\* Duplicate Records Found: 0

\* Missing Values: Only 12 values in yoy\_growth\_pct

\* AMFI Validation Status: Passed

\* All NAV values validated as positive

\* All transaction amounts validated as positive



\---



\# Database



Database Name: bluestock\_mf.db



Schema Type: Star Schema



Fact Tables:



\* fact\_nav

\* fact\_transactions

\* fact\_performance

\* fact\_aum



Dimension Tables:



\* dim\_fund

\* dim\_date



