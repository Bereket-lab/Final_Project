import tkinter as tk
from tkinter import messagebox, scrolledtext
import tkinter.ttk as ttk
from calorie_calc import CalorieCalculator
from meal_ideas import MealSuggester
import json
from datetime import datetime

def generate_plan():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        age = int(entry_age.get())
        sex = sex_var.get()
        activity = activity_var.get()

        if not sex:
            raise ValueError("Please select a sex.")

        if activity not in ("low", "medium", "high"):
            raise ValueError("Please select an activity level.")

        calc = CalorieCalculator(weight, height, age, sex, activity)
        tdee = calc.calculate_tdee()

        suggester = MealSuggester('diet_plan.csv')
        plan = suggester.suggest_day_plan(tdee)

        if not plan:
            messagebox.showwarning("No Plan", "Sorry, we couldn't generate a meal plan with the available data.")
            return

        total_cals = sum(meal['Calories'] for meal in plan)
        total_protein = sum(meal['Protein'] for meal in plan)
        total_carbs = sum(meal['Carbs'] for meal in plan)
        total_fat = sum(meal['Fat'] for meal in plan)

        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, f" Your estimated daily calorie goal is: {int(tdee)} calories\n\n")
        result_text.insert(tk.END, f" Here's a meal plan totaling ~{int(total_cals)} calories:\n\n")
        for meal in plan:
            result_text.insert(tk.END, f"- {meal['Meal']} ({meal['Category']}) — {meal['Calories']} cal | "
                                       f"Protein: {meal['Protein']}g | Carbs: {meal['Carbs']}g | Fat: {meal['Fat']}g\n")

        result_text.insert(tk.END, f"\n Total Macros — Protein: {int(total_protein)}g | "
                                   f"Carbs: {int(total_carbs)}g | Fat: {int(total_fat)}g\n")

        output_data = {
            "calorie_goal": int(tdee),
            "total_calories": int(total_cals),
            "total_protein": int(total_protein),
            "total_carbs": int(total_carbs),
            "total_fat": int(total_fat),
            "meals": plan
        }

        filename = f"meal_plan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=4)

        result_text.insert(tk.END, f"\n Meal plan saved to: {filename}")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

# GUI 
window = tk.Tk()
window.title("SMARTCal - Meal Planner")
window.geometry("750x700")

font_label = ("Arial", 12)
font_input = ("Arial", 12)
font_title = ("Arial", 16, "bold")

# Title
tk.Label(window, text="SMARTCal", font=font_title).pack(pady=15)

# Weight
tk.Label(window, text="Weight (kg):", font=font_label).pack(anchor="w", padx=20, pady=(10,0))
entry_weight = tk.Entry(window, font=font_input)
entry_weight.pack(fill="x", padx=20, pady=5)

# Height
tk.Label(window, text="Height (cm):", font=font_label).pack(anchor="w", padx=20, pady=(10,0))
entry_height = tk.Entry(window, font=font_input)
entry_height.pack(fill="x", padx=20, pady=5)

# Age
tk.Label(window, text="Age:", font=font_label).pack(anchor="w", padx=20, pady=(10,0))
entry_age = tk.Entry(window, font=font_input)
entry_age.pack(fill="x", padx=20, pady=5)

# Sex
tk.Label(window, text="Sex:", font=font_label).pack(anchor="w", padx=20, pady=(10,0))
sex_var = tk.StringVar()
sex_frame = tk.Frame(window)
tk.Radiobutton(sex_frame, text="Male", variable=sex_var, value="male", font=font_input).pack(side="left", padx=15)
tk.Radiobutton(sex_frame, text="Female", variable=sex_var, value="female", font=font_input).pack(side="left", padx=15)
sex_frame.pack(anchor="w", padx=20, pady=5)

# Activity Level
tk.Label(window, text="Activity Level:", font=font_label).pack(anchor="w", padx=20, pady=(10,0))
activity_var = tk.StringVar()
activity_combo = ttk.Combobox(window, textvariable=activity_var, font=font_input, state="readonly")
activity_combo['values'] = ("low", "medium", "high")
activity_combo.pack(fill="x", padx=20, pady=5)

# button creating
tk.Button(window, text="Generate Meal Plan", command=generate_plan,
          font=font_input, bg="#007acc", fg="white", padx=15, pady=10).pack(pady=20)

# Result 
result_text = scrolledtext.ScrolledText(window, width=85, height=20, font=("Courier New", 11), wrap=tk.WORD)
result_text.pack(padx=20, pady=10, fill="both", expand=True)

window.mainloop()