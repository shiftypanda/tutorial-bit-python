# function that creates a while loop and prints out a sequence



def even_printing():
    """prints out 2,4,6,8,10, Goodbye"""
    count = 2
    while count <= 10:
        if count % 2 == 0:
            print(count)
        count += 1
    print("Goodbye!")


def hello_countdown_evens():
    """prints Hello!, 10, 8, 6, 4, 2"""
    count = 10
    print("Hello!")
    while count >= 2:
        if count % 2 == 0:
            print(count)
        count -= 1



def sum_given_sequence_to_end(end):
    """sums a given sequence of number starting from 0 until reaches end"""
    final_sum = 0
    iterator = 0
    while iterator <= end:
        final_sum += iterator
        iterator += 1
    print(final_sum)

sum_given_sequence_to_end(end)
