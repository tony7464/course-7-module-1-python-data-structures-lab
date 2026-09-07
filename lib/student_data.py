# This module initializes student records.

# List of students stored as tuples (ID, Name, Major).
# Tuples keep each record ordered and unchanged; the outer list can grow or shrink.
students = [
    (101, "Alice Johnson", "Computer Science"),
    (102, "Bob Smith", "Mathematics"),
    (103, "Charlie Davis", "Physics"),
    (104, "David Wilson", "Computer Science"),
    (105, "Eve Lewis", "Mathematics"),
]

# Dictionary mapping student ID -> set of completed course codes.
# Dicts give fast lookup by ID; sets store unique courses and support set operations.
completed_courses = {
    101: {"CS101", "CS102", "MATH201"},
    102: {"MATH101", "MATH201", "STAT110"},
    103: {"PHYS101", "PHYS201", "MATH201"},
    104: {"CS101", "CS201", "CS102"},
    105: {"MATH101", "MATH201", "MATH301"},
}
