# f = open("demo.txt", "w")
# f.close()

# f = open("demo.txt", "r")
# data = f.readline()
# data1 = f.readline()
# print(data)
# print(data1)
# print(type(data))
# f.close()

# f= open("demo.txt", "w")
# f.write("I want to learn python.")
# f = open("demo.txt", "a")
# f.write("\nHello every one..DO you know me")
# f.write("\nHAHAHA")

# f.close()


#R+ mode
f = open("demo.txt", "a+")
f.write("abcdse")
data = f.read()
print(data)
f.close()
