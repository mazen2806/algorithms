from core.decorators import decorator1, decorator2, Tracer, all_args_str, debugger_with_args


class A:
    def __init__(self, val_a):
        self.a = val_a
        self.s = ''

    @decorator1
    def print_values(self):
        self.s = f'Printed a: {self.a}'


@all_args_str
def to_upper(*args):
    result = [s.upper() for s in args]
    return result


@debugger_with_args
def func(a, b, verbose=True):
    return a, b, verbose


@Tracer
def spam(a1, a2, a3):
    return a1 + a2 + a3


@decorator1
def test_decorator():
    print("Test decorator...")


if __name__ == '__main__':
    a = A('Object A')
    a.print_values()
    # func(1, 'a', verbose=False)
    # to_upper("123xqwsa", 123)
    # test methods decorations
    test_decorator()
    print(test_decorator.__name__)