def invalid_input(x):
    if (x!="y" or x!="n"):
        print("Invalid input. It should be either 'y' or 'n'")
        exit()


my_list=["Elephant", "Dolphin", "Penguin", "Tiger", "Eagle", "Frog", "Kangaroo", "Owl"]

print("Think of one of the following: ")
print(my_list, sep=", ")
print("----------------------------")

while True:
    answer=input("\nCan it live in water (y/n)? ")  
    # if yes: dolphin, penguin, frog
    # if no: elephant, tiger, eagle, kangaroo, owl
    if answer=='y':
        answer=input("Is it a mammal (y/n)? ")
        # if yes: dolphin
        # if no: penguin, frog
        if answer=='y':
            print("It must be a dolphin!")
            break
        elif answer=='n':
            answer=input("Is it a bird? (y/n)? ")
            # if yes: penguin
            # if no: frog
            if answer=='y':
                print("It must be a penguin!")
                break
            elif answer=='n':
                print("It must be a frog!")
                break
    elif answer=='n':
        answer=input("Is it a bird (y/n)? ")
        # if yes: eagle, owl
        # if no: elephant, tiger, kangaroo
        if answer=='y':
            answer=input("Is it more active in night (y/n)? ")
            # if yes: owl
            # if no: eagle
            if answer=='y':
                print("It must be an owl!")
                break
            elif answer=='n':
                print("It must be an eagle!")
                break
        elif answer=='n':
            answer=input("Does it jump around a lot while walking (y/n)? ")
            # if yes: kangaroo
            # if no: elephant, tiger
            if answer=='y':
                print("It must be a kangaroo!")
                break
            elif answer=='n':
                answer=input("Is it a carnivore (y/n)? ")
                # if yes: tiger
                # if no: elephant
                if answer=='y':
                    print("It must be a tiger!")
                    break
                elif answer=='n':
                    print("It must be an elephant!")
                    break
