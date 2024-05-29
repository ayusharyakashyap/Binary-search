def binary_search(arr, target):

    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def get_array_from_user():
    
    array_input = input("Enter the elements of the array separated by space: ")
    arr = array_input.split()
    try:
        
        arr = [int(x) for x in arr]
    except ValueError:
        pass  
    return arr

def main():
    arr = get_array_from_user()
    
    target_input = input("Enter the element you want to search for: ")
    try:   
        target = int(target_input)
    except ValueError:
        target = target_input  
    
    result = binary_search(arr, target)
    
    if result != -1:
        print(f"Element {target} is present at index {result}.")
    else:
        print(f"Element {target} is not present in the array.")

main()
