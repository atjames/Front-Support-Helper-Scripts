def emails_to_comma_separated(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r') as file:
            # Read all lines from the file and strip newline characters
            emails = [line.strip() for line in file if line.strip()]
        
        # Join the email addresses with a comma
        result = ", ".join(emails)
        
        # Write the result to the output file
        with open(output_file_path, 'w') as file:
            file.write(result)
        
        print(f"Emails successfully written to {output_file_path}")
    except FileNotFoundError:
        print(f"The file at path {input_file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'input.txt' with the path to your input file
# Replace 'output.txt' with the path to your output file
# :D 
emails_to_comma_separated('input.txt', 'output.txt')
