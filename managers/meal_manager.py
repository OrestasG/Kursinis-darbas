import json
from pathlib import Path
from .base_manager import BaseManager


class MealManager(BaseManager):
    """Manages meals composed of user-defined ingredients."""

    def __init__(self, ingredient_manager):
        self._file = Path("meals.json")
        self._ingredient_manager = ingredient_manager
        self._meals = {}
        self.load()

    def add_item(self):
        name = input("Meal name: ").lower()
        ingredients = self._ingredient_manager.get_ingredients()
        meal_ingredients = []

        while True:
            ing = input("Add ingredient (or 'done'): ").lower()
            if ing == 'done':
                break
            elif ing not in ingredients:
                print("Ingredient not found.")
                continue
            amount = float(input("Amount in grams: "))
            meal_ingredients.append((ing, amount))

        self._meals[name] = meal_ingredients
        print(f"Meal '{name}' created.\n")
        self.save()

    def list_items(self):
        print("\nMeals:")
        for name, ing_list in self._meals.items():
            print(f"- {name}:")
            for ing, amt in ing_list:
                print(f"   • {ing} - {amt}g")
        print()

    def get_meals(self):
        return self._meals

    def save(self):
        with open(self._file, "w") as file:
            json.dump(self._meals, file)

    def load(self):
        if self._file.exists():
            with open(self._file, "r") as file:
                raw = json.load(file)
                self._meals = {
                    k: [(i, float(a)) for i, a in v]
                    for k, v in raw.items()
                }