# Maximum Subarray Problem

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# 🐌 Brute Force Method – Check All Subarrays
# Time Complexity: O(n²)

def max_subarray_brute_force(arr):
    max_sum = float('-inf')  # Initialize to negative infinity
    for i in range(len(arr)):
        curr_sum = 0
        for j in range(i, len(arr)):
            curr_sum += arr[j]
            max_sum = max(max_sum, curr_sum)
    return max_sum

# 🚀 Improved Prefix Sum – Smarter Traversal
# Time Complexity: O(n²)
def max_subarray_prefix_sum(arr):
    prefix = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        prefix[i + 1] = prefix[i] + arr[i]

    max_sum = float('-inf')
    for i in range(len(arr)):
        for j in range(i + 1, len(arr) + 1):
            max_sum = max(max_sum, prefix[j] - prefix[i])
    return max_sum

# 🧠 Optimal Kadane's Algorithm – Efficient and Elegant
# Time Complexity: O(n)

def max_subarray_kadane(arr):
    current_max = global_max = arr[0]
    for i in range(1, len(arr)):
        current_max = max(arr[i], current_max + arr[i])
        global_max = max(global_max, current_max)
    return global_max

# Output Comparison
print("Brute Force:", max_subarray_brute_force(arr))      # Output: 6
print("Prefix Sum:", max_subarray_prefix_sum(arr))        # Output: 6
print("Kadane's Algo:", max_subarray_kadane(arr))         # Output: 6
