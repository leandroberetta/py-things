"""
    Interceptors (Decorators and class decorators)

    Author: Leandro Beretta <lea.bereta@gmail.com>
    
"""


def access_logger(cls):
    """ Class decorator for logging all method access. """

    class AccessLogger:
        def __init__(self, *args, **kwargs):
            self.instance = cls(*args, **kwargs)

        def __getattribute__(self, item):
            try:
                return object.__getattribute__(self, item)
            except AttributeError:
                return log_access(self.instance.__getattribute__(item))

    return AccessLogger


def time_logger(cls):
    """ Class decorator for loggging all class methods execution elapsed time. """

    class TimeLogger:
        def __init__(self, *args, **kwargs):
            self.instance = cls(*args, **kwargs)

        def __getattribute__(self, item):
            try:
                return object.__getattribute__(self, item)
            except AttributeError:
                return log_time(self.instance.__getattribute__(item))

    return TimeLogger


def log_time(f):
    """ Decorator for logging the execution elapsed time of a function. """

    import functools

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        import datetime

        before = datetime.datetime.now()
        result = f(*args, **kwargs)
        after = datetime.datetime.now()

        print("Elapsed Time = {0}".format(after - before))
        return result
    return wrapper


def log_access(f):
    """ Decorator for logging the access of a function. """

    import functools

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        print('Accessing %s' % f)

        return f(*args, **kwargs)
    return wrapper


@access_logger
@time_logger
class Greeter:
    @staticmethod
    def say_hello():
        print('Hello!')

    @staticmethod
    def say_goodbye():
        print('Goodbye!')


if __name__ == '__main__':
    greeter = Greeter()

    greeter.say_hello()
    greeter.say_goodbye()
