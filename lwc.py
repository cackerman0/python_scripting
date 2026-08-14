import argparse

parser = argparse.ArgumentParser(description='Read contents of a file.')
parser.add_argument('file_path', help='Path to the file to read.')
args = parser.parse_args()

file = open(args.file_path, 'r')
f = file.readlines()

# Count number of lines
print("Lines:", len(f))

# Count number of words
print("Words:", sum(len(line.split()) for line in f))

# Count number of characters
print("Characters:", sum(len(line) for line in f))
file.close()