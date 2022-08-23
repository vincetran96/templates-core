# Retail.pbix
Average Discount
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