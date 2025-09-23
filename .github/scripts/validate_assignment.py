#!/usr/bin/env python3
"""
Assignment Structure Validation Script
======================================

GitHub Actions script to validate assignment directory structure and files.
"""

import sys
import re
from pathlib import Path
from typing import List, Tuple


class AssignmentValidator:
    """Validates assignment directory structure and basic file requirements"""

    def __init__(self):
        self.errors = []
        self.warnings = []

        # Define required structure for each assignment
        self.assignment_structures = {
            'assignment1': {
                'required_files': [
                    'problem1.py',
                    'grader.py'
                ],
                'required_dirs': [],
                'optional_files': ['README.md']
            },
            'assignment2': {
                'required_files': [
                    'grader.py',
                    'problem1/README.md',
                    'problem1/main.py',
                    'problem2/README.md',
                    'problem2/textops/__init__.py',
                    'problem2/textops/main.py',
                    'problem2/textops/clean/__init__.py',
                    'problem2/textops/clean/filters.py',
                    'problem2/textops/tokenize/__init__.py',
                    'problem2/textops/tokenize/word.py',
                    'problem3/README.md',
                    'problem3/main.py',
                    'problem4/README.md',
                    'problem5/README.md',
                    'problem6/README.md'
                ],
                'required_dirs': [
                    'problem1',
                    'problem2',
                    'problem2/textops',
                    'problem2/textops/clean',
                    'problem2/textops/tokenize',
                    'problem3',
                    'problem4',
                    'problem5',
                    'problem6'
                ],
                'optional_files': [
                    'problem4/dsops/__init__.py',
                    'problem4/dsops/main.py',
                    'problem4/dsops/split/__init__.py',
                    'problem4/dsops/split/train_test.py',
                    'problem4/dsops/stats/__init__.py',
                    'problem4/dsops/stats/labels.py',
                    'problem5/cachekit/__init__.py',
                    'problem5/cachekit/main.py',
                    'problem6/main.py'
                ]
            }
        }

    def validate_student_id(self, path_parts: List[str]) -> bool:
        """Validate student ID format (should be numeric)"""
        if len(path_parts) < 2:
            self.errors.append("❌ Invalid path: missing student ID")
            return False

        student_id = path_parts[1]
        if not re.match(r'^\d{7,9}$', student_id):
            self.errors.append(f"❌ Invalid student ID format: '{student_id}' (should be 7-9 digits)")
            return False

        return True

    def validate_assignment_path(self, path_parts: List[str]) -> Tuple[str, str]:
        """Extract and validate assignment info from path"""
        if len(path_parts) < 3:
            self.errors.append("❌ Invalid path: missing assignment directory")
            return None, None

        student_id = path_parts[1]
        assignment = path_parts[2]

        if not re.match(r'^assignment\d+$', assignment):
            self.errors.append(f"❌ Invalid assignment format: '{assignment}' (should be 'assignmentN')")
            return None, None

        return student_id, assignment

    def validate_file_structure(self, assignment_path: Path, assignment_name: str) -> bool:
        """Validate the directory and file structure"""
        if assignment_name not in self.assignment_structures:
            self.warnings.append(f"⚠️ Unknown assignment: {assignment_name}")
            return True  # Don't fail for unknown assignments

        structure = self.assignment_structures[assignment_name]
        all_valid = True

        # Check required directories
        for required_dir in structure['required_dirs']:
            dir_path = assignment_path / required_dir
            if not dir_path.is_dir():
                self.errors.append(f"❌ Missing required directory: {required_dir}")
                all_valid = False

        # Check required files
        for required_file in structure['required_files']:
            file_path = assignment_path / required_file
            if not file_path.is_file():
                self.errors.append(f"❌ Missing required file: {required_file}")
                all_valid = False

        return all_valid

    def validate_file_content(self, assignment_path: Path, assignment_name: str) -> bool:
        """Basic validation of file contents"""
        all_valid = True

        # Check Python files for basic syntax
        python_files = list(assignment_path.rglob("*.py"))
        for py_file in python_files:
            if not self.validate_python_syntax(py_file):
                all_valid = False

        # Check specific file requirements
        if assignment_name == 'assignment2':
            all_valid &= self.validate_assignment2_specifics(assignment_path)

        return all_valid

    def validate_python_syntax(self, file_path: Path) -> bool:
        """Check if Python file has valid syntax"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Skip empty files
            if not content.strip():
                return True

            # Try to compile the code
            compile(content, str(file_path), 'exec')
            return True

        except SyntaxError as e:
            self.errors.append(f"❌ Syntax error in {file_path.relative_to(file_path.parents[3])}: {e}")
            return False
        except Exception as e:
            self.warnings.append(f"⚠️ Could not read {file_path.relative_to(file_path.parents[3])}: {e}")
            return True

    def validate_assignment2_specifics(self, assignment_path: Path) -> bool:
        """Assignment 2 specific validations"""
        all_valid = True

        # Check that textops __init__.py has re-exports (if implemented)
        textops_init = assignment_path / 'problem2/textops/__init__.py'
        if textops_init.exists():
            try:
                with open(textops_init, 'r') as f:
                    content = f.read()

                # If file is not empty, check for basic structure
                if content.strip() and 'NotImplementedError' not in content:
                    if 'from .' not in content and 'import' not in content:
                        self.warnings.append("⚠️ textops/__init__.py appears to be missing imports")

            except Exception:
                pass

        # Check that main.py files exist and aren't completely empty
        main_files = [
            'problem1/main.py',
            'problem2/textops/main.py',
            'problem3/main.py'
        ]

        for main_file in main_files:
            file_path = assignment_path / main_file
            if file_path.exists():
                try:
                    with open(file_path, 'r') as f:
                        content = f.read()
                    if len(content.strip()) < 50:  # Very basic check
                        self.warnings.append(f"⚠️ {main_file} seems very short - make sure it's implemented")
                except Exception:
                    pass

        return all_valid

    def validate_pr_title(self, pr_title: str, student_id: str, assignment_name: str) -> bool:
        """Validate PR title format: 'Nth Assignment by {student_id} (Full Name)'"""
        # Extract assignment number
        assignment_num = assignment_name.replace('assignment', '')

        # Convert number to ordinal
        ordinals = {
            '1': '1st', '2': '2nd', '3': '3rd', '4': '4th', '5': '5th',
            '6': '6th', '7': '7th', '8': '8th', '9': '9th', '10': '10th'
        }
        ordinal = ordinals.get(assignment_num, f'{assignment_num}th')

        # Expected pattern: "1st Assignment by 202500764 (Full Name)"
        pattern = rf'^{ordinal} Assignment by {student_id} \(.+\)$'

        if not re.match(pattern, pr_title):
            expected = f"{ordinal} Assignment by {student_id} (Your Full Name)"
            self.errors.append(f"❌ Invalid PR title format. Expected: '{expected}', Got: '{pr_title}'")
            return False

        return True

    def validate_changed_files(self, changed_files: List[str], pr_title: str = None) -> bool:
        """Validate structure based on changed files"""
        self.errors = []
        self.warnings = []

        # Group files by assignment
        assignments = {}

        for file_path in changed_files:
            if not file_path.startswith('submissions/'):
                continue

            path_parts = file_path.split('/')

            # Validate student ID
            if not self.validate_student_id(path_parts):
                continue

            # Validate assignment path
            student_id, assignment_name = self.validate_assignment_path(path_parts)
            if not student_id or not assignment_name:
                continue

            # Group by assignment
            assignment_key = f"{student_id}/{assignment_name}"
            if assignment_key not in assignments:
                assignments[assignment_key] = {
                    'path': Path('submissions') / student_id / assignment_name,
                    'files': []
                }
            assignments[assignment_key]['files'].append(file_path)

        # Validate each assignment
        all_valid = True
        for assignment_key, info in assignments.items():
            print(f"🔍 Validating {assignment_key}...")

            assignment_path = Path(info['path'])
            assignment_name = assignment_path.name
            student_id = assignment_path.parent.name

            # Check if assignment directory exists
            if not assignment_path.exists():
                self.errors.append(f"❌ Assignment directory does not exist: {assignment_path}")
                all_valid = False
                continue

            # Validate PR title if provided
            if pr_title and not self.validate_pr_title(pr_title, student_id, assignment_name):
                all_valid = False

            # Validate structure
            if not self.validate_file_structure(assignment_path, assignment_name):
                all_valid = False

            # Validate content
            if not self.validate_file_content(assignment_path, assignment_name):
                all_valid = False

        return all_valid

    def print_results(self):
        """Print validation results"""
        if self.errors:
            print("\n❌ VALIDATION ERRORS:")
            for error in self.errors:
                print(f"  {error}")

        if self.warnings:
            print("\n⚠️ WARNINGS:")
            for warning in self.warnings:
                print(f"  {warning}")

        if not self.errors and not self.warnings:
            print("\n✅ All validations passed!")
        elif not self.errors:
            print(f"\n✅ Structure validation passed with {len(self.warnings)} warnings")


def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_assignment.py <changed_files...> [--pr-title 'title']")
        sys.exit(1)

    # Parse arguments
    args = sys.argv[1:]
    pr_title = None
    changed_files = []

    i = 0
    while i < len(args):
        if args[i] == '--pr-title' and i + 1 < len(args):
            pr_title = args[i + 1]
            i += 2
        else:
            changed_files.append(args[i])
            i += 1

    print("🔍 Assignment Structure Validation")
    print("=" * 50)
    print(f"📁 Checking {len(changed_files)} changed files...")
    if pr_title:
        print(f"🏷️ PR Title: '{pr_title}'")

    validator = AssignmentValidator()
    is_valid = validator.validate_changed_files(changed_files, pr_title)

    validator.print_results()

    if not is_valid:
        print("\n💡 Fix the above issues and push again.")
        sys.exit(1)
    else:
        print("\n🎉 Validation successful!")
        sys.exit(0)


if __name__ == '__main__':
    main()