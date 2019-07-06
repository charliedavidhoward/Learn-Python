def capitalize_i(file):
    i_count = file.count('i ')
    file = file.replace('i ', 'I ')
    i_count += file.count('-i-')
    file = file.replace('-i-', '-I-')
    print("There were " + str(i_count) + " corrections")
    return file


with open("green_eggs.txt", "r") as f_open:
    file_1 = f_open.read()

file_2 = open("result.txt", "w")

file_2.write(capitalize_i(file_1))
