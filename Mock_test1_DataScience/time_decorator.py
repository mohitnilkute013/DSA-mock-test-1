import time

def timer(func):

    def inner():
        # print("This is inner function")
        start = time.time()
        func()
        end = time.time()

        return end-start
        
    return inner


@timer
def my_function():
    # Function code goes here
    print("This is my_function")
    time.sleep(2)

print(f"Time required for execution is: {my_function()} seconds")

