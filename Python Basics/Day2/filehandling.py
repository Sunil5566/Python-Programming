# f = open("demo.txt", "r")

# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# f.close()

#Writing a file
f = open("demo.txt", "w+")
f.write("My name is Sunil Bhattarai\nI am from Galyang")

# Move the file pointer to the beginning before reading
f.seek(0)

data = f.read()
print(data)

f.close()
