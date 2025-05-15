import unittest
from calorie_calc import CalorieCalculator

class TestCalorieCalculator(unittest.TestCase):

    def test_bmr_male(self):
        """Test BMR calculation for a male."""
        calc = CalorieCalculator(weight=70, height=175, age=25, sex='male', activity_level='low')
        expected_bmr = 10 * 70 + 6.25 * 175 - 5 * 25 + 5
        self.assertAlmostEqual(calc.calculate_bmr(), expected_bmr)

    def test_bmr_female(self):
        """Test BMR calculation for a female."""
        calc = CalorieCalculator(weight=60, height=160, age=30, sex='female', activity_level='medium')
        expected_bmr = 10 * 60 + 6.25 * 160 - 5 * 30 - 161
        self.assertAlmostEqual(calc.calculate_bmr(), expected_bmr)

    def test_tdee_low(self):
        """Test TDEE for low activity level."""
        calc = CalorieCalculator(70, 175, 25, 'male', 'low')
        expected = calc.calculate_bmr() * 1.2
        self.assertAlmostEqual(calc.calculate_tdee(), expected)

    def test_tdee_medium(self):
        """Test TDEE for medium activity level."""
        calc = CalorieCalculator(70, 175, 25, 'male', 'medium')
        expected = calc.calculate_bmr() * 1.55
        self.assertAlmostEqual(calc.calculate_tdee(), expected)

    def test_tdee_high(self):
        """Test TDEE for high activity level."""
        calc = CalorieCalculator(70, 175, 25, 'male', 'high')
        expected = calc.calculate_bmr() * 1.9
        self.assertAlmostEqual(calc.calculate_tdee(), expected)

if __name__ == '__main__':
    unittest.main()
