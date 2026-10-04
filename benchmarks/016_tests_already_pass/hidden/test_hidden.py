from batching import chunk


def test_last_partial_chunk_is_kept():
    assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]


def test_size_larger_than_list():
    assert chunk([1, 2], 5) == [[1, 2]]


def test_empty_list():
    assert chunk([], 3) == []


def test_even_split_still_works():
    assert chunk([1, 2, 3, 4, 5, 6], 3) == [[1, 2, 3], [4, 5, 6]]
