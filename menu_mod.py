import sys
#  function to display menu options and get user input
def menu_options():
    running = True
    while running:
        # promptuser for oprion
        print("Choose option from list")
        # list to store menu options 
        menu_items = ["1 : Run", "2 : Quit"]
         # print menu options
        for i in menu_items:
            print("{}".format(i))
             
        choice = input("Enter choice: ")
        if choice == "1":
            print("\nRunning Program...\n")
            #break
            running = False
    
        elif choice == "2":
            print("\nExiting now:(")
            sys.exit("Bye")
     
     
def main():
    menu_options()
            

if __name__ == '__main__':
    main()