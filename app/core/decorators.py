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


class Tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)


def all_args_str(func):
    @wraps(func)
    def wrapper(*args):
        if not all(isinstance(arg, str) for arg in args):
            raise ValueError('All arguments should be strings')
        return func(*args)
    return wrapper


def debugger_with_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Вызываю функцию {func.__name__} с args {args} и kwargs {kwargs}')
        return func(*args, **kwargs)
    return wrapper
