
"""Refactored utilities for transforming numbers and strings.
   
This module demonstrates clean, documented, and Pythonic functions,
along with a simple main() showcasing their usage.
"""
from __future__ import annotations
from typing import Iterable, List, Sequence, Union

Number = Union[int, float]


def scale_by_parity(numbers: Iterable[Number]) -> List[Number]:
    """Return a new list where each even number is doubled and each odd number is tripled.

    Parameters
    ----------
    numbers : Iterable[int | float]
        An iterable of numeric values to transform.

    Returns
    -------
    list[int | float]
        A list with even values multiplied by 2 and odd values multiplied by 3.

    Examples
    --------
    >>> scale_by_parity([1, 2, 3, 4])
    [3, 4, 9, 8]
    """
    # Use a single, readable comprehension—branching with a conditional expression.
    return [n * 2 if n % 2 == 0 else n * 3 for n in numbers]


def normalize_and_join(strings: Sequence[str], delimiter: str = " ") -> str:
    """Normalize strings by length and join them into a single string.

    Rules:
    - If a string has length > 5, convert it to UPPERCASE.
    - Otherwise, convert it to lowercase.

    Parameters
    ----------
    strings : Sequence[str]
        The sequence of strings to normalize.
    delimiter : str, optional
        The delimiter used to join the transformed strings, by default a single space.

    Returns
    -------
    str
        A single string formed by joining the transformed values.

    Examples
    --------
    >>> normalize_and_join(["apple", "banana", "kiwi"])
    'apple BANANA kiwi'
    """
    # Build the transformed list with a comprehension and join once (O(n)).
    transformed = [s.upper() if len(s) > 5 else s.lower() for s in strings]
    return delimiter.join(transformed)


def main() -> None:
    """Demonstrate the refactored functions with sample data."""
    example_numbers = [1, 2, 3, 4, 5, 6, 7]
    example_strings = ["apple", "banana", "kiwi", "grapefruit", "cherry"]

    processed_numbers = scale_by_parity(example_numbers)
    processed_strings = normalize_and_join(example_strings)

    print("Processed Numbers:", processed_numbers)
    print("Processed Strings:", processed_strings)


if __name__ == "__main__":
    main()
