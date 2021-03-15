import random

is_playing = True
user_nums = []
drawn_nums = None

while is_playing:
    while len(user_nums) < 6:
        try:
            user_choice = (int(input(f'#{len(user_nums) + 1}: Enter your number in range 1-49: ')))
            if user_choice < 1 or user_choice > 49:
                print('Number out of range.')
                break
            else:
                pass

            if len(user_nums) > 0:
                if user_choice in user_nums:
                    print('Chosen numbers must be unique.')
                    break
                else:
                    pass

            user_nums.append(user_choice)
        except ValueError:
            print('Entered values must be whole numbers.')

    drawn_nums = (random.sample(range(50), 6))

    guessed = 0

    for user_num in user_nums:
        for drawn_num in drawn_nums:
            if user_num == drawn_num:
                guessed += 1

    print(f'You guessed {guessed} numbers')
    if len(user_nums) == 6:
        print(f'Your numbers: {user_nums}')
        print(f'Drawn numbers are: {drawn_nums}')

    user_nums.clear()
    drawn_nums.clear()

    for retry in range(5):
        rerun = str(input('Would you like to play again? (y/n) '))
        if rerun == str('y'):
            is_playing = True
            break
        elif rerun == str('n'):
            is_playing = False
            print('Thank you for playing! Bye bye.')
            break
        print('Please answer "y" for "yes" or "n" for "no".')
    else:
        print("You keep making invalid choices, exiting.")
        break
