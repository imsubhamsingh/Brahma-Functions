def product_of_two_array(arr1, arr2):
    """
    This function takes two arrays and returns their product
    """
    product = []
    for i in range(len(arr1)):
        product.append(arr1[i] * arr2[i])
    return product


# Testing the function
print(product_of_two_array([1, 2, 3], [4, 5, 6]))  # Output: [4,10,18]
print(product_of_two_array([10, 20, 30], [1, 2, 3]))  # Output: [10,40,90]
print(product_of_two_array([2, 4, 6], [8, 10, 12]))  # Output: [16,40,72]
