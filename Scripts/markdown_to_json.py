#!/usr/bin/env python3
"""
Script to convert all markdown files in the current directory to a single structured JSON object.
"""
import json
import os
import sys
from pathlib import Path
import re


def extract_frontmatter(content):
    """
    Extract frontmatter from markdown content if it exists.
    Frontmatter is expected to be between --- delimiters at the start of the file.
    """
    frontmatter_pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
    match = re.match(frontmatter_pattern, content, re.DOTALL)
    
    if match:
        frontmatter = match.group(1)
        body = match.group(2)
        
        # Parse frontmatter (simple key: value format)
        frontmatter_dict = {}
        for line in frontmatter.split('\n'):
            line = line.strip()
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip().strip('"\'')
                # Try to convert to appropriate types
                if value.lower() in ('true', 'false'):
                    value = value.lower() == 'true'
                elif value.isdigit():
                    value = int(value)
                frontmatter_dict[key] = value
        
        return frontmatter_dict, body
    else:
        return {}, content


def convert_markdown_to_json(directory_path='.'):
    """
    Convert all markdown files in the given directory to a structured JSON object.
    
    Args:
        directory_path (str): Path to the directory to scan for markdown files
        
    Returns:
        dict: Structured JSON object containing all markdown files
    """
    markdown_data = {
        "directory": os.path.abspath(directory_path),
        "scan_date": os.path.getmtime(directory_path),
        "files": []
    }
    
    # Walk through directory recursively
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.lower().endswith('.md'):
                file_path = os.path.join(root, file)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Extract frontmatter if it exists
                    frontmatter, body = extract_frontmatter(content)
                    
                    # Get file stats
                    stat = os.stat(file_path)
                    
                    file_info = {
                        "filename": file,
                        "relative_path": os.path.relpath(file_path, directory_path),
                        "absolute_path": file_path,
                        "size_bytes": stat.st_size,
                        "modified_timestamp": stat.st_mtime,
                        "created_timestamp": stat.st_ctime,
                        "content": body,
                        "frontmatter": frontmatter
                    }
                    
                    markdown_data["files"].append(file_info)
                    
                except Exception as e:
                    print(f"Error processing {file_path}: {str(e)}", file=sys.stderr)
    
    return markdown_data


def main():
    # Get the directory to scan - either from command line argument or current directory
    target_dir = sys.argv[1] if len(sys.argv) > 1 else '.'
    
    if not os.path.isdir(target_dir):
        print(f"Error: {target_dir} is not a valid directory", file=sys.stderr)
        sys.exit(1)
    
    print(f"Scanning directory: {os.path.abspath(target_dir)}")
    
    # Convert markdown files to JSON
    result = convert_markdown_to_json(target_dir)
    
    # Output the JSON
    json_output = json.dumps(result, indent=2, ensure_ascii=False)
    print(json_output)
    
    # Optionally save to file
    output_file = os.path.join(target_dir, 'markdown_files.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(json_output)
    
    print(f"\nProcessed {len(result['files'])} markdown files.")
    print(f"Output saved to: {output_file}")


if __name__ == "__main__":
    main()