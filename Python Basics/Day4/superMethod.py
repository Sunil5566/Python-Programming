class A:
    def __init__(self):
        print("A constructor")

class B(A):
    def __init__(self):
        super().__init__()
        print("B constructor")


class C(B):
    def __init__(self):
        super().__init__()
        print("C constructor")

c1 = C()
                