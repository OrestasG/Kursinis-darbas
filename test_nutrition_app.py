import unittest
from unittest.mock import patch

from models.user_profile import UserProfile
from managers.ingredient_manager import IngredientManager
from managers.meal_manager import MealManager
from managers.meal_logger import MealLogger


class TestIngredientManager(unittest.TestCase):

    def setUp(self):
        self.manager = IngredientManager()
        self.manager._ingredients = {}

    def test_add_ingredient(self):
        self.manager._ingredients = {}
        with patch("builtins.input", side_effect=["banana", "89"]):
            self.manager.add_item()
        self.assertIn("banana", self.manager._ingredients)
        self.assertEqual(self.manager._ingredients["banana"], 89)

    def test_list_ingredients(self):
        self.manager._ingredients = {"apple": 52}
        with patch("builtins.print") as mock_print:
            self.manager.list_items()
            mock_print.assert_any_call("- apple: 52 kcal/100g")


class TestMealManager(unittest.TestCase):

    def setUp(self):
        self.ing_manager = IngredientManager()
        self.ing_manager._ingredients = {"rice": 130, "chicken": 165}
        self.manager = MealManager(self.ing_manager)

    def test_add_meal(self):
        with patch("builtins.input", side_effect=[
            "chicken rice bowl", "chicken", "150", "rice", "200", "done"
        ]):
            self.manager.add_item()
        self.assertIn("chicken rice bowl", self.manager._meals)
        self.assertEqual(
            self.manager._meals["chicken rice bowl"],
            [("chicken", 150.0), ("rice", 200.0)]
        )


class TestMealLogger(unittest.TestCase):

    def setUp(self):
        self.ingredients = {"egg": 155}
        self.meals = {"boiled egg": [("egg", 100)]}
        self.logger = MealLogger.__new__(MealLogger)
        self.logger._ingredients = self.ingredients
        self.logger._meals = self.meals
        self.logger._daily_limit = 2000
        self.logger._log = {}

    def test_log_and_calculate(self):
        self.logger._log[str(self._today())] = ["boiled egg"]
        total = self.logger.calories_today()
        self.assertEqual(total, 155)

    def _today(self):
        import datetime
        return datetime.date.today()


class TestUserProfile(unittest.TestCase):

    def test_calorie_calculation(self):
        # Mock input for a basic scenario
        with patch("builtins.input", side_effect=[
            "female", "30", "165", "70", "60", "60"
        ]):
            profile = UserProfile()
            cals = profile.get_daily_calories()
            self.assertTrue(cals > 500)


if __name__ == '__main__':
    unittest.main()