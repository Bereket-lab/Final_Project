import unittest
from meal_ideas import MealSuggester

class TestMealSuggester(unittest.TestCase):

    def setUp(self):
        self.suggester = MealSuggester('diet_plan.csv')

    def test_meals_loaded(self):
        """Ensure meals are loaded from the CSV."""
        self.assertGreater(len(self.suggester.meals), 0, "No meals loaded from CSV")

    def test_day_plan_near_target(self):
        """Test if a generated plan lands close to a target calorie range."""
        target = 2500
        plan = self.suggester.suggest_day_plan(target)
        total = sum(meal['Calories'] for meal in plan)
        self.assertTrue(target - 200 <= total <= target + 200,
                        f"Total calories {total} not within margin of {target}")

    def test_day_plan_meal_structure(self):
        """Ensure each meal has all expected keys."""
        plan = self.suggester.suggest_day_plan(2000)
        for meal in plan:
            self.assertIn('Meal', meal)
            self.assertIn('Category', meal)
            self.assertIn('Calories', meal)
            self.assertIn('Protein', meal)
            self.assertIn('Carbs', meal)
            self.assertIn('Fat', meal)

    def test_day_plan_is_not_empty(self):
        """Ensure the meal plan actually returns something."""
        plan = self.suggester.suggest_day_plan(1800)
        self.assertTrue(len(plan) > 0, "Meal plan is empty")

if __name__ == '__main__':
    unittest.main()
