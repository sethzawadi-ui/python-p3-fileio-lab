def write_file(file_name, content):
    """Writes content to a .txt file, overwriting if it exists."""
    file_path = f"{file_name}.txt"
    with open(file_path, 'w') as f:
        f.write(content)

def append_file(file_name, content):
    """Appends content to a .txt file."""
    file_path = f"{file_name}.txt"
    with open(file_path, 'a') as f:
        f.write(content)

def read_file(file_name):
    """Reads content from a .txt file and returns it as a string."""
    file_path = f"{file_name}.txt"
    with open(file_path, 'r') as f:
        return f.read()
