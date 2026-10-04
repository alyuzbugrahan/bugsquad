# Items leak between carts

When `add_item()` is called without a cart, it sometimes returns items from earlier calls.
`add_item("pear")` right after `add_item("apple")` returns `['apple', 'pear']` instead of `['pear']`.
