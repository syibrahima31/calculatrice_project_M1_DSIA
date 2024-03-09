from model import * 
from view import  *

def calculate(op): 
    x = float(get_number())
    y = float(get_number())

    if op == '1': 
        result = add(x, y)
    elif op =='2':
        result = sub(x, y)
    elif op == '3': 
        result = mult(x, y)
    elif op == '4': 
        result = div(x, y)

    affiche_result(result)