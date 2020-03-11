functools update_wrapper
 
##1. partial
def add(x, y):
    return x + y

add1 = partial(add, y=3)

##2. update_wrapper
#update_wrapper这个函数的主要功能是负责copy原函数的一些属性，\
#如moudle、name、doc、等，如果不加update_wrapper,那么被装饰器修饰的函数就会丢失其上面的一些属性信息

from functools import update_wrapper

def wrapper(f):
    def wrapper_function(*args, **kwargs):
        """aaaaa"""
        return f(*args, **kwargs)
    update_wrapper(wrapper_function, f)  # <<  添加了这条语句
    return wrapper_function

@wrapper
def wrapped():
    """abcdefg"""
    pass

print(wrapped.__doc__)  # 输出`这个是被修饰的函数`
print(wrapped.__name__)  # 输出`wrapped`
print(wrapped.__module__)

##__doc__和__name__属性已经是wrapped函数中的，当然，update_wrapper函数也对__module__和__dict__等属性进行了更改和更新

##3. wraps
from functools import  wraps

def wrapper(f):
    @wraps(f)
    def wrapper_function(*args, **kwargs):
        """111"""
        return f(*args, **kwargs)
    return wrapper_function

@wrapper
def wrapped():
    """222"""
    pass

print(wrapped.__doc__)  # 输出`这个是被修饰的函数`
print(wrapped.__name__)  # 输出`wrapped`







