"""Test the Task data type."""
from collections import namedtuple

Task = namedtuple('Task',['summary','owner','done','id'])
Task.__new__.__defaults__ = (None,None,False,None)

def test_defaults():
   """Using no parameters should invoke defaults."""
   t1 = Task()
   t2 = Task(None, None, False, None)
   assert t1 == t2

def test_member_access():
   """Check .field functionality of namedtuple."""

   t = Task('buy milk', 'brian')
   assert t.summary == 'buy milk'
   assert t.owner == 'brian'
   assert (t.done,t.id) == (False,None)

def test_asdict():
    """_asdict() should return a dictionary."""
    task = Task('do something', 'tokken', True, 21)
    dict = task._asdict()
    expected = {
        'summary': 'do something',
        'owner': 'tokken',
        'done': True,
        'id': 21
    }
    assert dict == expected

def test_replace():
    """replace() should change passed in fields."""

    task = Task('finish book', 'brian', False)
    task = task._replace(done=True)
    expected = Task('finish book', 'brian', True)

    assert task == expected