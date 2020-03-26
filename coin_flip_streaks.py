import random
total_streak = 0

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
    global total_streak
    current_streak = 1
    p_flip = None
    for flip in obs_set:
        if flip == p_flip:
            current_streak += 1
            if current_streak == 6:
                total_streak += 1
                continue
        else:
            current_streak = 1
        p_flip = flip
    x = total_streak
    return x

print('Enter the size of your observation set:')
observation_number = input()
gen_list = flip(observation_number)
print(gen_list)
number_streaks = streak_checker(gen_list)
print(number_streaks)
percent = int(number_streaks)/int(observation_number) * 100
print('chances of occurence of streak in a set of ' +observation_number+ ' samples is ' +str(percent) )