def fun(*args):
    return sum(args)

print(fun(4,5))

def add_num(*adding):
    return sum(adding)

print(add_num(3,4,5,6,7,8,9,1,2))


#find maximmum number

def maximum_num(*agrs1):
    return max(agrs1)

print(maximum_num(4,9,7,3,4))


#printing marks:
def printing_mark(name, *args2):
    return (f"{name} Marks: {args2}")
print(printing_mark("Sunil", 90,45,65,34,23))
         

#Kwargs

def profile(**info):
    for key, value in info.items():
        print(key, "=", value)

profile(Name="Sita", Age=19, Hobbies="Reading")



student = {"Name": "Ram", "Grade": 85}

def update_dict(d, **kwargs):
       for key, value in kwargs.items():
         d[key] = value       

update_dict(student, Grade=90, Address="Kathmandu")         
print(student)       
           

           