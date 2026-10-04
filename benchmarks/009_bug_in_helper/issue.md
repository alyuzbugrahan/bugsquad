# Invoice totals are wrong

`invoice_total([(10.0, 2)])` should be `24.0` (20.0 plus 20% tax), but it returns `20.2`.
An empty invoice also shows `0.2` instead of `0.0`.
