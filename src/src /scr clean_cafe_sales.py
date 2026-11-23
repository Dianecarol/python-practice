Summary
Implement the Cafe Sales Cleaning & Exploratory Analysis Pipeline v4 as a reusable Python workflow for cleaning the dirty cafe sales dataset, producing summary tables, and generating visualizations.

Requirements
Read data/dirty_cafe_sales.csv and write the cleaned dataset to data/cleaned_cafe_sales.csv.
Remove exact duplicate rows, trim whitespace, and normalize dirty tokens (ERROR, UNKNOWN, unknown, empty strings, null/NULL, None, and nan/NaN) to missing values.
Parse transaction dates and numeric fields safely. Coerce invalid values and reject non-positive values for Quantity, Price Per Unit, and Total Spent.
Impute unit prices from item names only when the mapping is unambiguous: Cookie ($1.00), Tea ($1.50), Coffee ($2.00), and Salad ($5.00). Do not infer prices from Cake/Juice or Sandwich/Smoothie based on item name alone.
Derive a missing Total Spent from Quantity × Price Per Unit, or derive one missing numeric field from the other two when possible. Track item-based price imputations and numeric derivations in the output.
Standardize Item, Payment Method, and Location categories, using Unknown for missing categories. Add YearMonth, DayOfWeek, DayOfWeekNum, and IsWeekend calendar fields.
Drop rows that remain incomplete in the critical numeric fields Quantity, Price Per Unit, or Total Spent.
Export 12 summary CSVs under outputs/:
summary_missingness.csv
summary_numeric_stats.csv
summary_by_item.csv
summary_by_payment.csv
summary_by_location.csv
summary_by_month.csv
summary_by_weekday_weekend.csv
summary_by_day_of_week.csv
summary_weekday_weekend_by_item.csv
summary_weekday_weekend_by_payment.csv
summary_weekday_weekend_by_location.csv
summary_payment_by_location_revenue.csv
Generate six charts under outputs/charts/: missingness comparison, revenue by item, monthly revenue trend, channel and payment revenue, weekday versus weekend sales, and weekday/weekend revenue by location.
Acceptance criteria
Running the pipeline from the project root creates the cleaned dataset, all 12 summary CSVs, and all 6 PNG charts at the specified paths.
Shared-price products are not imputed from their item names.
Invalid or non-positive numeric values do not survive as valid transaction quantities, prices, or totals.
Summary metrics and charts are generated from the cleaned dataset, with date-based summaries restricted to rows with valid transaction dates.
Output directories are created automatically when they do not already exist.
