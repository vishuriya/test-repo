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


