def new_decorator(og_func):

    def new_code():
        print("Execute some code before original func")

        og_func()

        print("Execute some code after original func")

    return new_code

def original_func():
    print("I am original function")


a = new_decorator(original_func)
a()


@new_decorator
def original_func():
    print("I am original function")

original_func()
