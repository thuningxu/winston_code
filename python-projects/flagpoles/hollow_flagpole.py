print('Print a Flagpole!')
def print_flag(n):
    # print the flag
    spaces = 0
    number_of_stars = 0
    for x in range(n):
        number_of_stars += 1
        spaces = number_of_stars - 2
        if number_of_stars == 1:
            print('*')
        elif number_of_stars == 2:
            print('*',  end = '')
            print('*')
        elif number_of_stars == n:
            for x in range(n - 1):
                print('*', end = '')
            print('*')
        else:
            print('*', end = '')
            for x in range(spaces):
                print(' ', end = '')
            print('*')

    for x in range(n - 1):
        print('*')


def print_flag_daddy(n):
    for x in range(n):
        if x == 0 or x == n-1:
            for y in range(x+1):
                print('*' , end = '')
            print()
        else:
            print('*', end = '')
            for y in range(x-1):
                print(' ' , end = '')
            print('*')

    for x in range(n - 1):
        print('*')

def print_flag_daddy2(n):
    for x in range(n):
        print('*', end = '')
        for y in range(x-1):
            if x == n-1:
                print('*' , end = '')
            else:
                print(' ' , end = '')
        if x != 0:
            print('*')
        else:
            print()

    for x in range(n - 1):
        print('*')

number = input('What is the number?')
number = int(number)
print_flag(number)
print()
print_flag_daddy(number)
print()
print_flag_daddy2(number)
#*
#**
#* *
#*  *
#*****
#*
#*
#*
#*
