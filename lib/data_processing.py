# This module contains functions to process student data.

def format_student_data(student):
    """
    Format student data for display.
    The function should return a formatted string containing:
    - Student ID
    - Student Name
    - Major
    such as: "ID: 10 | Name: Louis Medina | Major: Computer Science"
    """
    student_id, name, major = student
    return f"ID: {student_id} | Name: {name} | Major: {major}"


def display_students(student_list):
    """
    Display all student records.
    Loop through the student_list and print each student using format_student_data().
    """
    for student in student_list:
        print(format_student_data(student))


def student_directory(student_list):
    """
    Convert student tuples into a dictionary keyed by ID.

    Dictionary comprehension example:
        {101: {"name": "Alice Johnson", "major": "Computer Science"}, ...}

    Look up a student with directory.get(student_id) — returns None if missing.
    """
    return {
        student_id: {"name": name, "major": major}
        for student_id, name, major in student_list
    }


def get_student_from_directory(directory, student_id):
    """Return one student dict by ID, or None if that ID is not in the directory."""
    return directory.get(student_id)
