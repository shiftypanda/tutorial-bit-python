# to cover learning about guessing and checking
# exhaustive enumeration example


def guess_and_check_cube_root():
    """Used to guess and check cube root"""
    x = int(input('Enter an integer: '))
    ans = 0
    while ans**3 < abs(x):     # generates a guess
        ans = ans + 1
    if ans**3 != abs(x):
        print(str(x) + ' is not a perfect cube')
    else:
        if x < 0:
            ans = - ans
        print('Cube root of ' + str(x) + ' is ' + str(ans))

# guess_and_check_cube_root()

# cleaner guess and check method


def guess_and_check_cube_root_for_loop():
    cube = 8
    for guess in range(cube+1):
        if guess**3 == cube:
            print("Cube root of", cube, "is", guess)


#guess_and_check_cube_root_for_loop()


def guess_and_check_cube_root_for_loop_absolute():
    cube = -27
    for guess in range(abs(cube) + 1):
        if guess**3 >= abs(cube):
            break
    if guess ** 3 != abs(cube):
        print(cube, 'is not a perfect cube')
    else:
        if cube < 0:
            guess = -guess
        print("Cube root of", str(cube), "is", str(guess))

guess_and_check_cube_root_for_loop_absolute()