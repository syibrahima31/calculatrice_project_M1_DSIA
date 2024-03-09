import sys
import os 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.model import add, sub, mult, div

def test_add(): 
    assert add(1, 3) == 4 
    assert add(2, 3) == 5 

def test_mult(): 
    assert mult(2, 3) == 6