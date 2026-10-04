# chunk() silently drops items

`chunk([1, 2, 3, 4, 5], 2)` returns `[[1, 2], [3, 4]]` and the `5` is lost.
The expected result is `[[1, 2], [3, 4], [5]]`.
Our nightly export uses this, so some records are never sent.
