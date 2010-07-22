from wrappers import cached
from test_db import db_get, db_set    

# THOSE LOOK LIKE SOME HELPER FUNCTIONS

@cached('key1')
def simple_function1():
    return db_get(id=1)

@cached('key2')
def simple_function2():
    return db_get(id=2)

# SUPPOSE THIS IS IN ANOTHER MODULE

@cached('big_key1')
def some_bigger_function():
    """
    this function depends on big_key1, key1 and key2 
    """          
    def inner_workings():
        db_set(1, 'something totally new')
    ####### 
    ##   imagine 100 lines of code here :)
    ######                                
    inner_workings()
    
    return [simple_function1(),simple_function2()]

if __name__ == '__main__':
    simple_function1()
    simple_function2()    
    a,b = some_bigger_function()
    assert a == db_get(id=1), "this fails because we didn't invalidated cache properly"
