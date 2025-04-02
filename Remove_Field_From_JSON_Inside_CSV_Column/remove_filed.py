import pandas as pd
import json

def remove_field_from_json(csv_file, output_file, column_name, field_to_remove):

    df = pd.read_csv(csv_file)
    
    def clean_json(json_str):
        try:
            data = json.loads(json_str)
            if field_to_remove in data:
                del data[field_to_remove]
            return json.dumps(data)
        except (json.JSONDecodeError, TypeError):
            return json_str  
    
    df[column_name] = df[column_name].apply(clean_json)
    
    df.to_csv(output_file, index=False)
    print(f"Updated CSV saved as {output_file}")

# Example usage
remove_field_from_json(r"input.csv", "output.csv", "column_that_contains_the_JSON", "field_to_remove")