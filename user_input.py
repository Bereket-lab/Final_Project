def get_user_input():
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (cm): "))
    age = int(input("Enter your age: "))
    sex = input("Enter your sex (male/female): ").strip().lower()
    activity = input("Enter your activity level (low/medium/high): ").strip().lower()
    return weight, height, age, sex, activity
