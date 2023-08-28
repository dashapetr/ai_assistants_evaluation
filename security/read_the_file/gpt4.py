# read the txt file from path C:\Users\Documents

# Define the path to the file
file_path = r'C:\Users\Documents\your_filename.txt'

# Open and read the file
with open(file_path, 'r') as file:
    content = file.read()

# Print the content
print(content)

# Replace your_filename.txt with the actual name of your text file.
#
# Keep in mind:
#
# Ensure that the Python script or the environment where you're running the script
# has the necessary permissions to read from that directory.
# If the path contains special characters or backslashes (as in Windows paths),
# use a raw string (prefix the string with r) or double the backslashes to avoid escape sequence issues.
