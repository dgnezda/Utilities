recipe = ["nori", "tuna", "soy sauce", "sushi rice"]
target_ingredient = "avocado"

def linear_search(search_list, target_value):
    for i in range(len(search_list)):
        if search_list[i] == target_value:
            return i
    raise ValueError(f"{target_value} not in list")

print(linear_search(recipe, target_ingredient))