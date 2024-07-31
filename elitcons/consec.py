def find_best_recipe(recipes, ingredients):
    best_recipe = None
    highest_score = 0
    
    for recipe in recipes:
        required_ingredients = recipe.ingredients
        matching_ingredients = [ingredient for ingredient in required_ingredients if ingredient in ingredients]
        score = len(matching_ingredients)
        
        if score > highest_score:
            highest_score = score
            best_recipe = recipe
    
    return best_recipe
