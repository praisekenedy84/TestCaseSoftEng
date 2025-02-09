def get_user_input():
    """
    Gets user input for grades and credit hours.
    Returns a list of (grade, credit_hours) tuples.
    """
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
    """
    Calculates the GPA based on the provided grades and credit hours.
    """
    if not grades_and_credits:
        return "No courses entered. GPA cannot be calculated."

    grade_points = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}

    total_points = 0
    total_credits = 0
    all_f_grades = True

    for grade, credits in grades_and_credits:
        if grade != "F":
            all_f_grades = False
        total_points += grade_points[grade] * credits
        total_credits += credits

    # If all grades are F and total credits are zero, return 0.0
    if total_credits == 0 and all_f_grades:
        return 0.0
    elif total_credits == 0:
        return "Total credit hours cannot be zero unless all grades are F."

    return round(total_points / total_credits, 2)


def main():
    """
    Main function to run the interactive GPA calculator.
    """
    print("Welcome to the GPA Calculator!")
    user_courses = get_user_input()
    gpa = calculate_gpa(user_courses)
    print(f"\nYour GPA is: {gpa}")


if __name__ == "__main__":
    main()
