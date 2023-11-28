import argparse

def replace_hashtag(line):
    if line.startswith('#'):
        return '\section{' + line[1:].strip() + '}'
    return line

# Function to read markdown file and save it line by line
def process_markdown_file(input_file, output_file):

    # Read lines from the input markdown file
    with open(input_file, 'r') as infile:
        lines = infile.readlines()
    
    # Write lines to the output file
    with open(output_file, 'w') as outfile:
        for line in lines:
            line = replace_hashtag(line)



            outfile.write(line)

# Main function
def main():
    parser = argparse.ArgumentParser(description="Process markdown file.")
    
    parser.add_argument("input_file_path", type=str, help="Path to the input markdown file.")
    parser.add_argument("output_file_path", type=str, help="Path to the output markdown file.")
    
    args = parser.parse_args()

    process_markdown_file(args.input_file_path, args.output_file_path)
    print("Markdown file processed successfully!")

# Check if script is executed as the main module
if __name__ == "__main__":
    main()