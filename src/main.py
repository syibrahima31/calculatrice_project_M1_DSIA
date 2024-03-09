from controller import calculate

def run(): 
    while True:
        print("----MENU----")
        print("1. Addition ")
        print("2. Soustraction")
        print("3. Multiplication")
        print("4. Division")
        print("-: Quitter")

        op = input("Faites votre Choix : ").strip()

        if op not in "1234": 
            break 

        calculate(op )
        print("-"*50)



if __name__ == "__main__":
    run()