from batching import chunk


def test_even_split():
    assert chunk([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]


def test_single_chunk():
    assert chunk(["a", "b", "c"], 3) == [["a", "b", "c"]]
