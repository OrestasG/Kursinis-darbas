import json
from pathlib import Path
from validations import *
from user_input import *

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

        while True:
            gender = get_input("Gender (male/female): ", validate_gender, "Please enter 'male' or 'female'.")
            age = int(get_input("Age: ", validate_age, "Enter a valid age between 10 and 90."))
            height = float(get_input("Enter your height (cm): ", validate_height, "Height must be between 100 and 250 cm."))
            current_weight = float(get_input("Current weight (kg): ", validate_weight, "Weight must be between 30 and 250 kg."))
            goal_weight = float(get_input("Goal weight (kg): ", validate_weight, "Weight must be between 30 and 250 kg."))
            duration = int(get_input("Days to reach goal: ", validate_day_number, "Enter a valid number of days."))

            bmr = 10 * current_weight + 6.25 * height - 5 * age
            bmr += 5 if gender == "male" else -161

            total_deficit = (current_weight - goal_weight) * 7700
            daily_deficit = total_deficit / duration
            daily_calories = bmr - daily_deficit

            if 500 <= daily_calories <= 4000:
                return daily_calories
            else:
                print(
                    "\n❌ Calculated daily calories are unsafe. "
                    "Please re-enter your information.\n"
                )

    def get_daily_calories(self):
        return self._daily_calories

    def save(self):
        with open(self._file, "w") as file:
            json.dump({"daily_calories": self._daily_calories}, file)

    def load(self):
        with open(self._file, "r") as file:
            data = json.load(file)
            self._daily_calories = data["daily_calories"]