d = {}  # empty dictionary
marks = {
    "sujan": 90,
    "kamal": 60,
    "bibek": 80,
    "naran": 88
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())

# marks.update({"bhawani": 100, "bhawani":99})
# print(marks)

# print(marks.get("bhawani"))

# print(marks.get("bhawani")) # Prints None
# print(marks["bhawani"])  # Returns and error

print(marks.pop("kamal")) # Removes the key and returns the value
print(marks)