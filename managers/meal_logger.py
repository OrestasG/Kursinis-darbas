import json
import datetime
from pathlib import Path


class MealLogger:
    """Logs meals consumed and calculates daily calorie intake."""

    def __init__(self, meal_manager, ingredient_manager, daily_limit):
        self._file = Path("meal_logs.json")
        self._meals = meal_manager.get_meals()
        self._ingredients = ingredient_manager.get_ingredients()
        self._daily_limit = daily_limit
        self._log = {}
        self.load()

    def log_meal(self):
        today = str(datetime.date.today())
        if today not in self._log:
            self._log[today] = []

        meal = input("Meal eaten: ").lower()
        if meal not in self._meals:
            print("Meal not found.")
            return

        self._log[today].append(meal)
        self.save()
        print(f"Logged '{meal}' for today.\n")

    def calories_today(self):
        today = str(datetime.date.today())
        total = 0
        for meal in self._log.get(today, []):
            for ing, amt in self._meals.get(meal, []):
                total += self._ingredients[ing] * (amt / 100)
        return total

    def show_remaining_calories(self):
        consumed = self.calories_today()
        remaining = self._daily_limit - consumed
        print(f"Calories consumed today: {consumed:.0f}")
        print(f"Calories remaining: {remaining:.0f}\n")

    def save(self):
        with open(self._file, "w") as file:
            json.dump(self._log, file)

    def load(self):
        if self._file.exists():
            with open(self._file, "r") as file:
                self._log = json.load(file)