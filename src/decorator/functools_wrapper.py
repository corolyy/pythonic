from datetime import datetime
import functools

def log(func):
    def wrapper(*args, **kw):
        print 'call {}()'.format(func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print datetime.now()

now()  #now = log(now) --> call now()\n ${now}
print now.__name__ # --> wrapper

def log_adv(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print 'call {}()'.format(func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

@log_adv('execute')
def now_adv():
    print datetime.now()

now_adv() #now = log('execute')(now_adv)
print now_adv.__name__ # --> wrapper


def log_functools(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print 'call {}()'.format(func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

@log_functools('execute')
def now_funtools():
    print datetime.now()

now_funtools()
print now_funtools.__name__ # --> now_funtools