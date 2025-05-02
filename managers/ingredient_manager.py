import json
from pathlib import Path
from .base_manager import BaseManager
from validations import *
from user_input import *

class IngredientManager(BaseManager):
    """Manages ingredient storage and calorie values."""

    def __init__(self):
        self._file = Path("ingredients.json")
        self._ingredients = {}
        self.load()

    def add_item(self):
        name = get_input("Ingredient name: ", validate_non_empty_string, "Please enter valid ingredient.")
        calories = float(get_input("Calories per 100g: ", validate_calories, "Please enter a valid number."))
        self._ingredients[name] = calories
        print(f"{name} added.\n")
        self.save()

    def list_items(self):
        print("\nIngredients:")
        for name, kcal in self._ingredients.items():
            print(f"- {name}: {kcal} kcal/100g")
        print()

    def get_ingredients(self):
        return self._ingredients

    def save(self):
        with open(self._file, "w") as file:
            json.dump(self._ingredients, file)

    def load(self):
        if self._file.exists():
            with open(self._file, "r") as file:
                self._ingredients = json.load(file)