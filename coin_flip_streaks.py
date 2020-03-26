import random

#assign random values to all positions in random set
def flip(number):
    flip_list = []
    for i in range(int(number)):
        x = random.randint(0,1)
        if x == 0:
            flip_list.append('H')
        if x == 1:
            flip_list.append('T')
    return flip_list

# def streak_checker(obs_set):
#     for i in range(len(obs_set)):


print('Enter the size of your observation set:')
observation_number = input()
gen_list = flip(observation_number)
print(gen_list)
# streak_checker(gen_list)
