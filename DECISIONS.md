
# DECISIONS.md

## Why these refactors?
I adopted **PEP 8** naming (e.g., `normalize_and_join`, `example_numbers`) and added **PEP 257**-style docstrings to every public function and the module. Clear names shorten the mental jump from code to intent, and docstrings make behavior discoverable via `help()`/IDE tooltips. I also added explicit type hints (including a `Number` alias) to raise readability and enable static analysis by tools like `mypy` or Pyright.

The numerical transformation uses a **single list comprehension** with a conditional expression (`A if cond else B`). Compared to constructing and mutating a list in a loop, comprehensions are both concise and fast while remaining readable. For the string logic, I replaced repeated string concatenations with **list-building + a single `str.join`**. This avoids quadratic-time growth from repeated concatenation and expresses the intent (transform then join) more clearly. I parameterized the delimiter to make the function more reusable.

## Comments and examples
I added brief **inline comments** only where they add signal (e.g., explaining the comprehension’s intent). Over-commenting was avoided to keep the code self-documenting. I also included small **doctest-style examples** so the docstrings double as runnable usage checks.
