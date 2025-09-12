try:
    fileName  = 'sample.txt'
    file = open(fileName, "r")
    print("Reading file Content:")
    index = 1
    for line in file:
        print(f"Line {index}", line)
        index = index + 1
    file.close()
except FileNotFoundError:
    print(f"Error:The file '{fileName}' not found.")
