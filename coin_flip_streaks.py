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

def streak_checker(obs_set):
    x = 0
    for i in range(len(obs_set)):
        if obs_set[i]== obs_set[i+1]:
            if obs_set[i+1] == obs_set[i+2]:
                if obs_set[i+2] == obs_set[i+3]:
                    if obs_set[i+3] == obs_set[i+4]:
                        if obs_set[i+4] == obs_set[i+5]:
                            print('its a streak')
                            x = x+1
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            else:
                continue
        else:
            continue
    return x



print('Enter the size of your observation set:')
observation_number = input()
gen_list = flip(observation_number)
print(gen_list)
number_streaks = streak_checker(gen_list)
print(number_streaks)
