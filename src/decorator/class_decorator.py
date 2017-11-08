# -*- coding:utf-8 -*-
import numbers


def is_non_empty_str(name, value):
    if not isinstance(name, str):
        raise ValueError("{} must be of type str".format(name))
    if not isinstance(value, str):
        raise ValueError("{} must be of type str".format(value))


# Factory function: return paramlized function
def is_in_range(minimum=None, maximum=None):
    assert minimum is not None or maximum is not None
    def is_in_range(name, value):
        if not isinstance(value, numbers.Number):
            raise ValueError("{} must be a number".format(value))
        if minimum is not None and value < minimum:
            raise ValueError("{} {} is too small".format(name, value))
        if maximum is not None and value > maximum:
            raise ValueError("{} {} is too large")
    return is_in_range


# class Decorator
def ensure(name, validate_func, doc=None):
    def decorator(Class):
        private_name = "__" + name
        def getter(self):
            return getattr(self, private_name)
        def setter(self, value):
            validate_func(name, value)
            setattr(self, private_name, value)
        setattr(Class, name, property(getter, setter, doc=doc))
        return Class
    return decorator


@ensure("quantity", is_in_range(1000, 10000))
@ensure("price", is_in_range(10, 100))
@ensure("title", is_non_empty_str)
class Book(object):
    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return "《{}》. Price: {}. Quantity: {}".format(
            self.title, self.price, self.quantity)


print Book('old man and sea', 50, 10000) # --> 《old man and sea》. Price: 50. Quantity: 10000"

print Book('lala land', "1", 100)  # --> raise