"""Efficient, beginner-friendly array algorithms."""

from typing import Dict, List, Optional, Tuple, Union


Number = Union[int, float]


# Time Complexity: O(n) | Space Complexity: O(1)
def array_statistics(numbers: List[Number]) -> Dict[str, Number]:
    """Return the minimum, maximum, sum, and average of a non-empty array."""
    if not numbers:
        raise ValueError("Statistics require at least one number.")

    minimum = numbers[0]
    maximum = numbers[0]
    total: Number = 0

    for number in numbers:
        if number < minimum:
            minimum = number
        if number > maximum:
            maximum = number
        total += number

    return {
        "min": minimum,
        "max": maximum,
        "sum": total,
        "average": total / len(numbers),
    }


# Time Complexity: O(n) average | Space Complexity: O(n)
def remove_duplicates(numbers: List[Number]) -> List[Number]:
    """Remove duplicate values while keeping their first-seen order."""
    seen = set()
    unique = []

    for number in numbers:
        if number not in seen:
            seen.add(number)
            unique.append(number)

    return unique


# Time Complexity: O(n) | Space Complexity: O(k), where k is the matches
def find_all_indices(numbers: List[Number], target: Number) -> List[int]:
    """Return every index at which target appears."""
    return [index for index, number in enumerate(numbers) if number == target]


# Time Complexity: O(n) | Space Complexity: O(n)
def rotate_right(numbers: List[Number], k: int) -> List[Number]:
    """Return a new array rotated right by k positions."""
    if not numbers:
        return []

    shift = k % len(numbers)
    if shift == 0:
        return numbers.copy()
    return numbers[-shift:] + numbers[:-shift]


# Time Complexity: O(n) average | Space Complexity: O(n)
def two_sum(numbers: List[Number], target: Number) -> Optional[Tuple[int, int]]:
    """Return indices of the first pair found whose values add to target."""
    seen: Dict[Number, int] = {}

    for index, number in enumerate(numbers):
        complement = target - number
        if complement in seen:
            return seen[complement], index
        seen[number] = index

    return None


# Time Complexity: O(n) | Space Complexity: O(n)
def parse_array(text: str) -> List[Number]:
    """Parse comma- or whitespace-separated integers and decimal numbers."""
    cleaned = text.replace(",", " ")
    parts = cleaned.split()
    if not parts:
        return []

    numbers: List[Number] = []
    for part in parts:
        try:
            numbers.append(int(part))
        except ValueError:
            try:
                numbers.append(float(part))
            except ValueError as error:
                raise ValueError(f"'{part}' is not a valid number.") from error
    return numbers


# Time Complexity: O(1) | Space Complexity: O(1)
def algorithm_complexities() -> Dict[str, Tuple[str, str]]:
    """Return the documented time and space complexity for each algorithm."""
    return {
        "Array statistics": ("O(n)", "O(1)"),
        "Remove duplicates": ("O(n) average", "O(n)"),
        "Search": ("O(n)", "O(k)"),
        "Rotate right": ("O(n)", "O(n)"),
        "Two Sum": ("O(n) average", "O(n)"),
    }
