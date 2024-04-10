filenames = ["1.file_1", "1.file_2", "1.file_3"]

filenames = [filename.replace('.','-',1) + '.txt' for filename in filenames]

print(filenames)