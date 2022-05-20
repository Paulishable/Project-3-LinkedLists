with open("data.txt", "r") as data_file:
    lines = data_file.readlines()
    for line in lines:
        print(line)
