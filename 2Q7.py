def f():
    # local variable
    s = "I learn python."
    print(s)
f()


# This function uses global variable n
def g():
    print("Inside Function", n)

# Global scope
n = "pyhton is a programming language."
g()
print("Outside Function", n)
