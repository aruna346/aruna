import json

# Specify the path to the JSON file
json_file_path = "config_test.json"

# Read the data from the JSON file
with open(json_file_path, "r") as json_file:
    data = json.load(json_file)

# Extract the 'number' from the data
number = data.get("number")

# Check if the number is more than or equal to 70
if number is not None and number >= 70:
    print("You have passed")
else:
    print("You have not passed")
