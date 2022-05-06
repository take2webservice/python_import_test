from .. import fuga as parent_fuga
from sys import path
print(path)

def hello():
    print("child.grand_child.fuga hello")
    parent_fuga.hello()