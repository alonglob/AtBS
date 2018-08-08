# What does it take to be a Python Expert?
# James Powel

# Context Manager
'''
this is an example for a Context Manager, but is already available at the context-library imported below.

class ContextManager:
    def __init__(self, gen):  # when created asks for a generator
        self.gen = gen
    def __call__(self, *args, **kwargs):  # when called expect arguments to be passed
        self.args, self.kwargs = args, kwargs
        return self
    def __enter__(self):  # when entered create a instance of the generator with the args passed with call
        self.gen_inst = self.gen(*self.args, **self.kwargs)
        next(self.gen_inst)  # call the first generated object
    def __exit__(self, exc_type, exc_val, exc_tb):  # when exiting the ctx_manager call this:
        next(self.gen_inst, None)  # calls the next generator object, closing the table.
'''


from sqlite3 import connect
from contextlib import contextmanager


@contextmanager
def temptable(cur):
    print('created table')
    cur.execute('create table points(x int, y int)')  # first object generated, creates the table
    try:
        yield
    finally:
        print('dropped table')
        cur.execute('drop table points')  # second and final object generated, drops the table.


with connect('test.db') as conn:
    cur = conn.cursor()
    with temptable(cur):
        cur.execute('insert into points (x, y) values(1, 1)')
        cur.execute('insert into points (x, y) values(2, 1)')
        cur.execute('insert into points (x, y) values(1, 2)')
        for row in cur.execute('select x, y from points'):
            print(row)



