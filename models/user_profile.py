import json
from pathlib import Path


class UserProfile:
    """Handles user profile and calorie calculation."""

    def __init__(self):
        self._file = Path("user_profile.json")
        self._daily_calories = None
        if self._file.exists():
            self.load()
        else:
            self._daily_calories = self._calculate_daily_calories()
            self.save()

    def _calculate_daily_calories(self):
        gender = input("Enter your gender (male/female): ").lower()
        age = int(input("Enter your age: "))
        height = float(input("Enter your height (cm): "))
        current_weight = float(input("Current weight (kg): "))
        goal_weight = float(input("Goal weight (kg): "))
        duration = int(input("Days to reach goal: "))

        bmr = 10 * current_weight + 6.25 * height - 5 * age
        bmr += 5 if gender == "male" else -161

        total_deficit = (current_weight - goal_weight) * 7700
        daily_deficit = total_deficit / duration
        daily_calories = bmr - daily_deficit

        return max(daily_calories, 1200)

    def get_daily_calories(self):
        return self._daily_calories

    def save(self):
        with open(self._file, "w") as file:
            json.dump({"daily_calories": self._daily_calories}, file)

    def load(self):
        with open(self._file, "r") as file:
            data = json.load(file)
            self._daily_calories = data["daily_calories"]