"""
    BMI Calculator Program
"""


class BMICalculationException(Exception):
    """bmi calculation custom exceptio"""


class BMICalculator:
    """
    BMI Calculation Class
    """

    def __init__(self, person) -> None:
        """
        person is a dictionary having keys as Gender, HeightCm, WeightKg
        """
        self.gender = person.get("gender", None)
        self.height_in_cm = person.get("HeightCm", None)
        self.weight_in_kg = person.get("WeightKg", None)

    def get_bmi(self) -> float:
        """
        calculates bmi of a person
        """
        if not self.height_in_cm or not self.weight_in_kg:
            raise BMICalculationException("weight or height of a person cannot be None")

        if self.height_in_cm <= 0 or self.weight_in_kg <= 0:
            raise BMICalculationException(
                "Weight or height of a person cannot be zero or in negative"
            )

        return self.weight_in_kg / (self.height_in_cm / 100) ** 2

    @staticmethod
    def get_bmi_paramters(bmi_value) -> dict:
        """
        based on BMI value this function calculates the BMI Category and health risk parameters
        """
        bmi_params = {}

        if not bmi_value or bmi_value <= 0:
            raise BMICalculationException(
                "BMI value cannot be None or zero or negative while evaluating BMI parameters"
            )

        if bmi_value <= 18.4:
            bmi_params["BMI Category"] = "Underweight"
            bmi_params["Health risk"] = "Malnutrition risk"
        elif 18.5 <= bmi_value <= 24.9:
            bmi_params["BMI Category"] = "Normal weight"
            bmi_params["Health risk"] = "Low risk"
        elif 25.0 <= bmi_value <= 29.9:
            bmi_params["BMI Category"] = "Overweight"
            bmi_params["Health risk"] = "Enhanced risk"
        elif 30.0 <= bmi_value <= 34.9:
            bmi_params["BMI Category"] = "Moderately obese "
            bmi_params["Health risk"] = "Medium risk"
        elif 35.0 <= bmi_value <= 39.9:
            bmi_params["BMI Category"] = "Severely obese"
            bmi_params["Health risk"] = "High risk"
        else:
            bmi_params["BMI Category"] = "Very severely obese"
            bmi_params["Health risk"] = "Very high risk"

        return bmi_params


if __name__ == "__main__":
    persons = [
        {"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
        {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
        {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
        {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
        {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
        {"Gender": "Female", "HeightCm": 167, "WeightKg": 82},
        {"Gender": "Male", "HeightCm": 178, "WeightKg": 0},
        {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
        {"Gender": "Female", "HeightCm": 167, "WeightKg": 82},
        {"Gender": "Female", "HeightCm": -1, "WeightKg": -2},
    ]

    overweight_persons = []

    for person in persons:
        try:
            p = BMICalculator(person)
            bmi = p.get_bmi()
            bmi_params = p.get_bmi_paramters(bmi)

            if bmi_params.get("BMI Category") not in ["Underweight", "Normal weight"]:
                overweight_persons.append(person)

        except BMICalculationException as e:
            print(e)

    print(f"Total number of overweight persons = {len(overweight_persons)}")
