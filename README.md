SMARTCal is a calorie and meal planning tool written in Python. Based on your body metrics and lifestyle, it calculates your daily calorie needs (TDEE) and builds a full-day meal plan by mixing and matching foods from a dataset while aiming to meet your nutrition goals.


SMARTCal

- smartcal.py              # Main component that runs file with GUI
- calorie_calc.py          # BMR & TDEE calculations
- meal_ideas.py            # Meal planning logic
- user_input.py            # Collects user input
-  diet_plan.csv            # Dataset 
-  tests/
   - unittest_meal_ideas.py
   - unittest_calorie_calc.py
- meal_plan_*.json 


How to run: 
write the following in the command line: python smartcal.py


Enter your weight, height, age, sex, and activity level in the provided GUI. Then, the program will calculate your calorie goal and print a meal plan along with your calorie goal.
A .json file with your plan will also be created and saved automatically.

![image](https://github.com/user-attachments/assets/505b1fef-8217-4c6f-8234-b3e3a0662453)



Dataset retrieved from: 
https://www.kaggle.com/datasets/adilshamim8/daily-food-and-nutrition-dataset
