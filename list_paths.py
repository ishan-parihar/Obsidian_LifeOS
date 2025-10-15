#!/usr/bin/env python3

import os
import argparse
import pathspec  # For .gitignore parsing
from datetime import datetime  # For timestamp generation


def load_gitignore_patterns(root_dir):
    """
    Loads patterns from a .gitignore file in the root_dir.
    Returns a pathspec.PathSpec object or None if .gitignore is not found or empty.
    """
    gitignore_path = os.path.join(root_dir, ".gitignore")
    patterns = []
    if os.path.isfile(gitignore_path):
        try:
            with open(gitignore_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith(
                        "#"
                    ):  # Ignore empty lines and comments
                        patterns.append(line)
            if patterns:
                return pathspec.PathSpec.from_lines(
                    pathspec.patterns.GitWildMatchPattern, patterns
                )
            else:
                print(
                    f"Info: '.gitignore' found in '{root_dir}' but it's empty or only contains comments."
                )
        except IOError as e:
            print(f"Warning: Could not read '.gitignore' from '{root_dir}': {e}")
        except Exception as e:
            print(f"Warning: Error processing '.gitignore' from '{root_dir}': {e}")
    else:
        print(f"Info: No '.gitignore' file found in '{root_dir}'.")
    return None


def build_directory_tree(root_dir, ignore_spec):
    """
    Builds a hierarchical directory tree structure.
    Returns a dictionary representing the tree structure.
    """
    tree = {"_dirs": {}, "_files": []}
    abs_root_dir = os.path.abspath(root_dir)

    for dirpath, dirnames, filenames in os.walk(abs_root_dir, topdown=True):
        # --- Explicitly ignore the .git directory ---
        if ".git" in dirnames:
            dirnames.remove(".git")

        # --- Filter directories based on .gitignore ---
        original_dirnames = list(dirnames)
        dirnames[:] = []

        for dirname in original_dirnames:
            full_dir_path_abs = os.path.join(dirpath, dirname)
            path_for_match = os.path.relpath(full_dir_path_abs, abs_root_dir)
            path_for_match_normalized = path_for_match.replace(os.sep, "/") + "/"

            if ignore_spec and ignore_spec.match_file(path_for_match_normalized):
                continue

            dirnames.append(dirname)

        # Get relative path from root
        rel_dirpath = os.path.relpath(dirpath, abs_root_dir)
        if rel_dirpath == ".":
            rel_dirpath = ""

        # Navigate to the correct position in the tree
        current_node = tree
        if rel_dirpath:
            path_parts = rel_dirpath.replace(os.sep, "/").split("/")
            for part in path_parts:
                if part not in current_node["_dirs"]:
                    current_node["_dirs"][part] = {"_dirs": {}, "_files": []}
                current_node = current_node["_dirs"][part]

        # Add directories to current level
        for dirname in sorted(dirnames):
            if dirname not in current_node["_dirs"]:
                current_node["_dirs"][dirname] = {"_dirs": {}, "_files": []}

        # Add files to current level
        files_to_add = []
        for filename in filenames:
            full_file_path_abs = os.path.join(dirpath, filename)
            path_for_match = os.path.relpath(full_file_path_abs, abs_root_dir)
            path_for_match_normalized = path_for_match.replace(os.sep, "/")

            if ignore_spec and ignore_spec.match_file(path_for_match_normalized):
                continue

            files_to_add.append(filename)

        # Add files to the current directory level
        current_node["_files"] = sorted(files_to_add)

    return tree


def format_tree_output(tree, prefix="", is_root=True):
    """
    Formats the tree structure into VSCode-like hierarchical output.
    Directories are listed first, then files, with proper indentation.
    """
    output_lines = []

    # Get directories and sort them
    dirs = list(tree["_dirs"].keys())
    dirs.sort()

    # Get files and sort them
    files = tree["_files"]

    # Process directories first
    for i, dirname in enumerate(dirs):
        is_last_item = (i == len(dirs) - 1) and len(files) == 0

        # Add directory name
        if is_root:
            output_lines.append(f"{dirname}/")
            new_prefix = "  "
        else:
            connector = "└── " if is_last_item else "├── "
            output_lines.append(f"{prefix}{connector}{dirname}/")
            extension = "    " if is_last_item else "│   "
            new_prefix = prefix + extension

        # Recursively process subdirectories and their files
        subdir_output = format_tree_output(tree["_dirs"][dirname], new_prefix, False)
        output_lines.extend(subdir_output)

    # Process files after directories
    for i, filename in enumerate(files):
        is_last_file = (i == len(files) - 1)

        if is_root:
            output_lines.append(f"{filename}")
        else:
            connector = "└── " if is_last_file else "├── "
            output_lines.append(f"{prefix}{connector}{filename}")

    return output_lines


def generate_relative_paths_list(root_dir, base_output):
    """
    Generates a text file containing a hierarchical directory structure
    within the specified root_dir, respecting .gitignore if present and always ignoring .git.
    Output format is similar to VSCode's file explorer with directories above files.
    Automatically appends a timestamp to the output filename.

    Args:
        root_dir (str): The path to the root directory to scan.
        base_output (str): The base name for the output text file (timestamp will be appended).
    """
    if not os.path.isdir(root_dir):
        print(f"Error: Directory '{root_dir}' not found.")
        return

    abs_root_dir = os.path.abspath(root_dir)
    ignore_spec = load_gitignore_patterns(root_dir)

    # Build the directory tree
    tree = build_directory_tree(root_dir, ignore_spec)

    # Format the tree into hierarchical output
    output_lines = format_tree_output(tree)

    try:
        current_timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        # Append timestamp to base filename before extension
        base, ext = os.path.splitext(base_output)
        output_file = f"{base}_{current_timestamp}{ext}"

        with open(output_file, "w", encoding="utf-8") as f:
            for line in output_lines:
                f.write(f"{line}\n")

        print(
            f"Successfully generated hierarchical directory structure with {len(output_lines)} items in '{output_file}'."
        )
        if not output_lines and os.path.isdir(abs_root_dir):
            print(
                f"(Note: The directory '{root_dir}' is empty or all its contents were ignored.)"
            )

    except IOError as e:
        print(f"Error writing to file '{output_file}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generates a text file with relative paths of files and folders, respecting .gitignore and always ignoring .git."
    )
    parser.add_argument(
        "directory",
        nargs="?",  # Makes it optional
        default=".",  # Default to current directory
        help="The root directory to scan (default: current directory).",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="file_folder_list.txt",
        help="The base name of the output text file (timestamp will be appended; default: file_folder_list.txt).",
    )

    args = parser.parse_args()

    target_directory = args.directory
    base_output = args.output

    print(f"Scanning directory: '{target_directory}'")
    print(f"Base output name: '{base_output}' (timestamp will be appended)")

    generate_relative_paths_list(target_directory, base_output)
