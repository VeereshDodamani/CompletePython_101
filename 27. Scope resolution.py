## variable scope: where a variable is visible and accessable
## scope resolution: (LEGB) Local -> Enclosed -> Global -> Built in

def func1():
    a = 1
    print(a)

def func2():
    b = 2
    print(b)

func1()
func2()

def func1():
    a = 1
    print(a)
# we can't print b here because b is not in func1 scope
    print(b)

def func2():
    b = 2
    print(b)
# we can't print a here because b is not in func1 scope
    print(a)

func1()
func2()


x = 3
def func3():
    print(x)

def func4():
    print(x)

func3()
func4()


from math import e

def func5():
    print(e)

func5()
