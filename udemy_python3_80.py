import random


print('Paper')
print('Rock')
print('Scissor')
l = ['Paper','Rock','Scissor']
print(f'choices: {l}')

pc =random.choice(l)

player = input(f'pick the the element (index from 0 to {len(l)-1})b:')
picked = l[int(player)]
if picked == pc:
    print("tie")
