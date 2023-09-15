import os
import glob

def get_files_by_extension(directory, file_extension):
    """
    Recursively find all files with a specified file extension in a directory and its subdirectories.

    Args:
        directory (str): The directory to start the search from.
        file_extension (str): The file extension to filter by (e.g., '.txt', '.jpg').

    Returns:
        list: A list of file paths matching the specified file extension.
    """
    matching_files = []

    # Recursively walk through the directory and its subdirectories
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(file_extension):
                matching_files.append(os.path.join(root, file))

    return matching_files
