
# STUDENT GRADE ANALYZER
# Created by: John Kerry Burudi

def calculate_grade(mark):
    if mark >= 70:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 50:
        return "C"
    elif mark >= 40:
        return "D"
    else:
        return "E"


def main():
    students = []

    print("=" * 40)
    print("       STUDENT GRADE ANALYZER")
    print("=" * 40)

    while True:
        try:
            number = int(input("Enter number of students: "))
            if number > 0:
                break
            print("Please enter a number greater than zero.")
        except ValueError:
            print("Please enter a valid whole number.")

    for i in range(number):
        print(f"\nStudent {i + 1}")

        name = input("Enter student name: ").strip()

        while not name:
            print("Name cannot be empty.")
            name = input("Enter student name: ").strip()

        while True:
            try:
                mark = float(input("Enter marks (0-100): "))
                if 0 <= mark <= 100:
                    break
                print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

        grade = calculate_grade(mark)

        students.append({
            "name": name,
            "mark": mark,
            "grade": grade
        })

    print("\n" + "=" * 40)
    print("         CLASS PERFORMANCE REPORT")
    print("=" * 40)

    for student in students:
        print(
            f"{student['name']}: "
            f"{student['mark']}% - Grade {student['grade']}"
        )

    average = sum(s["mark"] for s in students) / len(students)

    top_student = max(students, key=lambda s: s["mark"])
    lowest_student = min(students, key=lambda s: s["mark"])

    passed = sum(1 for s in students if s["mark"] >= 40)
    pass_rate = (passed / len(students)) * 100

    print("\nCLASS SUMMARY")
    print("-" * 40)
    print(f"Class average: {average:.2f}%")
    print(f"Top student: {top_student['name']}")
    print(f"Highest mark: {top_student['mark']}%")
    print(f"Lowest student: {lowest_student['name']}")
    print(f"Pass rate: {pass_rate:.2f}%")

    print("\nAnalysis completed successfully!")


if __name__ == "__main__":
    main()
