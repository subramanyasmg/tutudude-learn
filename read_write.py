
try:
    data = input('Enter text to write to the file: ')
    fileName  = 'output.txt'
    file = open(fileName, "w")
    file.write(data + '\n')
    file.close()
    print(f'Data written to file {fileName}')

    additionalData = input('Enter additional text to append to the file: ')
    file = open(fileName, "a")
    file.write(additionalData)
    file.close()
    print('Data successfully appended to the file')

    print(f'Final content of the {fileName}')
    file= open(fileName, "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print(f"Error:The file '{fileName}' not found.")
