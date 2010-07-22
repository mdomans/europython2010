db = {
    1 : "foo",
    2 : "bar",    
    0 : "default",
}


def db_get(id = 0):
    return db[id]

def db_set(id, value):
    db[id] = value