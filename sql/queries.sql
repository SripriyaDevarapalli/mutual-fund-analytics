-- Top 5 funds by AUM
SELECT fund_house, MAX(aum_crore)
FROM 03_aum_by_fund_house_clean
GROUP BY fund_house
ORDER BY MAX(aum_crore) DESC
LIMIT 5;

-- Average NAV by fund
SELECT amfi_code, AVG(nav)
FROM nav_history_clean
GROUP BY amfi_code;

-- Monthly NAV trend
SELECT substr(date,1,7), AVG(nav)
FROM nav_history_clean
GROUP BY substr(date,1,7);

-- SIP YoY Growth
SELECT month, yoy_growth_pct
FROM 04_monthly_sip_inflows_clean;

-- Transactions by state
SELECT state, COUNT(*)
FROM investor_transactions_clean
GROUP BY state
ORDER BY COUNT(*) DESC;

-- Funds with expense ratio < 1%
SELECT scheme_name, expense_ratio_pct
FROM scheme_performance_clean
WHERE expense_ratio_pct < 1;

-- Top performing funds
SELECT scheme_name, return_5yr_pct
FROM scheme_performance_clean
ORDER BY return_5yr_pct DESC
LIMIT 10;

-- Average transaction amount
SELECT AVG(amount_inr)
FROM investor_transactions_clean;

-- Holdings by sector
SELECT sector, COUNT(*)
FROM 09_portfolio_holdings_clean
GROUP BY sector;

-- Risk category distribution
SELECT risk_category, COUNT(*)
FROM 01_fund_master_clean
GROUP BY risk_category;
