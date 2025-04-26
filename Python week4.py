def modify_file(input_filename, output_filename):
    """
    Reads the content of an input file, modifies it (converts to uppercase),
    and writes the modified content to a new output file.

    Args:
        input_filename (str): The name of the file to read.
        output_filename (str): The name of the file to write the modified content to.
    """
    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()
    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
        return

    modified_content = content.upper()  # Example modification: convert to uppercase

    try:
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        print(f"Successfully read '{input_filename}', modified it, and wrote to '{output_filename}'.")
    except Exception as e:
        print(f"Error writing to output file '{output_filename}': {e}")

if _name_ == "_main_":
    input_file = "input.txt"  # Replace with your input filename
    output_file = "output_modified.txt"  # Replace with your desired output filename

    # Create a sample input file for testing
    with open(input_file, 'w') as f:
        f.write("This is a sample line of text.\n")
        f.write("Another line for testing the program.\n")

    modify_file(input_file, output_file)