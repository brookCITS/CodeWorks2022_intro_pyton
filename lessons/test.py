from mymodule import person1
import json

#mymodule.greeting("Brook")
#print("Hello "+p["name"])

with open("files/data.json", "r") as file:
    data = json.load(file)
#print(data)
for person in data:
    print("Hello "+ person["name"])
