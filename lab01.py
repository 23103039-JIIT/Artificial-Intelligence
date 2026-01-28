import numpy as np

arr1 = np.random.randint(1, 50, (3,3,3))
arr2 = np.random.randint(1, 50, (3,3,3))

print("Array 1:\n", arr1)
print("Array 2:\n", arr2)

result = arr1 + arr2
print("Result of Addition:\n", result)

result_sub = arr1 - arr2
print("Result of Subtraction:\n", result_sub)

result_mul = arr1 * arr2
print("Result of Multiplication:\n", result_mul)

result_div = np.divide(arr1, arr2, where=arr2!=0)
result_div = np.nan_to_num(result_div) 
print("Result of Division:\n", result_div)


# Statistics for array1
print("\nStatistics for Array 1:")
print("Maximum:", np.max(arr1))
print("Minimum:", np.min(arr1))
print("Mean:", np.mean(arr1))
print("Standard Deviation:", np.std(arr1))

# Statistics for array2
print("\nStatistics for Array 2:")
print("Maximum:", np.max(arr2))
print("Minimum:", np.min(arr2))
print("Mean:", np.mean(arr2))
print("Standard Deviation:", np.std(arr2))