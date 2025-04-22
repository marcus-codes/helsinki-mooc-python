import os
from pathlib import Path

# Define all exercises by section
EXERCISE_STRUCTURE = {
    "Getting Started": [
        "Emoticon",
        "Fix the code: Seven Brothers",
        "Row, Row, Row Your Boat",
        "Minutes in a year",
        "Print some code"
    ],
    "Information from the user": [
        "Name twice",
        "Name and exclamation marks",
        "Name and address",
        "Fix the code: Utterances",
        "Story"
    ],
    "More about variables": [
        "Extra space",
        "Arithmetics",
        "Fix the code: Print a single line"
    ],
    "Arithmetic operations": [
        "Times five",
        "Name and age",
        "Seconds in a day",
        "Fix the code: Product",
        "Sum and product",
        "Sum and mean",
        "Food expenditure",
        "Students in groups"
    ],
    "Conditional statements": [
        "Orwell",
        "Absolute value",
        "Soup or no soup",
        "Order of magnitude",
        "Calculator",
        "Temperatures",
        "Daily wages",
        "Loyalty bonus",
        "What to wear tomorrow",
        "Solving a quadratic equation"
    ]
}


def create_structure():
    base_path = Path("part_1")

    for section, exercises in EXERCISE_STRUCTURE.items():
        # Create section folder (e.g. 'getting_started')
        section_dir = base_path / section.lower().replace(" ", "_")
        section_dir.mkdir(exist_ok=True)

        # Create Python files for each exercise
        for exercise in exercises:
            filename = exercise.lower().replace(" ", "_").replace(":", "") + ".py"
            filepath = section_dir / filename

            # Write basic docstring
            with open(filepath, "w") as f:
                f.write(f'''"""
Helsinki MOOC - Part 1: {section}
Exercise: {exercise}
"""

# Your solution here
''')


if __name__ == "__main__":
    create_structure()
    print("✅ Part 1 folder structure created with all exercise files!")