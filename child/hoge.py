#from .grand_child import fuga
#from . import fuga as fuga
from .. import fuga as fuga

def hello():
    print("hello in child")

def hello2():
    print("hello2 in child")

def hello3():
    fuga.hello()