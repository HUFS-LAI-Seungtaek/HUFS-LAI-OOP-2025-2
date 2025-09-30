#!/usr/bin/env python3
"""
PR Description Update Script
===========================

GitHub Actions script to update PR description with file tree.
"""

import os
import sys
from pathlib import Path
from typing import List, Dict


def generate_file_tree(files: List[str]) -> str:
    """Generate a tree-like structure from list of files"""
    if not files:
        return "No files changed."

    # Filter only submission files
    submission_files = [f for f in files if f.startswith('submissions/')]

    if not submission_files:
        return "No submission files changed."

    # Sort files for consistent output
    submission_files.sort()

    # Create a simple tree representation
    lines = []

    # Group by path levels
    path_tree = {}
    for file_path in submission_files:
        parts = file_path.split('/')
        current = path_tree

        for part in parts:
            if part not in current:
                current[part] = {}
            current = current[part]

    def build_tree(tree_dict, prefix="", is_root=True):
        result = []
        items = list(tree_dict.items())

        for i, (name, subtree) in enumerate(items):
            is_last = i == len(items) - 1

            if is_root:
                result.append(name)
                if subtree:
                    result.extend(build_tree(subtree, "", False))
            else:
                connector = "└── " if is_last else "├── "
                result.append(f"{prefix}{connector}{name}")

                if subtree:
                    extension = "    " if is_last else "│   "
                    result.extend(build_tree(subtree, prefix + extension, False))

        return result

    return "\n".join(build_tree(path_tree))


def update_pr_description(file_tree: str, template_path: str = ".github/pull_request_template.md") -> str:
    """Update PR template with file tree"""
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            template = f.read()

        # Replace placeholder with actual file tree
        updated = template.replace('[FILE_TREE_PLACEHOLDER]', file_tree)
        return updated

    except FileNotFoundError:
        # Fallback template if file doesn't exist
        return f"""# Assignment Submission

## Changed Files

```
{file_tree}
```

## Implementation Summary
Please describe what you implemented.

## Testing
- [ ] I have run `python grader.py` locally
- [ ] All tests pass

---
**Note**: This PR will be automatically validated for correct structure and format.
"""


def main():
    if len(sys.argv) < 2:
        print("Usage: python update_pr_description.py <changed_files...>")
        sys.exit(1)

    changed_files = sys.argv[1:]

    print("🌳 Generating file tree for PR description...")
    print(f"📁 Processing {len(changed_files)} changed files...")

    # Generate file tree
    file_tree = generate_file_tree(changed_files)

    # Update PR description
    pr_description = update_pr_description(file_tree)

    print("\n📝 Updated PR Description:")
    print("=" * 50)
    print(pr_description)
    print("=" * 50)

    # Output for GitHub Actions to use
    # GitHub Actions can read this and update the PR
    with open('pr_description.md', 'w', encoding='utf-8') as f:
        f.write(pr_description)

    print("\n✅ PR description saved to pr_description.md")


if __name__ == '__main__':
    main()