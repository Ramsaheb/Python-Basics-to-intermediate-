import pickle

# f = open('pickled.txt', 'wb')
# dct = {'name':'ram', 'age': 19, 'gender':'male', 'marks':75}
# pickle.dump(dct, f)
# f.close()

# f = open('pickled.txt', 'rb')
# d = pickle.load(f)
# print(d)
# f.close()

# from pickle import dumps, loads

# dct = {'name':'ram', 'age': 19, 'gender':'male', 'marks':75}

# dctstring = dumps(dct)
# print(dctstring)


# dct = loads(dctstring)
# print(dct)
def storedata():
    ram = {'name':'ram', 'age': 19, 'gender':'male', 'marks':75}
    raaam = {'name':'ram', 'age': 19, 'gender':'male', 'marks':75}

    db = {}
    db['ram'] = ram
    db['raaam'] = raaam

    dbfile = open('examplePickle.db', 'ab')

    pickle.dump(db, dbfile)

    dbfile.close()


def loaddata():
    dbfile = open('examplePickle.db', 'rb')

    db = pickle.load(dbfile)
    for key in db:
        print(key, '==>', db[key])
    dbfile.close()


storedata()
loaddata()