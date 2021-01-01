import database

class TestClass(object):

    db = database.create_db('./tests')

    def test_createdb(self):
        x = database.create_db('./x')
        assert x is not None

    def test_load(self):
        x = self.db.load_db()
        assert x is True

    def test_commit(self):
        self.db.load_db()
        self.db.write('key', 'value')
        x = self.db.commit()
        assert x is True

    def test_write(self):
        self.db.load_db()
        self.db.write('key3', 'value3')
        self.db.commit()
        x = self.db.read_by_key('key3')
        assert x == 'value3'

    def test_read(self):
        self.db.load_db()
        self.db.write('key2', 'value2')
        self.db.commit()
        x = self.db.read_by_key('key2')
        assert x == 'value2'

    def test_delete(self):
        self.db.load_db()
        self.db.write('key1', 'value1')
        self.db.delete_by_key('key1')
        self.db.commit()
        x = self.db.read_by_key('key1')
        assert x is False

if __name__ == "__main__":
    tests = TestClass()
    test_methods = [method for method in dir(tests) if callable(getattr(tests, method)) if method.startswith('test_')]
    for method in test_methods:
        getattr(tests, method)()
        print(".", end="")
