# This module contains functions for filtering student data.

def filter_students_by_major(student_list, major):
    """
    Return a filtered list of students by major using a list comprehension.
    The function should:
    - Check if a student's major matches the given major (case insensitive).
    - Return a new list containing only students that match.
    """
    # List comprehension: build a new list of matching tuples in one readable line.
    return [
        student
        for student in student_list
        if student[2].lower() == major.lower()
    ]


def group_students_by_major(student_list):
    """
    Return a dictionary of major -> list of student names.

    Uses a dictionary comprehension (plus a nested list comprehension) so
    callers can look up everyone in a major without scanning the full list.
    """
    unique_major_names = {student[2] for student in student_list}
    return {
        major: [name for _, name, student_major in student_list if student_major == major]
        for major in unique_major_names
    }


def map_ids_to_students(student_list):
    """
    Return a dictionary of student ID -> student tuple using a dict comprehension.
    Useful for fast lookups with dict.get() instead of looping through the list.
    """
    return {student[0]: student for student in student_list}
