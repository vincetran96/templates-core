# What?
Power BI template(s) with star schema modelling

# Content
## Retail.pbix
### Tables
- `dDates`: Dates table
- `dProducts`: Products
- `dPromo_Codes`: Promotion codes
- `fPromo_Discount`: Promotion discount
- `fSales`: Sales
### Measures
- `Average Discount`
    - Key takeaways:
        - `_PromosWithLastCurrentDate`: Filter the `fPromo_Discount` for rows with `Start Date` and `End Date` that contain the `Current Date`
        - `_PromosCrossingDateRange`: Filter the `fPromo_Discount` for rows with `Start Date` and `End Date` that overlap the current Date range "context"
        - From the two filtered tables above, we can calculate the average discount for each of them
