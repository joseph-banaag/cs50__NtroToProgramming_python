# APPLICATION PROGRAMMING INTERFACE
import requests
import json
import sys

if len(sys.argv) != 2: #this is for error catching when the user type more than the required value
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1]) #this link limits the result to "1". it can be changed by replacing the value of limit= to desired quantity.
# sys.argv = the index value of this object will be from the one the user will type in starting ay index 1 since 0 is the filename itself.
# json_format = json.dumps(response.json(), indent=2)
# print(json_format)

dumped_format = (json.dumps(response.json(), indent=2))
print(dumped_format)
#this will display the requested songs of boysavenue in json format which is no longer a python dict

track_names = response.json()
for track in track_names["results"]:
    print(track["trackName"])

"""
THIS IS TO PRINT THE VALUES INSIDE THE sys.argv object.
try:
    print(sys.argv[2])
except IndexError:
    print("no value on index 2. try adding more keywords")
"""
print(f"this is the type of response: {type(response)}")
print(f"this is the type of dumps: {type(dumped_format)}")