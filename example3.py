from wrappers import cached, invalidate 
from test_db import db_get, db_set    

# THOSE LOOK LIKE SOME HELPER FUNCTIONS

@cached('key1')
def simple_function1():
    return db_get(id=1)

@cached('key2')
def simple_function2():
    return db_get(id=2)

# SUPPOSE THIS IS IN ANOTHER MODULE

@cached('key')
def some_bigger_function():
    
    return {
        '1': simple_function1(),
        '2': simple_function2(),
        '3': db_get(id=3)
    }

if __name__ == '__main__': 
    simple_function1()
    # somewhere else
    db_set(1, 'foobar')
    # and again
    db_set(3, 'bazbar')
    invalidate('key')
    # ooops, we forgot something
    data = some_bigger_function()
    assert data['1'] == db_get(id=1), "this fails because we didn't manage to invalidate all the keys"
