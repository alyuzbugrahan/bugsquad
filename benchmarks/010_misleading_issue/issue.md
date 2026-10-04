# format_report crashes for large amounts

I think the f-string formatting in `format_report` can't handle numbers above 1000.
`format_report(["1.234,50"])` raises `ValueError`, while small prices work fine.
