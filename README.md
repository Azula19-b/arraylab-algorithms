# ArrayLab Algorithms

ArrayLab Algorithms is a small, beginner-friendly Python command-line app for
practicing common array operations and learning why efficient algorithms matter.
It uses only the Python standard library.

## Run the app

Python 3.8 or newer is recommended.

```bash
python3 main.py
```

Enter numbers separated by spaces, commas, or both. The menu lets you view
statistics, remove duplicates, find every occurrence of a number, rotate the
array, solve Two Sum, review algorithm complexity, or enter a new array.
Invalid menu choices and invalid numeric input are handled without crashing.

## Algorithms and Big-O

| Algorithm | Approach | Time | Extra space |
| --- | --- | --- | --- |
| Statistics | One pass tracks min, max, and sum | O(n) | O(1) |
| Remove duplicates | A set tracks values already seen | O(n) average | O(n) |
| Search | One pass collects matching indices | O(n) | O(k), for k matches |
| Rotate right | List slicing builds a rotated copy | O(n) | O(n) |
| Two Sum | A dictionary maps seen values to indices | O(n) average | O(n) |

The set and dictionary operations are O(1) on average. The algorithms avoid
unnecessary nested loops, and Two Sum never checks every possible pair.

## Run the tests

```bash
python3 -m unittest test_array_utils.py -v
```

The test suite covers normal inputs and edge cases such as empty arrays,
duplicates, missing values, large and negative rotations, and invalid input.
