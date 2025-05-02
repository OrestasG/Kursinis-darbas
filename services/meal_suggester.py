from validations import *
from user_input import *

class MealSuggester:
    """Suggests meals based on available ingredients."""

    def __init__(self, meal_manager):
        self._meals = meal_manager.get_meals()

    def suggest(self):
        available = get_input(
            "Enter available ingredients (comma-separated): ",
            validate_non_empty_string,
            "Please enter at least one ingredient."
        )
        available = available.split(",")
        available = [i.strip() for i in available]

        print("\nSuggested meals:")
        found = False
        for meal, ing_list in self._meals.items():
            if all(ing in available for ing, _ in ing_list):
                print(f"- {meal}")
                found = True
        # If no meals match the available ingredients, inform the user.
        if not found:
            print("No matches found.\n")