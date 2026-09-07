# This module contains functions to lazily generate student data.

def student_generator(student_list, major):
    """
    Generate student records filtered by major lazily for memory efficiency
    using a Python generator.
    """
    # Generator expression: yields one matching student at a time.
    # Unlike a list comprehension, this does not build the full result list
    # in memory — values are produced only when next() or a loop asks for them.
    return (
        student
        for student in student_list
        if student[2].lower() == major.lower()
    )
