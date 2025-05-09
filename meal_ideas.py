import csv
import random

class MealSuggester:
    def __init__(self, csv_file='diet_plan.csv'):
        self.meals = []

        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    self.meals.append({
                        'Meal': row['Food_Item'],
                        'Category': row['Category'],
                        'Calories': float(row['Calories (kcal)']),
                        'Protein': float(row['Protein (g)']),
                        'Carbs': float(row['Carbohydrates (g)']),
                        'Fat': float(row['Fat (g)'])
                    })
                except (KeyError, ValueError):
                    continue

    def suggest_day_plan(self, calorie_target, max_meals=10, margin=200):
        best_plan = []
        best_total = 0

        for _ in range(3000):  # Try 3000 random shuffles to explore options
            random.shuffle(self.meals)
            plan = []
            total = 0
            for meal in self.meals:
                if total + meal['Calories'] <= calorie_target + margin:
                    plan.append(meal)
                    total += meal['Calories']
                if total >= calorie_target - margin:
                    break

            if calorie_target - margin <= total <= calorie_target + margin:
                return plan  # Found a good plan, return early

            if total > best_total and total <= calorie_target + margin:
                best_plan = plan
                best_total = total

        return best_plan if best_plan else []