from functools import wraps

def decorator1(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print('Called decorator1...')
        print('Exited from decorator1')
        return f(*args, **kwargs)

    return wrapper


def decorator2(f):
    def wrapper(*args, **kwargs):
        print('Called decorator2...')
        print('Exited from decorator2')
        return f(*args, **kwargs)

    return wrapper


class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)


@tracer
def spam(a1, a2, a3):
    return a1 + a2 + a3


class A:
    def __init__(self, val_a):
        self.a = val_a
        self.s = ''

    @decorator1
    @decorator2
    def print_values(self):
        self.s = f'Printed a: {self.a}'


@decorator1
def test_decorator():
    print("Test decorator...")

if __name__ == '__main__':
    a = A('Object A')
    a.print_values()
    # test methods decorations
    test_decorator()
    print(test_decorator.__name__)
