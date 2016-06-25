"""
    Traits (Decorator factories and class decorators)

    Author: Leandro Beretta <lea.bereta@gmail.com>

"""

import logging


def logger(level):
    """ Decorator factory which creates a class decorator for adding a logger object to some class. """

    def decorator(cls):
        import logging

        logger_obj = logging.getLogger(cls.__name__)
        logging.basicConfig(format='%(levelname)s %(message)s', level=level)

        setattr(cls, 'logger', logger_obj)

        return cls
    return decorator


@logger(logging.DEBUG)
class Greeter:
    @staticmethod
    def say_hello():
        Greeter.logger.info('Hello!')
        print('Hello!')

    def say_goodbye(self):
        self.logger.info('Goodbye!')
        print('Goodbye!')


if __name__ == '__main__':
    greeter = Greeter()

    greeter.say_hello()
    greeter.say_goodbye()
