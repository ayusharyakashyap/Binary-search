def binary_search(arr, target):
    """Perform binary search on the sorted array to find the target."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2  # Calculate the middle index
        if arr[mid] == target:  # If the target is found at mid
            return mid
        elif arr[mid] < target:  # If target is greater, ignore the left half
            left = mid + 1
        else:  # If target is smaller, ignore the right half
            right = mid - 1
    return -1  # Target not found

def get_array_from_user():
    """Get a list of elements from the user."""
    array_input = input("Enter the elements of the array separated by space: ")
    arr = array_input.split()  # Split the input string into a list of strings
    try:
        # Attempt to convert each element to an integer if possible
        arr = [int(x) for x in arr]
    except ValueError:
        pass  # If conversion fails, keep the elements as strings
    return arr

def main():
    """Main function to execute the binary search program."""
    arr = get_array_from_user()  # Get the array from the user
    
    # Sort the array since binary search requires a sorted array
    arr.sort()
    print("Sorted array:", arr)  # Print the sorted array for reference
    
    # Get the target element from the user
    target_input = input("Enter the element you want to search for: ")
    try:
        # Attempt to convert the target to an integer if possible
        target = int(target_input)
    except ValueError:
        target = target_input  # If conversion fails, keep the target as a string
    
    # Perform binary search
    result = binary_search(arr, target)
    
    # Display the result of the search
    if result != -1:
        print(f"Element {target} is present at index {result}.")
    else:
        print(f"Element {target} is not present in the array.")

# Run the main function
main()
