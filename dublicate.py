def find_missing_and_duplicate(arr):
    i = 0
    while i < len(arr):
        if arr[i] != i + 1 and arr[i] != arr[arr[i] - 1]:
            # Swap arr[i] with arr[arr[i] - 1]
            temp = arr[i]
            arr[i] = arr[temp - 1]
            arr[temp - 1] = temp
        else:
            i += 1

    missing_number = -1
    duplicate_number = -1

    for i in range(len(arr)):
        if arr[i] != i + 1:
            missing_number = i + 1
            duplicate_number = arr[i]
            break

    return missing_number, duplicate_number

# Example usage:
arr = [1, 4, 3, 4, 5]  # Duplicate: 3, Missing: 4
missing, duplicate = find_missing_and_duplicate(arr)
print("Missing number:", missing)
print("Duplicate number:", duplicate)
