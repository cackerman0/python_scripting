file = open('file.txt', 'r')
f = file.readlines()

# Count number of lines
print("Lines:", len(f))

# Count number of words
print("Words:", sum(len(line.split()) for line in f))

# Count number of characters
print("Characters:", sum(len(line) for line in f))
file.close()