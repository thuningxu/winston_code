print('Print a Flagpole!')
while True:
    def print_flag(n):
        # print the flag
        diagonal = n
        flagpole = n * 2 - 1
        number_of_stars = 0
        for x in range(n):
            number_of_stars += 1
            for x in range(number_of_stars):
                print('*', end = '')
            print()

        for x in range(n - 1):
            print('*')
    number = input('What is the number?')
    number = int(number)
    print_flag(number)

##*
##**
##***
##****
##*****
##*
##*
##*
##*
