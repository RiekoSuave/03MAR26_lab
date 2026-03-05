inventory = {}
sales = []

def main_menu():
        
    print ("\n=== inventory tracker===")

    print ("1.add product")

    print ("2.list inventory")

    print ("3.remove product")

    print ("4.exit")
    
def get_int(prompt, min_value = None):
    val = 0
    raw = input(prompt)
    
    val = int(raw)
    return val
  
def main():
    while True:
        main_menu()
        choice = get_int("choose an option", min_value = 1)
        
        if choice == 1:
            print ("this is choice 1.")
        elif choice == 2:
            print ("this is choice 2.")
        elif choice == 3:
            print ("this is choice 3.")
        elif choice == 4:
            print ("goodbye!")
            break
        else: 
            print("invalid option")
            
            
if __name__ == "__main__":
    main()
        