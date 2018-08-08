# What does it take to be a Python Expert?
# James Powel

# Meta Classes:

# user.py
from Lectures.meta_classes.library import Base

assert hasattr(Base,'foo'), 'you broke it, you fool!'  # this will warn if foo doesnt exist.

class Derived(Base):
    def bar(self):
        return 'bar'
