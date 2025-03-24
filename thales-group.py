############# ============== Monkey Patching ================ ############################

# monkey patching -  dynamic or runtime midification of a class or module
# it's often considered a last resort or a workaround rather than a best practice
# used for - Testing, bug fixes, Extending functionality, quick prototyping, Legacy code integration

class MyClass:
    def origional_method(self):
        return "original method called"
    

def new_method(self):
    return "New method called"

# Monkey patching: Replace original_method with new_method
MyClass.origional_method = new_method

obj = MyClass()
print(obj.origional_method())

############# ============== multi threading vs multi processing? ================ ############################

# Mutithreding - concurrent, shared meomory, Lightweight
# Multiprocessing - Parallelism, isolation, overhead
# Multithreading is often used for I/O-bound tasks and scenarios where lightweight concurrency is needed, 
# while multiprocessing is more suitable for CPU-bound tasks and scenarios where parallelism across multiple
# CPU cores is required. However, the choice between multithreading and multiprocessing depends on the 
# specific requirements of your application and the nature of the tasks you need to perform.
# In Python, the Global Interpreter Lock (GIL) restricts execution of multiple threads in the same 
# --process to one at a time, effectively serializing the execution of Python bytecode.
# This means that even though you're using multithreading, only one thread is executing Python
# -- bytecode at any given time. 
# Multithreading in Python may not provide significant performance improvements for CPU-bound tasks 
# --like your square calculation example
# As the threads are still subject to the limitations imposed by the GIL(Global interpreter lock)

############# ============== convert list into dictionary ================ ########################

my_list = ['apple', 'banana', 'Kiwi']

mydict = {index:value for index, value in enumerate(my_list) }

print(mydict)

############# ============== sort this dictionary using decoratorand without using sort ================ ########################
my_dict = {3: 'apple', 1: 'banana', 2:'mango'}

def sort_dict(func):
    def wrapper(d):
        sorted_dict = {k:v for k, v in sorted(d.items())}
        return func(sorted_dict)
    return wrapper


@sort_dict
def print_sort_dct(d):
    print(d)

print_sort_dct(my_dict)

############# ============== explain append, extend in the list? ================ ########################
# Syntax: list.append(element)
# Syntax: list.extend(iterable)
my_list = [1,2,3]
my_list.append(4)
print(my_list)
my_list.extend([5, 6,7,8])
print(my_list)

















