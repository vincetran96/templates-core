# Retail.pbix
## Average Discount

To calculate the amount of discount. Can be used in a table with Dates as rows and one or many Articles are selected.

```
z_Average Discount = 
VAR _Dates = VALUES(dDates[Date])
VAR _MinDate = MINX(_Dates, dDates[Date])
VAR _MaxDate = MAXX(_Dates, dDates[Date])
VAR _NumDates = COUNTROWS(_Dates)
VAR _LastCurrentDate = MAX(dDates[Date])
VAR _PromosWithLastCurrentDate =
    FILTER(
        fPromo_Discount,
        AND(_LastCurrentDate >= fPromo_Discount[Start Date], _LastCurrentDate <= fPromo_Discount[End Date])
    )
VAR _PromosCrossingDateRange =
    FILTER(
        fPromo_Discount,
        NOT(OR(_MaxDate < fPromo_Discount[Start Date], _MinDate > fPromo_Discount[End Date]))
    )
VAR _ResultSingleDay = AVERAGEX(_PromosWithLastCurrentDate, [Discount])
VAR _ResultMultiDay = AVERAGEX(_PromosCrossingDateRange, [Discount])
RETURN
    IF(
        _NumDates > 1,
        _ResultMultiDay,
        IF(
            ISBLANK(_ResultSingleDay),
            0,
            _ResultSingleDay
        )
    )
```

## Days on Promo

To calculate how many days an Article is on promo. Can be used in a table with Week/Month as rows.

```
Days on Promo = 
VAR _Dates = VALUES(dDates[Date])
VAR _MinDate = MINX(_Dates, dDates[Date])
VAR _MaxDate = MAXX(_Dates, dDates[Date])
VAR _NumDates = COUNTROWS(_Dates)

// Filter the discount table for rows overlapping the selected Date range
// Then grab the min start date and max end date
VAR _PromosCrossingDateRange =
    FILTER(
        fPromo_Discount,
        NOT(OR(_MaxDate < fPromo_Discount[Start Date], _MinDate > fPromo_Discount[End Date]))
    )
VAR _MinStartDate = MINX(_PromosCrossingDateRange, fPromo_Discount[Start Date])
VAR _MaxEndDate = MINX(_PromosCrossingDateRange, fPromo_Discount[End Date])

// Find the appropriate promo start date of the selected Date range
//  using max of _MinDate and _MinStartDate
// Same for promo end date, but min of _MaxDate and _MaxEndDate
// If _NumPromoDays is blank, it maybe that there is no promo discount date range
//  that overlaps with the selected Date range, hence we need to check if that var
//  is blank before returning the result
VAR _PromoStartDateOfRange = IF(_MinDate > _MinStartDate, _MinDate, _MinStartDate)
VAR _PromoEndDateOfRange = IF(_MaxDate < _MaxEndDate, _MaxDate, _MaxEndDate)
VAR _NumPromoDays = DATEDIFF(_PromoStartDateOfRange, _PromoEndDateOfRange, DAY)

RETURN
    IF(NOT(ISBLANK(_NumPromoDays)), _NumPromoDays + 1, 0)
```
