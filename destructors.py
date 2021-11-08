class A:
    def __init__(self, bb):
        self.b = bb

    def __del__(self):
        print("die A")


class B:
    @staticmethod
    def get_name(self):
        print("12122")
    def __init__(self):
        self.a = A(self)

    def __del__(self):
        print("die B")


def fun():
    b = B()


fun()