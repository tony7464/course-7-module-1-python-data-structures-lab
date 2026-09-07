# This module contains operations related to sets.

def unique_majors(student_list):
    """
    Return a set of unique student majors using set comprehension.
    Extract the major field from each student record.
    """
    # Set comprehension: duplicates are dropped automatically.
    return {major for _, _, major in student_list}


def courses_in_common(courses_a, courses_b):
    """
    Return the intersection of two course sets (classes both students completed).
    Example: {"CS101", "CS102"} & {"CS101", "MATH201"} -> {"CS101"}
    """
    return courses_a & courses_b


def all_unique_courses(*course_sets):
    """
    Return the union of any number of course sets (every distinct course).
    Example: {"CS101"} | {"MATH201"} -> {"CS101", "MATH201"}
    """
    combined = set()
    for courses in course_sets:
        combined = combined | courses
    return combined


def courses_only_in_first(courses_a, courses_b):
    """
    Return the difference of two course sets (in A, but not in B).
    Example: {"CS101", "CS102"} - {"CS101"} -> {"CS102"}
    """
    return courses_a - courses_b
