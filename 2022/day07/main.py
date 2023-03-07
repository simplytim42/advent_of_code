path = "/root"
file_structure = {"/root": 0}


with open("input.txt") as file:
    for command in file.readlines():

        # update the path variable
        if "$ cd" in command:

            if command[5] == '/':
                path = "/root"

            elif ".." in command:
                path = path[:path.rfind("/")]
            
            else:
                directory_name = command[5:]
                path += "/" + directory_name.strip()
                file_structure.update({path:0})
        
        elif command[0].isdigit():
            size = int(command[:command.find(" ")])

            # update directory and all parent directories with new file size
            directory = path
            for i in range(path.count("/")):
                file_structure[directory] += size
                directory = directory[:directory.rfind("/")]

# part 1
total = 0

for path in file_structure:
    if file_structure[path] <= 100000:
        total += file_structure[path]

print("part 1: ", total)


# part 2
total_disk_space = 70000000
space_required_for_update = 30000000

current_free_space = total_disk_space - file_structure["/root"]
space_to_delete = space_required_for_update - current_free_space

size_of_directory_to_delete = None
for path in file_structure:
    if file_structure[path] >= space_to_delete:

        if size_of_directory_to_delete is None:
            size_of_directory_to_delete = file_structure[path]

        elif size_of_directory_to_delete > file_structure[path]:
            size_of_directory_to_delete = file_structure[path]

print("part 2: ", size_of_directory_to_delete)