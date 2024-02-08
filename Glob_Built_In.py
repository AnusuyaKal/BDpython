python
import glob

# Search for all text files in the current directory
text_files = glob.glob("*.txt")

# Print all the matching file paths
for file_path in text_files:
    print(file_path)