import os
import sys

def print_tree(path, prefix=""):
    """Recursively print directory tree structure."""
    try:
        entries = os.listdir(path)
    except PermissionError:
        print(prefix + "|-- [Permission Denied]")
        return
    except FileNotFoundError:
        print(prefix + "|-- [Path Not Found]")
        return
    except Exception as e:
        print(prefix + f"|-- [Error: {e}]")
        return

    entries.sort()
    count = len(entries)

    for index, entry in enumerate(entries):
        full_path = os.path.join(path, entry)
        is_last = (index == count - 1)

        connector = "`--" if is_last else "|--"
        print(prefix + connector + " " + entry)

        if os.path.isdir(full_path):
            extension = "    " if is_last else "|   "
            print_tree(full_path, prefix + extension)

def main():
    try:
        if len(sys.argv) != 2:
            print("Usage: python tree.py <directory_path>")
            sys.exit(1)

        root_path = sys.argv[1]

        if not os.path.exists(root_path):
            print("Error: Path does not exist.")
            sys.exit(1)

        print(root_path)
        print_tree(root_path)
    except KeyboardInterrupt:
        print("\nProcess cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
