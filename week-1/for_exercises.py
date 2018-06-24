# for loop exercises end of week one


def for_loop_print_evens():
    """prints 2, 4, 6, 8, 10, Goodbye! using a for loop"""
    for counter in range(2, 11, 2):
        print(counter)

    print("Goodbye!")


# for_loop_print_evens()

def for_loop_hello_countdown_evens():
    """prints Hello!, 10, 8, 6, 4, 2"""
    print("Hello!")
    for counter in range(10, 1, -2):
        print(counter)


# for_loop_hello_countdown_evens()

def for_loop_sum_to_end(end):
    """sums numbers from 0 up to end"""
    final_number = 0
    for numbers in range(0, int(end+1)):
        final_number += numbers

    print(final_number)

for_loop_sum_to_end(end)