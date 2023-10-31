# Eric Ly
def encoder(old): # encoder function
    new = ''
    old = str(old)
    for num in old:
        num = int(num)
        if num <= 6:
            num += 3
            new += str(num)
        elif num > 6: # situations where adding three will push back to start
            if num == 7:
                new += '0'
            elif num == 8:
                new += '1'
            elif num == 9:
                new +='2'
    print('Your password has been encoded and stored!')
    print('')


def main(): # main function
    while True:
        print('Menu') # creating the menu
        print('-------------')
        print('1. Encoder')
        print('2. Decoder')
        print('3. Quit')
        selection = int(input('Please enter an option: '))

        if selection == 1: # option 1
            password = input('Please enter your password to encode: ')
            if len(password) == 8:
                encoder(int(password))
            else:
                print('Sorry, password must be an 8-digit integer number.')
        elif selection== 3: # option 3
            quit()
        elif selection == 0 or selection >3: # restricting options
            print('Sorry, option must be between 1 and 3.')


if __name__ == '__main__':
    main()