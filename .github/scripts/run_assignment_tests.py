#!/usr/bin/env python3
"""
Assignment Test Runner Script
============================

GitHub Actions script to run assignment-specific tests.
"""

import os
import sys
import subprocess
from pathlib import Path
from typing import List, Dict, Set


class AssignmentTestRunner:
    """Runs tests for specific assignments based on changed files"""

    def __init__(self):
        self.errors = []
        self.warnings = []

    def extract_assignments(self, changed_files: List[str]) -> Dict[str, Path]:
        """Extract unique assignments from changed files"""
        assignments = {}

        for file_path in changed_files:
            if not file_path.startswith('submissions/'):
                continue

            path_parts = file_path.split('/')
            if len(path_parts) < 3:
                continue

            student_id = path_parts[1]
            assignment_name = path_parts[2]

            assignment_key = f"{student_id}/{assignment_name}"
            if assignment_key not in assignments:
                assignments[assignment_key] = Path('submissions') / student_id / assignment_name

        return assignments

    def run_grader(self, assignment_path: Path) -> bool:
        """Run the grader.py script for an assignment"""
        grader_path = assignment_path / 'grader.py'

        if not grader_path.exists():
            self.warnings.append(f"⚠️ No grader.py found in {assignment_path}")
            return True  # Don't fail if no grader exists

        print(f"🧪 Running grader for {assignment_path}")

        try:
            # Change to assignment directory to run grader
            original_cwd = os.getcwd()
            os.chdir(assignment_path)

            # Run the grader script
            result = subprocess.run(
                [sys.executable, 'grader.py'],
                capture_output=True,
                text=True,
                timeout=120  # 2 minute timeout
            )

            os.chdir(original_cwd)

            # Print output for visibility
            if result.stdout:
                print("📋 Grader Output:")
                print(result.stdout)

            if result.stderr:
                print("⚠️ Grader Errors:")
                print(result.stderr)

            if result.returncode != 0:
                self.errors.append(f"❌ Grader failed for {assignment_path} (exit code: {result.returncode})")
                return False

            print(f"✅ Grader passed for {assignment_path}")
            return True

        except subprocess.TimeoutExpired:
            os.chdir(original_cwd)
            self.errors.append(f"❌ Grader timeout for {assignment_path} (120s limit)")
            return False

        except Exception as e:
            os.chdir(original_cwd)
            self.errors.append(f"❌ Error running grader for {assignment_path}: {e}")
            return False

    def check_python_syntax(self, assignment_path: Path) -> bool:
        """Basic syntax check for all Python files"""
        all_valid = True
        python_files = list(assignment_path.rglob("*.py"))

        for py_file in python_files:
            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                if not content.strip():
                    continue  # Skip empty files

                # Try to compile
                compile(content, str(py_file), 'exec')

            except SyntaxError as e:
                rel_path = py_file.relative_to(assignment_path)
                self.errors.append(f"❌ Syntax error in {rel_path}: {e}")
                all_valid = False

            except Exception as e:
                rel_path = py_file.relative_to(assignment_path)
                self.warnings.append(f"⚠️ Could not check {rel_path}: {e}")

        return all_valid

    def run_tests_for_assignments(self, changed_files: List[str]) -> bool:
        """Run tests for all assignments found in changed files"""
        self.errors = []
        self.warnings = []

        assignments = self.extract_assignments(changed_files)

        if not assignments:
            print("ℹ️ No assignments found in changed files")
            return True

        all_passed = True

        for assignment_key, assignment_path in assignments.items():
            print(f"\n🧪 Testing {assignment_key}...")

            if not assignment_path.exists():
                self.errors.append(f"❌ Assignment directory does not exist: {assignment_path}")
                all_passed = False
                continue

            # First check syntax
            if not self.check_python_syntax(assignment_path):
                all_passed = False
                continue

            # Then run grader if it exists
            if not self.run_grader(assignment_path):
                all_passed = False

        return all_passed

    def print_results(self):
        """Print test results"""
        if self.errors:
            print("\n❌ TEST ERRORS:")
            for error in self.errors:
                print(f"  {error}")

        if self.warnings:
            print("\n⚠️ TEST WARNINGS:")
            for warning in self.warnings:
                print(f"  {warning}")

        if not self.errors and not self.warnings:
            print("\n✅ All tests passed!")
        elif not self.errors:
            print(f"\n✅ Tests passed with {len(self.warnings)} warnings")


def main():
    if len(sys.argv) < 2:
        print("Usage: python run_assignment_tests.py <changed_files...>")
        sys.exit(1)

    changed_files = sys.argv[1:]

    print("🧪 Assignment Test Runner")
    print("=" * 50)
    print(f"📁 Testing assignments from {len(changed_files)} changed files...")

    runner = AssignmentTestRunner()
    success = runner.run_tests_for_assignments(changed_files)

    runner.print_results()

    if not success:
        print("\n💡 Fix the above issues and push again.")
        sys.exit(1)
    else:
        print("\n🎉 All tests passed!")
        sys.exit(0)


if __name__ == '__main__':
    main()