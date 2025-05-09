class CalorieCalculator:
    def __init__(self, weight, height, age, sex, activity_level):
        self.weight = weight
        self.height = height
        self.age = age
        self.sex = sex.lower()
        self.activity_level = activity_level.lower()

    def calculate_bmr(self):
        if self.sex == 'male':
            return 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
        else:
            return 10 * self.weight + 6.25 * self.height - 5 * self.age - 161

    def calculate_tdee(self):
        bmr = self.calculate_bmr()
        if self.activity_level == 'low':
            return bmr * 1.2
        elif self.activity_level == 'medium':
            return bmr * 1.55
        else:
            return bmr * 1.9

