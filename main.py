"""
Demo script for the Student Data Management System.

Run from the project root (after pipenv shell):
    python main.py
"""
import sys

from lib.student_data import students, completed_courses
from lib.filters import filter_students_by_major, group_students_by_major, map_ids_to_students
from lib.data_processing import display_students, student_directory, get_student_from_directory
from lib.set_operations import (
    unique_majors,
    courses_in_common,
    all_unique_courses,
    courses_only_in_first,
)
from lib.data_generator import student_generator


def demonstrate_memory_efficiency():
    """
    Show why a generator expression uses less memory than a list comprehension.

    A list comprehension stores every matching student immediately.
    A generator expression stores only the iterator — each student is created
    when you ask for the next value (lazy evaluation).

    The sample `students` list is tiny, so we compare against a large dataset
    where the difference is obvious.
    """
    majors = ("Computer Science", "Mathematics", "Physics")
    large_dataset = [
        (i, f"Student {i}", majors[i % 3])
        for i in range(50_000)
    ]

    as_list = [student for student in large_dataset if student[2] == "Mathematics"]
    as_generator = (student for student in large_dataset if student[2] == "Mathematics")

    print("Memory comparison (50,000 students, Mathematics filter):")
    print(f"  List comprehension size:     {sys.getsizeof(as_list):,} bytes")
    print(f"  Generator expression size:   {sys.getsizeof(as_generator):,} bytes")
    print("  The generator stays small because it does not store the full result.")


def main():
    print("=== All students ===")
    display_students(students)

    print("\n=== Computer Science majors (list comprehension) ===")
    display_students(filter_students_by_major(students, "Computer Science"))

    print("\n=== Unique majors (set comprehension) ===")
    print(unique_majors(students))

    print("\n=== Students grouped by major (dictionary comprehension) ===")
    print(group_students_by_major(students))

    print("\n=== Dictionary lookup with .get() ===")
    directory = student_directory(students)
    found = get_student_from_directory(directory, 101)
    missing = get_student_from_directory(directory, 999)
    print(f"  ID 101: {found}")
    print(f"  ID 999: {missing}")

    print("\n=== Fast ID map (dictionary comprehension) ===")
    by_id = map_ids_to_students(students)
    print(f"  ID 104: {by_id.get(104)}")

    print("\n=== Completed courses (sets) ===")
    alice_courses = completed_courses[101]
    david_courses = completed_courses[104]
    print(f"  Alice: {alice_courses}")
    print(f"  David: {david_courses}")
    print(f"  Shared (intersection): {courses_in_common(alice_courses, david_courses)}")
    print(f"  Only Alice (difference): {courses_only_in_first(alice_courses, david_courses)}")
    print(f"  All unique (union): {all_unique_courses(alice_courses, david_courses)}")

    print("\n=== Lazy generator by major (Mathematics) ===")
    math_stream = student_generator(students, "Mathematics")
    print(f"  First: {next(math_stream)}")
    print(f"  Next:  {next(math_stream)}")

    print()
    demonstrate_memory_efficiency()


if __name__ == "__main__":
    main()
