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

def some_bigger_function():
    db_set(1, 'something')
    value = simple_function1()
    db_set(2, 'something else')
    #### now we know we used 2 cached functions so....
    invalidate('key1')
    invalidate('key2')
    #### now we know we are safe, but for a price                  
    return simple_function2()

if __name__ == '__main__':  
    some_bigger_function()
