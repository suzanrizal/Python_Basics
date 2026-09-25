import os
# Select the directory whose content you want to list
directory = "/Tolls"

# Use the OS module to list the directory content 
contents = os.listdir(directory)

# Print the contents of the directory
print(contents)