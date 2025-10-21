
# REVIEW_COMMENTS.md

**Comment 1 – Nice improvement**
Great switch to `str.join` after building a transformed list. This avoids quadratic concatenation and reads clearly as “map then reduce.”

**Comment 2 – Small enhancement suggestion**
In `scale_by_parity`, consider validating inputs (e.g., raising `TypeError` if a non-numeric slips in) or documenting that non-integers with a fractional part will still be tripled/doubled based on `n % 2` semantics.

**Comment 3 – Test coverage**
Add a tiny test (doctest or `pytest`) for the empty-sequence case and mixed types (int/float). Example:

```python
assert scale_by_parity([1.0, 2, 3.5]) == [3.0, 4, 10.5]
assert normalize_and_join([]) == ""
```
