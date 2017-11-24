class MyInt(type):
    def __call__(cls, *args, **kwds):
        print("***** Here's My int *****", args)
        print("Now do whatever you want with these objects..")
        return type.__call__(cls, *args, **kwds)

class int(metaclass=MyInt):
    def __init__(self, x, y,z):
        self.x = x
        self.y = y
        self.z = z
    
i = int(4,5,6)