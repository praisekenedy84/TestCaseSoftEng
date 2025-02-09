import pytest


def get_user_input():
    grade_points = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
    courses = []

    print("Enter course grades and credit hours. Type 'done' to finish.")

    while True:
        grade = input("Enter grade (A, B, C, D, F) or 'done' to finish: ").upper()
        if grade == "DONE":
            break
        if grade not in grade_points:
            print("Invalid grade! Please enter A, B, C, D, or F.")
            continue

        try:
            credit_hours = int(input("Enter credit hours for this course: "))
            if credit_hours < 0:
                print("Credit hours must be non-negative!")
                continue
            courses.append((grade, credit_hours))
        except ValueError:
            print("Invalid input! Please enter a number for credit hours.")

    return courses


def calculate_gpa(grades_and_credits):
    if not grades_and_credits:
        return "No courses entered. GPA cannot be calculated."

    grade_points = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}

    total_points = 0
    total_credits = 0
    all_f_grades = True

    for grade, credits in grades_and_credits:
        if grade not in grade_points:
            raise ValueError(f"Invalid grade: {grade}")
        if not isinstance(credits, (int, float)) or credits < 0:
            raise ValueError("Credit hours must be a non-negative number")

        if grade != "F":
            all_f_grades = False

        total_points += grade_points[grade] * credits
        total_credits += credits

    if total_credits == 0 and not all_f_grades:
        return "Total credit hours cannot be zero unless all grades are F."

    return round(total_points / total_credits, 2) if total_credits > 0 else 0.0


def main():
    print("Welcome to the GPA Calculator!")
    user_courses = get_user_input()
    gpa = calculate_gpa(user_courses)
    print(f"\nYour GPA is: {gpa}")


if __name__ == "__main__":
    main()


def test_gpa_calculator_valid_input():
    assert calculate_gpa([("A", 3), ("B", 4), ("C", 2)]) == 3.11


def test_gpa_calculator_empty_input():
    assert calculate_gpa([]) == "No courses entered. GPA cannot be calculated."


def test_gpa_calculator_invalid_grade():
    with pytest.raises(ValueError, match="Invalid grade: M"):
        calculate_gpa([("A", 3), ("M", 4)])


def test_gpa_calculator_zero_credit_hours_with_F():
    assert calculate_gpa([("F", 0), ("F", 0)]) == 0.0


def test_gpa_calculator_zero_credit_hours_without_F():
    assert calculate_gpa([("A", 0), ("B", 0)]) == "Total credit hours cannot be zero unless all grades are F."


def test_gpa_calculator_all_F():
    assert calculate_gpa([("F", 3), ("F", 3)]) == 0.0


def test_gpa_calculator_mixed_grades():
    assert calculate_gpa([("A", 3), ("B", 3), ("C", 3), ("D", 3), ("F", 3)]) == 2.0
