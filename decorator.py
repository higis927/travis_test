def printdebug(func):
    def __decorator():
        print('enter the login')
        func()
        print('exit the login')
    return __decorator  
 
def another_print(func):
    print "fuck %s!" % func.__name__[::-1].upper()

@printdebug  #combine the printdebug and login
def login():
    print('in login')

@another_print
def another(): 
    pass

another()
login()

