class Singleton:
    __instance = None
    def __init__(self):
        if not Singleton.__instance:
            print(' __init__ method called..')
        else:
            print('Instance already created: ', self.getIntance())
    @classmethod
    def getIntance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance

a = Singleton() # Class initialized, but object not created
print('Object created', Singleton.getIntance()) # Object gets created here
b = Singleton() # Instance already created