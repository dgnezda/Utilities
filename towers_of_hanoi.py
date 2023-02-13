from stack3 import Stack


print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []
l_stack = Stack("Left")
m_stack = Stack("Middle")
r_stack = Stack("Right")
stacks.append(l_stack)
stacks.append(m_stack)
stacks.append(r_stack)


#Set up the Game
num_disks = int(input("\nHow many disks do you want to play with?\n"))

while num_disks < 3:
    num_disks = int(input("Enter a number greater than or equal to 3\n"))

for n in range(num_disks, 0, -1):
    l_stack.push(n)

num_optimal_moves = 2**num_disks - 1

print(f"The fastest you can solve this game is in {num_optimal_moves} moves.")


#Get User Input
def get_input():
    choices = [x.get_name()[0] for x in stacks]
  
    while True:
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print(f"Enter {letter} for {name}.")
        
        user_input = input("").upper()
        
        if user_input in choices:
            for i in range(len(stacks)):
                if user_input == choices[i]:
                    return stacks[i]


#Play the Game
num_user_moves = 0

while r_stack.get_size() != num_disks:
    print("\n\n\n...Current Stacks...")
      
    for s in stacks:
        s.print_items()
      
    while True:
        print("\nWhich stack do you want to move from?\n")
        from_stack = get_input()
        print("\nWhich stack do you want to move to?\n")
        to_stack = get_input()

        if from_stack.is_empty():
            print('\n\nInvalid Move. Try Again')
        elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            break
        else:
            print('\n\nInvalid Move. Try Again')


print(f"\n\nYou completed the game in {num_user_moves} moves, and the optimal number of moves is {num_optimal_moves}")