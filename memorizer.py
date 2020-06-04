# this is a script to help a user memorize some text
import os
import random

def main():

    original_string = str(input("Enter some text you would like help memorizing: "))
    words_list = original_string.split()

    omit = 1

    print("made it here")
    prompt_rec(omit, words_list, original_string)


def prompt_rec(n, lst, strng):

    # base case
    if n == len(lst):
        print("You have successfully written the original text from memory.")
        return 0

    
    dont_repeat = []  # a list to hold already used indexes so they don't get repeated

    for i in range(n):

        # this loop picks a random word in the string to replace with underscores.
        # the loop is necessary to not choose an index that has already been used 
    
        valid_index = False

        while not valid_index:

            index = random.randint(0, len(lst) - 1)
            if index not in dont_repeat:
                valid_index = True

        dont_repeat.append(index)
        lst[index] = '_' * len(lst[index])

 
    attempt = ''  # this string will hold the users attempt to retype the original text
    attempt_count = 0  # use to print "try again" message for repeat attempts

    while(attempt != strng):
 
        os.system('cls' if os.name == 'nt' else 'clear')  # clear the console

        if attempt_count > 0:
            print("That wasn't quite right. Try again: ")
            print()
        attempt_count += 1

        print(" ".join(lst))

        attempt = input("using the partial text above, type the original text, then press enter: ")
        print()

    return prompt_rec(n+1, lst, strng)

if __name__ == "__main__":
    main()
