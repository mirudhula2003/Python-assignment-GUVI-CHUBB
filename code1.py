import os

def read_student_scores(filename):
    students = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    name, score = line.strip().split(',')
                    score = float(score)
                    students.append((name, score))
                except ValueError:
                    print("Skipping malformed line:", line.strip())
    except FileNotFoundError:
        print("Error: The file", filename, "was not found.")
    except IOError:
        print("Error: An issue occurred while reading the file", filename)

    return students

def main():
    filename = "code1.txt"
    students = read_student_scores(filename)

    if not students:
        print("No valid student data found.")
        return

    total_score = sum(score for _, score in students)
    average_score = total_score / len(students) if students else 0

    above_average_students = [name for name, score in students if score > average_score]

    print("Average score:", average_score)

    if above_average_students:
        print("Students who scored above average:")
        for student in above_average_students:
            print(student)
    else:
        print("No students scored above average.")

if __name__ == "__main__":
    main()

