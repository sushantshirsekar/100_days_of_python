# ===============================================
# Script-Purpose : Implemented random coin toss
# using random function
# ===============================================

import random

random_coin_toss = random.randint(1,2)
print(random_coin_toss)
if random_coin_toss == 1:
    print("Heads")
else:
    print("Tails")
