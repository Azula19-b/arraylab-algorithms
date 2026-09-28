"""Command-line interface for practicing efficient array algorithms."""

from array_utils import (
    algorithm_complexities,
    array_statistics,
    find_all_indices,
    parse_array,
    remove_duplicates,
    rotate_right,
    two_sum,
)


MENU = """
ArrayLab Algorithms
1. Array statistics
2. Remove duplicates
3. Search for a number
4. Rotate array right by k
5. Two Sum
6. Show time/space complexity
7. Enter a new array
8. Exit
"""


# Time Complexity: O(n) | Space Complexity: O(n)
def read_array():
    """Prompt until the user enters a valid array."""
    while True:
        raw = input("Enter numbers separated by spaces or commas: ").strip()
        try:
            return parse_array(raw)
        except ValueError as error:
            print(f"Invalid input: {error}")


# Time Complexity: O(1) | Space Complexity: O(1)
def read_number(prompt):
    """Prompt until the user enters a valid integer or decimal number."""
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            try:
                return float(raw)
            except ValueError:
                print("Invalid input: enter a number.")


# Time Complexity: O(1) | Space Complexity: O(1)
def read_integer(prompt):
    """Prompt until the user enters a valid integer."""
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Invalid input: enter a whole number.")


# Time Complexity: O(1) | Space Complexity: O(1)
def show_complexities():
    """Print a compact complexity table."""
    print("\nAlgorithm             Time             Space")
    print("-" * 50)
    for name, (time_cost, space_cost) in algorithm_complexities().items():
        print(f"{name:<21} {time_cost:<16} {space_cost}")


# Time Complexity: depends on selected operation | Space Complexity: O(n)
def main():
    """Run the interactive ArrayLab menu."""
    print("Welcome to ArrayLab! Start by entering an array.")
    numbers = read_array()

    while True:
        print(f"\nCurrent array: {numbers}")
        print(MENU)
        choice = input("Choose an option (1-8): ").strip()

        if choice == "1":
            try:
                stats = array_statistics(numbers)
                print(
                    f"Min: {stats['min']}, Max: {stats['max']}, "
                    f"Sum: {stats['sum']}, Average: {stats['average']}"
                )
            except ValueError as error:
                print(error)
        elif choice == "2":
            print(f"Without duplicates: {remove_duplicates(numbers)}")
        elif choice == "3":
            target = read_number("Number to find: ")
            indices = find_all_indices(numbers, target)
            print(f"Indices: {indices}" if indices else "Number not found.")
        elif choice == "4":
            k = read_integer("Rotate right by k: ")
            print(f"Rotated array: {rotate_right(numbers, k)}")
        elif choice == "5":
            target = read_number("Target sum: ")
            result = two_sum(numbers, target)
            print(f"Indices: {result}" if result is not None else "No pair found.")
        elif choice == "6":
            show_complexities()
        elif choice == "7":
            numbers = read_array()
        elif choice == "8":
            print("Thanks for practicing with ArrayLab!")
            break
        else:
            print("Invalid choice: enter a number from 1 to 8.")


if __name__ == "__main__":
    main()
