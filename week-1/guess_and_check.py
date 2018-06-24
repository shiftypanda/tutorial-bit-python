# to cover learning about guessing and checking


def guess_and_check_cube_root():
    """Used to guess and check cube root"""
    x = int(input('Enter an integer: '))
    ans = 0
    while ans**3 < x:     # generates a guess
        ans = ans + 1
    if ans**3 != x:
        print(str(x) + ' is not a perfect cube')
    else:
        print('Cube root of ' + str(x) + ' is ' + str(ans))

guess_and_check_cube_root()