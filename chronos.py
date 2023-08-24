import time
while True:
    print('##### Welcome to the chronospace! #####')
    time.sleep(3)
    print('\n')
    print('Here we have the best prices in the league community!')
    print('\n')
    loginid = input('Type your discord username: ')
    print('\n')
    print(f'Please {loginid}, select your option: ')
    print('1 - ELOJOB ')
    print('2 - DUOBOOST')
    print('3 - SMURF ACCOUNTS')
    print('4 - NFA ACCOUNTS')
    print('5 - COACHING')
    print('6 - EXIT')

    answ = int(input())

    if answ == 1:
        print('Please type the role that you want to see in your history: ')
        answer1 = input().lower()
        if answer1 == 'top' or answer1 == 'jg' or answer1 == 'jungle' or answer1 == 'mid' or answer1 == 'adc' or answer1 == 'sup':
            print('Alright, the booster has been contacted. You will soon receive a friend request from him.')
            break
        else:
            print('Invalid command!')
            continue

    elif answ == 2:
        print('Please type your elo/rank that you are and the elo that you want to be: ')
        eloansw = input('Type your elo: ').lower()
        elowishansw = input('Type the elo that you want to reach: ').lower()
        if eloansw == 'iron' or eloansw == 'bronze' or eloansw == 'silver' or eloansw == 'gold' or eloansw == 'platinum' or eloansw == 'emerald' and elowishansw == 'iron' or elowishansw == 'bronze' or elowishansw == 'silver' or elowishansw == 'gold' or elowishansw == 'platinum' or elowishansw == 'emerald' or elowishansw == 'diamond':
            print('Your booster will call you soon, please keep your eyes on your friend requests!')
            break
        else:
            print('Booster unnavailable/invalid command!')
            continue

    elif answ == 3:
        print('An admin/mod has been called, please wait.')
        break
    
    elif answ == 4:
        print('An admin/mod has been called, please wait.')
        break

    elif answ == 5:
        coachansw = input('please type your main role: ')
        if coachansw == 'top' or coachansw == 'jg' or coachansw == 'jungle' or coachansw == 'mid' or coachansw == 'adc' or coachansw == 'sup':
            print('Your coach has been called, please wait and keep your eyes on your friend requests!')
            break
        else:
            print('Invalid command!')
            continue
    
    elif answ == 6:
        exitansw = input('Want to exit? Y/N').upper()
        if exitansw == 'Y':
            break
        elif exitansw == 'N':
            continue
        else:
            print('Invalid command!')
            continue