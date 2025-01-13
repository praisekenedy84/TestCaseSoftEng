def calculate_gpa(grades_and_credit):
    if not grades_and_credit:
        raise ValueError("No grades provided")

    grade_points = {
        "A": 4.0,
        "B": 3.0,
        "C": 2.0,
        "D": 1.0,
        "F": 0.0
    }

    total_points = 0
    total_credit = 0
    all_f_grades = True  # Flag to check if all grades are F

    for grade, credit in grades_and_credit:
        if grade not in grade_points:
            raise ValueError(f"Invalid grade: {grade}")
        if credit < 0:
            raise ValueError("Credit hours must be non-negative")

        if grade != "F":
            all_f_grades = False

        total_points += grade_points[grade] * credit
        total_credit += credit

    # Allow total credit to be zero only if all grades are F
    if total_credit == 0 and not all_f_grades:
        raise ValueError("Total credit hours cannot be zero unless all grades are F")

    # Return GPA (0.0 if all grades are F and total credit are zero)
    return round(total_points / total_credit, 2) if total_credit > 0 else 0.0
