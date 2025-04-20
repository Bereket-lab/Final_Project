# SMARTCal

def calculate_bmr(weight, height, age, sex):
    """
    Calculates the user's BMR (Basal Metabolic Rate).
    
    BMR tells how many calories your body uses when resting.

    Args:
        weight (float): Weight in kilograms
        height (float): Height in centimeters
        age (int): Age in years
        sex (str): 'male' or 'female'

    Returns:
        float: The BMR value
    """
    if sex == 'male':
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161


def calculate_tdee(bmr, activity_level):
    """
    Adjusts BMR using activity level to get daily calorie needs.

    Args:
        bmr (float): The BMR value
        activity_level (str): 'low', 'medium', or 'high'

    Returns:
        float: Total calories needed per day
    """
    if activity_level == 'low':
        return bmr * 1.2
    elif activity_level == 'medium':
        return bmr * 1.55
    else:
        return bmr * 1.9
# meal_ideas.py

def suggest_meals(calories):
    """
    Suggests simple meal ideas based on calorie target.

    Args:
        calories (int): The user's calorie goal for the day

    Returns:
        list: A list of 3 meals as examples
    """
    if calories < 1800:
        return ["Grilled chicken salad", "Veggie stir-fry", "Fruit smoothie"]
    elif calories < 2500:
        return ["Rice with beans", "Turkey sandwich", "Baked salmon with veggies"]
    else:
        return ["Pasta with meat sauce", "Chicken burrito bowl", "Beef stew with bread"]
# main.py

from calorie_calc import calculate_bmr, calculate_tdee
from meal_ideas import suggest_meals

def run_app():
    """
    Main function to run the SmartCal app.
    Collects user info, calculates calorie needs, and gives meals.
    """
    print("Welcome to SmartCal!")

    # Get basic info
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (cm): "))
    age = int(input("Enter your age: "))
    sex = input("Enter your sex (male/female): ").lower()
    activity = input("Activity level (low/medium/high): ").lower()

    # Calculate BMR and TDEE
    bmr = calculate_bmr(weight, height, age, sex)
    tdee = calculate_tdee(bmr, activity)

    print(f"\nYour daily calorie goal is around: {int(tdee)} calories")

    # Suggest meals
    meals = suggest_meals(tdee)
    print("\nHere are some meal ideas for you:")
    for meal in meals:
        print(f"- {meal}")

if __name__ == "__main__":
    run_app()