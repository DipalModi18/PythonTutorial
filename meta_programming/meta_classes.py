# Where ordinary class defines behaviour of its own instance,
#   meta-class defines behaviour of 'ordinary' class and its instance.
#   Meta-class can add or subtract method or field to ordinary class.
#   Python has one special class 'type' class which is default meta-class.
#   All custom type class must inherit from type class.

#
# class Calc():
# 	def add(self, x, y):
# 		return x + y
#
# 	def sub(self, x, y):
# 		return x - y
#
# 	def mul(self, x, y):
# 		return x * y
# if we have class 'Calc' having three class methods and we want to provide debug functionality
#   to all the methods in one class then we can use meta-class for this.


def debug_function(func):
	def wrapper(*args, **kwargs):
		print("{0} is called with parameter {1}".format(func.__qualname__, args[1:]))
		return func(*args, **kwargs)

	return wrapper


def debug_all_methods(cls):
	for key, val in vars(cls).items():
		if callable(val):
			setattr(cls, key, debug_function(val))
	return cls

# First we need to create a meta class 'MetaClassDebug' having debug functionality
#   and make Calc class inherit from MetaClassDebug.
#   And when we call any method from Calc class it will get invoke with our debug_function.
class MetaClassDebug(type):

	def __new__(cls, clsname, bases, clsdict):
		obj = super().__new__(cls, clsname, bases, clsdict)
		obj = debug_all_methods(obj)
		return obj


class Calc(metaclass=MetaClassDebug):
	def add(self, x, y):
		return x + y

	def sub(self, x, y):
		return x - y

	def mul(self, x, y):
		return x * y


calc = Calc()
print(calc.add(2, 3))
print(calc.sub(2, 3))
print(calc.mul(2, 3))
# we create a meta-class MetaClassDebug and write new method which is responsible
#   of creating instance of class and applied our decorator function debug_function
#   to the object(instance) which will get created of every class which inherit MetaClassDebug.
#   As Calc is inherited from MetaClassDebug hence every method has been decorated by debug_function
#   from debug_all_methods.
