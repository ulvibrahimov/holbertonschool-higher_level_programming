import os

def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template.
    """
    # 1. Check input types
    if not isinstance(template, str):
        print("Error: template should be a string.")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(i, dict) for i in attendees):
        print("Error: attendees should be a list of dictionaries.")
        return

    # 2. Handle empty inputs
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # 3. Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        content = template
        placeholders = ["name", "event_title", "event_date", "event_location"]
        
        for placeholder in placeholders:
            # Get the value from dictionary, defaulting to None if missing
            value = attendee.get(placeholder)
            
            # Replace missing or None values with "N/A"
            if value is None:
                value = "N/A"
                
            # Replace the placeholder in the template
            content = content.replace(f"{{{placeholder}}}", str(value))
            
        output_filename = f"output_{index}.txt"
        
        # 4. Generate Output Files
        try:
            with open(output_filename, 'w') as file:
                file.write(content)
        except Exception as e:
            print(f"Error writing to {output_filename}: {e}")

