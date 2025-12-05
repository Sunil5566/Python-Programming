# class Account:
#     def __init__(self,acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass

#     def reset_password(self):
#         print(self.__acc_pass)    

# acc1 = Account("12345", "abcde")

# print(acc1.acc_no)
# # print(acc1.acc_pass)
# print(acc1.reset_password())


class Person:
    __name = "Anyone"

    def p1_name(self):
        print(self.__name)


p1 = Person()
print(p1.p1_name())    