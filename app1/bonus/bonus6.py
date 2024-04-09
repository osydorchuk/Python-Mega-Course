contents = ["content_1",
            "content_2",
            "content_3"]

filenames = ["file_1.txt", "file_2.txt", "file_3.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", 'w')
    file.write(content)
    file.close()