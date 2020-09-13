#!/usr/bin/python3.7
# written by: atholcomb
# string_parse.py
# Create a function which takes in an encoded string 
# and returns a dictionary according to the following example:
#parse_code("John000Doe000123") ➞ {
#  "first_name": "John",
#  "last_name": "Doe",
#  "id": "123"
#}
#
#parse_code("michael0smith004331") ➞ {
#  "first_name": "michael",
#  "last_name": "smith",
#  "id": "4331"
#}
#
#parse_code("Thomas00LEE0000043") ➞ {
#  "first_name": "Thomas",
#  "last_name": "LEE",
#  "id": "43"
#}

import json

zero = ["0", "00", "000", "00000"]
parsed = dict()

def parse_code(string):
    for z in zero:
        if z in string:
            string_list = string.split(z) # split the string into a list
           
            # no_spaces removes all spaces in the list
            no_spaces = [val for idx, val in enumerate(string_list) if val or (not val and string_list[idx])]

            # place values from list into dictionary
            parsed["first_name"] = no_spaces[0]
            parsed["last_name"] = no_spaces[1]
            parsed["id"] = no_spaces[2]
    
            # format dictionary to look like above example
            return json.dumps(parsed, indent=2)  


print(parse_code("John000Doe000123"))
print(parse_code("michael0smith004331"))
print(parse_code("Thomas00LEE0000043"))
