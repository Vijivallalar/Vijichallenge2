def linear_search_product(products, target_product):
    # Initialize an empty list to store the indices
    indices = []

    # Iterate through the list of products and check for matches
    for i, product in enumerate(products):
        if product == target_product:
            indices.append(i)  # Add the index to the list if a match is found

    return indices  # Return the list of indices (can be empty if no matches)
# Sample list of products
product_list = ["Apple", "Banana", "Orange", "Apple", "Grapes", "Apple"]

# Target product to search for
target = "Apple"

# Call the function to perform the linear search
result = linear_search_product(product_list, target)

# Print the result
if result:
    print(f"The product '{target}' was found at indices: {result}")
else:
    print(f"The product '{target}' was not found in the list.")
  