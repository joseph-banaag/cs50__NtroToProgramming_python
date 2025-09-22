# PYTHON LIBRARY MODULES:
import random # this import will help the random.+any module eg. random.choice to work.
from random import choice # this will help the choice module work without the random library

coin = random.choice(["heads", "tails"])
# print(coin)

coin_2 = choice(["heads", "tails"])
# print(coin_2)

random_numb = random.randint(1,9)
# print(random_numb)

shuffle_list = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(shuffle_list)
print(shuffle_list) #this will print the exact list in shuffle horizontally or by default.
for numb in shuffle_list:
    print(numb) #this will print the items on the list vertically

