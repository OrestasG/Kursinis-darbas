from models.user_profile import UserProfile
from managers.ingredient_manager import IngredientManager
from managers.meal_manager import MealManager
from managers.meal_logger import MealLogger
from services.meal_suggester import MealSuggester


class NutritionApp:
    """Main application class composed of managers and helpers."""

    def __init__(self):
        self.user = UserProfile()
        self.ingredients = IngredientManager()
        self.meals = MealManager(self.ingredients)
        self.logger = MealLogger(
            self.meals,
            self.ingredients,
            self.user.get_daily_calories()
        )
        self.suggester = MealSuggester(self.meals)

    def run(self):
        while True:
            print("\n📋 MENU")
            print("1. Add Ingredient")
            print("2. List Ingredients")
            print("3. Create Meal")
            print("4. List Meals")
            print("5. Log Meal")
            print("6. Show Remaining Calories")
            print("7. Suggest Meals")
            print("8. Exit")

            choice = input("Choose an option: ")

            if choice == '1':
                self.ingredients.add_item()
            elif choice == '2':
                self.ingredients.list_items()
            elif choice == '3':
                self.meals.add_item()
            elif choice == '4':
                self.meals.list_items()
            elif choice == '5':
                self.logger.log_meal()
            elif choice == '6':
                self.logger.show_remaining_calories()
            elif choice == '7':
                self.suggester.suggest()
            elif choice == '8':
                print("🍽️ Goodbye!")
                break
            else:
                print("❌ Invalid option.")


if __name__ == "__main__":
    app = NutritionApp()
    app.run()