"""
    unit test for bmi calculation class
"""

import unittest

from bmi_calculator import BMICalculationException, BMICalculator


class TestBMICalculator(unittest.TestCase):
    """bmi calculation unittest module"""

    def test_bmi_calculation_happy_case(self):
        """bmi calculation unittest : positive case"""
        bmi_obj = BMICalculator({"Gender": "Female", "HeightCm": 166, "WeightKg": 62})
        bmi_value = bmi_obj.get_bmi()
        self.assertIsNotNone(bmi_value)
        self.assertIsInstance(bmi_obj.get_bmi_paramters(bmi_value), dict)

    def test_bmi_calculation_negative_case(self):
        """bmi calculation unittest : negative input case"""
        bmi_obj = BMICalculator({"Gender": "Female", "HeightCm": -1, "WeightKg": -1})
        self.assertRaises(BMICalculationException, bmi_obj.get_bmi)

    def test_bmi_calculation_zero_weight_values(self):
        """bmi calculation unittest : zero weight case"""
        with self.assertRaises(
            BMICalculationException,
            msg="Weight or height of a person cannot be zero or in negative",
        ):
            bmi_obj = BMICalculator({"Gender": "Female", "HeightCm": 10, "WeightKg": 0})
            bmi_obj.get_bmi()

    def test_bmi_calculation_none_weight_values(self):
        """bmi calculation unittest : none weight case"""
        with self.assertRaises(
            BMICalculationException,
            msg="weight or height of a person cannot be None",
        ):
            bmi_obj = BMICalculator(
                {"Gender": "Female", "HeightCm": None, "WeightKg": None}
            )
            bmi_obj.get_bmi()

    def test_bmi_calculation_zero_height_values(self):
        """bmi calculation unittest : zero height case"""
        with self.assertRaises(
            BMICalculationException,
            msg="Weight or height of a person cannot be zero or in negative",
        ):
            bmi_obj = BMICalculator({"Gender": "Female", "HeightCm": 0, "WeightKg": 1})
            bmi_obj.get_bmi()

    def test_bmi_calculation_negative_weight_values(self):
        """bmi calculation unittest : negative weight case"""
        with self.assertRaises(
            BMICalculationException,
            msg="Weight or height of a person cannot be zero or in negative",
        ):
            bmi_obj = BMICalculator(
                {"Gender": "Female", "HeightCm": 10, "WeightKg": -10}
            )
            bmi_obj.get_bmi()

    def test_bmi_calculation_negative_height_values(self):
        """bmi calculation unittest : negative height case"""
        with self.assertRaises(
            BMICalculationException,
            msg="Weight or height of a person cannot be zero or in negative",
        ):
            bmi_obj = BMICalculator(
                {"Gender": "Female", "HeightCm": -10, "WeightKg": 10}
            )
            bmi_obj.get_bmi()

    def test_bmi_calculation_exceptions(self):
        """bmi calculation unittest : exception case"""
        bmi_obj = BMICalculator({"Gender": "Female", "HeightCm": 0, "WeightKg": 0})
        self.assertRaises(BMICalculationException, bmi_obj.get_bmi)

    def test_bmi_params_calculation_function(self):
        """bmi calculation unittest : for BMI parameters function"""
        bmi_obj = BMICalculator({"Gender": "Female", "HeightCm": 166, "WeightKg": 62})
        bmi_value = bmi_obj.get_bmi()
        bmi_params = bmi_obj.get_bmi_paramters(bmi_value)
        self.assertIsInstance(bmi_params, dict)

    def test_bmi_params_calculation_function_exception(self):
        """bmi calculation unittest : for BMI parameters function for exception case"""
        with self.assertRaises(
            BMICalculationException,
            msg="BMI value cannot be None or zero or negative while evaluating BMI parameters",
        ):

            BMICalculator.get_bmi_paramters(None)

    def test_bmi_params_calculation_function_for_underweight(self):
        """bmi calculation unittest : for BMI parameters function and underweight values"""
        bmi_params = BMICalculator.get_bmi_paramters(15.0)
        self.assertEqual(bmi_params["BMI Category"], "Underweight")

    def test_bmi_params_calculation_function_for_overweightt(self):
        """bmi calculation unittest : for BMI parameters function and overweight values"""
        bmi_params = BMICalculator.get_bmi_paramters(27.2)
        self.assertEqual(bmi_params["BMI Category"], "Overweight")

    def test_bmi_params_calculation_function_for_medium_risk(self):
        """bmi calculation unittest : for BMI parameters function and medium risk individual"""
        bmi_params = BMICalculator.get_bmi_paramters(33.9)
        self.assertEqual(bmi_params["Health risk"], "Medium risk")


if __name__ == "__main__":
    unittest.main()
