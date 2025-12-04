#1.Convert to integer
x = "10"
y = int(x)
print(y, type(y))

Car_model = "2001"
In_Int = int(Car_model)
print(Car_model, type(Car_model))
print(In_Int, type(In_Int))



#2.Convert to float
Grade = 3
float_Grade = float(Grade)
print(float_Grade, type(float_Grade))



#3.Convert to String
Number = 90
Num = str(Number)
print(Num, type(Num))



#4.Convert to boolean
a = 0
b = bool(a)
print(b)

c = 1
d = bool(c)
print(d)



#5.List dict set tuples
 #List
e = (3,5)
f = print(list(e))
print(type(f))

#List to sets
g = [1,2,3,4,5,5,5,7,8,8,8]
h = set(g)
print(h)

#tuples into dict
l = ("car", "ball")
m = ("cat", "dog")
o = dict(zip(l,m))
print(o)

#  Using list of tuples:
pairs = [("car", "cat"), ("ball", "dog")]
p = dict(pairs)
print(p)





#Printing something

name = "sunil"
surname = "bhattarai"
print(name, surname, sep="..")

