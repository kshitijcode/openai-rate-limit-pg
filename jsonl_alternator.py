import json

def modify_model_values_in_file(input_file_path, output_file_path):
    try:
        # Open the input JSONL file for reading
        with open(input_file_path, 'r') as input_file:
            lines = input_file.readlines()
        
        # Initialize a list to hold modified lines
        modified_lines = []
        
        # Iterate over each line in the file
        for i, line in enumerate(lines):
            # Load the JSON object from the line
            data = json.loads(line)
            
            # Modify the model value based on whether the line number is even or odd
            if i % 2 == 0:  # Even lines
                data['model'] = 'gpt-4-32-k'
            else:  # Odd lines
                data['model'] = 'gpt-4-32-k'
            
            # Convert the modified JSON object back to a string and add it to the list
            modified_lines.append(json.dumps(data))
        
        # Open the output file for writing and write the modified lines
        with open(output_file_path, 'w') as output_file:
            output_file.write('\n'.join(modified_lines))
        
        print(f"File successfully processed and saved as '{output_file_path}'")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file_path = 'data/real_data.jsonl'
output_file_path = 'data/real_data_gpt-4-32k.jsonl'
modify_model_values_in_file(input_file_path, output_file_path)
