import pytest
from gpa_calculator import calculate_gpa

def test_gpa_calculator_valid_input():
    grades_and_credits = [("A", 3), ("B", 4), ("C", 2)]
    assert calculate_gpa(grades_and_credits) == 3.11

def test_gpa_calculator_empty_input():
    with pytest.raises(ValueError, match="No grades provided"):
        calculate_gpa([])

def test_gpa_calculator_invalid_grade():
    grades_and_credits = [("A", 3), ("Z", 4)]
    with pytest.raises(ValueError, match="Invalid grade: Z"):
        calculate_gpa(grades_and_credits)

def test_gpa_calculator_zero_credit_hours_with_f():
    # Zero credit hours but all grades are F
    grades_and_credits = [("F", 0), ("F", 0)]
    assert calculate_gpa(grades_and_credits) == 0.0

def test_gpa_calculator_zero_credit_hours_without_f():
    # Zero credit hours with non-F grades
    grades_and_credits = [("A", 0), ("B", 0)]
    with pytest.raises(ValueError, match="Total credit hours cannot be zero unless all grades are F"):
        calculate_gpa(grades_and_credits)

def test_gpa_calculator_all_f():
    # All grades are F with non-zero credits
    grades_and_credits = [("F", 3), ("F", 3)]
    assert calculate_gpa(grades_and_credits) == 0.0

def test_gpa_calculator_mixed_grades():
    grades_and_credits = [("A", 3), ("B", 3), ("C", 3), ("D", 3), ("F", 3)]
    assert calculate_gpa(grades_and_credits) == 2.0
