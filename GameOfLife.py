# Daniel McMurray
# CIS 125 Intro To CS
# GameOfLife.py
# Framework of the game
# Created in collaboration with Marisa Gross, Evan Sauers, and Jacob Wright

# Populate defines what is in the world.
def populate(world,h,w):
    dummy = 0
    print("Hey look, I'm populating!")

# Display shows the population in the world.
def display(world,h,w):
    dummy2 = 0
    print("Hey look, I'm displaying!")

# Generation updates the population and returns the next generation.
def generation(world,h,w):
    dummy3 = 0
    print("Hey look, I'm generating!")

# Main puts all of the functions together.
def main():
    import random
    height = 80
    width = 22
    world = []
    
    populate(world,height,width)
    
    x = (input("Please enter a key: "))
    while x != "Q":
    
        display(world,height,width)
        
        generation(world,height,width)
        
        x = input("Enter Q to quit: ")

main()