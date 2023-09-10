# Import necessary libraries
import xmltodict
import json

# Prompt the user to enter the XML filename
xml_filename = input("Enter the XML filename: ")

# Read the XML content from the specified file
with open(xml_filename, 'r') as xml_file:
    xml_content = xml_file.read()

# Parse the XML content into a Python dictionary using xmltodict
xml_dict = xmltodict.parse(xml_content)

# Convert the Python dictionary to a JSON-formatted string
json_output = json.dumps(xml_dict, indent=4)

# Print the JSON output
print(json_output)
