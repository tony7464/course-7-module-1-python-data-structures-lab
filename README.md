# Student Data Management System

A small Python app for storing, filtering, and processing student records with lists, tuples, dictionaries, and sets.

## Features

- **Student records** — each student is an immutable tuple `(ID, Name, Major)` stored in a list.
- **List filtering** — `filter_students_by_major()` uses a list comprehension (case-insensitive).
- **Dictionary lookups** — `student_directory()` and `map_ids_to_students()` use dictionary comprehensions; missing IDs are handled with `.get()`.
- **Unique majors** — `unique_majors()` uses a set comprehension so duplicates drop automatically.
- **Completed courses** — each student ID maps to a **set** of course codes. Intersection, union, and difference show shared and unique courses.
- **Lazy processing** — `student_generator()` yields matching students one at a time so large datasets do not need a full filtered list in memory.

## Project Structure

```
lib/
  student_data.py      # sample students (tuples in a list) and completed_courses (dict of sets)
  filters.py           # list and dictionary comprehensions
  data_processing.py   # format/display records; dict directory + .get()
  set_operations.py    # unique majors and course set operations
  data_generator.py    # generator expression by major
main.py                # runnable demo of every feature
testing/               # pytest suite
```

## Setup Instructions

1. Fork and clone this repository, then enter the project folder:

   ```sh
   git clone <repo-url>
   cd course-7-module-1-python-data-structures-lab-1
   ```

2. Confirm Python is available (this lab targets 3.10+):

   ```sh
   python --version
   ```

3. Install dependencies with Pipenv:

   ```sh
   pipenv install
   pipenv shell
   ```

## Usage

From the project root, with the virtual environment active:

```sh
python main.py
```

That script prints all students, filters by major, shows unique majors, dictionary lookups, course set operations, the generator, and a small memory comparison (list vs generator).

### Import the modules in your own code

```python
from lib.student_data import students, completed_courses
from lib.filters import filter_students_by_major, group_students_by_major
from lib.data_processing import display_students, student_directory, get_student_from_directory
from lib.set_operations import unique_majors, courses_in_common
from lib.data_generator import student_generator

# Sequence storage (list of tuples)
display_students(students)

# List comprehension filter
cs_students = filter_students_by_major(students, "Computer Science")

# Dictionary comprehension: major -> names
by_major = group_students_by_major(students)

# Fast lookup with dict.get()
directory = student_directory(students)
alice = get_student_from_directory(directory, 101)   # dict or None

# Set of unique majors
print(unique_majors(students))

# Set operations on completed courses
shared = courses_in_common(completed_courses[101], completed_courses[104])

# Generator expression (lazy): one Mathematics student at a time
math_stream = student_generator(students, "Mathematics")
print(next(math_stream))
```

### Why generators are memory-efficient

A **list comprehension** builds the entire result list immediately. A **generator expression** stores only the iterator and produces the next student when you call `next()` or loop. `main.py` builds a 50,000-student dataset and prints `sys.getsizeof()` for both so you can see the generator stay small.

## Running Tests

```sh
pipenv shell
pytest -x
```

## Data Structures Used

| Structure | Where it is used |
| --- | --- |
| **List** | `students` collection; filtered results from list comprehensions |
| **Tuple** | each student record `(ID, Name, Major)` |
| **Dict** | `completed_courses`, `student_directory()`, `group_students_by_major()`, `map_ids_to_students()` |
| **Set** | unique majors; completed course codes; `&`, `\|`, `-` |
| **List comprehension** | `filter_students_by_major()` |
| **Dictionary comprehension** | directory, ID map, and grouping by major |
| **Set comprehension** | `unique_majors()` |
| **Generator expression** | `student_generator()` |
