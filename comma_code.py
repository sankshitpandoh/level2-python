import sys
def comma_fun(list_value):
    length = len(list_value)
    if length >1:
        print('here are the items of your list')
        print('\'', end='')
        for i in range(length - 1):
            print(list_value[i]+', ', end='')
        print('and ', end='')
        print(list_value[-1], end='')
        print('\'')
    elif length == 1:
        print('\'' +list_value[length - 1]+ '\'')
    else:
        print('you have an empty list')

user_list = []
while True:
    print('Enter items in your list:')
    single_item = input()
    if single_item == '':
        comma_fun(user_list)
        sys.exit()
    else:    
        user_list.append(single_item)
        
    
