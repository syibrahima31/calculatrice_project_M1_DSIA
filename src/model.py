def add(x:float, y:float) -> float: 
    """
        - arguments : 
            x : premier argument 
            y : deuxieme argument 
        - return: 
            float le resultat 
    """
    return x + y 

def sub(x:float, y:float) -> float: 
    """
        - arguments : 
            x : premier argument 
            y : deuxieme argument 
        - return: 
            float le resultat 
    """
    return x - y 

def mult(x:float, y:float) -> float: 
    """
        - arguments : 
            x : premier argument 
            y : deuxieme argument 
        - return: 
            float le resultat 
    """
    return x * y 


def div(x:float, y:float) -> float: 
    """
        - arguments : 
            x : premier argument 
            y : deuxieme argument  non nul 
        - return: 
            float le resultat 
    """
    if y==0: 
        raise ZeroDivisionError("On ne divise pas par zero")
    return x / y 


if __name__ == "__main__":
    try: 
        print(div(1, 0))
    except ZeroDivisionError as e: 
        print(e)