inventory = []

def run(id):
    print("=========================================")
    print("Inventory:")
    if len(inventory) == 0:
        print("Empty")
    else:
        for item in inventory:
            print(item)
    print("=========================================")
    if id == 0:
        print("You find yourself in a concrete room, what do you do?\n1. Look around (Forwards)\n2. Look around (To the Right)\n3. Look around (To the Left)\n4. Look around (Backwards)")
        Input = int(input("~ "))
        run(Input)
    elif id == 1:
        print("You look forwards and see a concrete wall with a window with bars. You also notice a sink, what do you do?\n1. Go back.\n2. Look at the window.\n3. Look out of the window.\n4. Look at the sink.")
        Input = int(input("~ "))
        run(0) if Input == 1 else run(Input + 3)
    elif id == 2:
        print("You look to the right and notice a wooden slab hanging rom the wall by some iron chains. The slap has a matress, only a few centimeters thick. What do you do?\n1. Go back.\n2. Look under the matress.\n3. Look under the \"bed\".")
        Input = input("~ ")
        if Input == "1":
            run(0)
        elif Input == "2":
            run(10)
        else:
            run(11)
    elif id == 3:
        print("You look to the left and see a shelf with books. You notice that one of the books is a little bit out of place. What do you do?\n1. Go back.\n2. Look at the shelf.\n3. Look at the book.")
        Input = input("~ ")
        if Input == "1":
            run(0)
        elif Input == "2":
            run(12)
        else:
            run(13)
    elif id == 4:
        print("You look backwards and see a door. You notice that it is locked. What do you do?\n1. Go back.\n2. Look at the door.")
        Input = input("~ ")
        run(0) if Input == "1" else run(14)
    elif id == 5:
        print("You look at the window, the bars are too thick to ever cut through.")
        run(1)
    elif id == 6:
        print("You look out the window, and see that there are more buildings that appear to be the same as the one you are in. In the distance you can see a barb wire fence and a lookout tower.")
        run(1)
    elif id == 7:
        print("You look at the sink, you notice it drip every 2-3 seconds. You also notice a little mirror on the side. What do you do?\n1. Go back.\n2. Look under the sink.")
        Input = int(input("~ "))
        run(1) if Input == "1" else run(8)
    elif id == 8:
        print("You notice a loose tile and take it off the wall. It reveals a tunnel. What do you do?\n1. Go back.\n2. Go through it.")
        Input = int(input("~ "))
        run(1) if Input == "1" else run(9)
    elif id == 9:
        print("You go through the tunnel and after what seemed like an eternity, you reach the end.")
    elif id == 10:
        print("You look under the mattress and find a key and take it.")
        inventory.append("Key #1")
        run(2)
    elif id == 11:
        print("You look under the bed, but the only thing you find is a dead mouse.")
        run(2)
    elif id == 12:
        print("You look at the shelf, and notice that there are a lot of books about the history of the prison. You also notice that one of the books is a little bit out of place. What do you do?\n1. Go back.\n2. Look at the book.")
        Input = int(input("~ "))
        run(1) if Input == "1" else run(13)
    elif id == 13:
        print("You look at the book, and notice that it is a little bit out of place. You take it out and find a key inside. You take it.")
        inventory.append("Key #2")
        run(3)
    elif id == 14:
        print("You look at the door, and notice that it is locked. You also notice a keyhole. What do you do?\n1. Go back.\n2. Try to open the door with the key.")
        Input = int(input("~ "))
        run(0) if Input == "1" else run(15)
    elif id == 15:
        if "Key #1" in inventory:
            print("The key fits and you open the door. You find yourself in a corridor. What do you do?\n1. Go back.\n2. Go to the left.\n3. Go to the right.")
            Input = int(input("~ "))
            run(0) if Input == 1 else run(16) if Input == 2 else run(17)
        elif "Key #2" in inventory and "Key #1" not in inventory:
            print("The key doesn't fit, you need to find another key.")
            run(14)
        else:
            print("The door is locked, you need to find a key.")
            run(14)
    elif id == 16:
        print("You go left but reach a dead end. You turn around and go back.")
        run(15)
    elif id == 17:
        print("You go right and find a door. You notice that it is locked. What do you do?\n1. Go back.\n2. Try to open the door with the key.")
        Input = int(input("~ "))
        run(0) if Input == 1 else run(18)
    elif id == 18:
        if "Key #2" in inventory:
            print("The key fits and you open the door. You made it out!")
    else:
        print("Error occured, sending home...")
        run(0)

run(0)

print("You win! You escaped the prison!!!")