# this is a script to help a user memorize some text
import os
import random
import string

def main():

    original_string = str(input("Enter some text you would like help memorizing: "))
    words_list = original_string.split()

    omit = 1

    prompt_rec(omit, words_list, original_string)


def prompt_rec(n, lst, strng, dont_repeat=[]):

    # base case
    if n == len(lst) + 1:
        print("You have successfully written the original text from memory.")
        return 0 
    
    valid_index = False

    while not valid_index:

        index = random.randint(0, len(lst) - 1)
        if index not in dont_repeat:
            valid_index = True
    
    dont_repeat.append(index)


    for i in range(len(lst[index])):  # this loop replaces the letters of the word at the selected index with underscores

        if lst[index][i] not in string.punctuation:
            l = list(lst[index])  # turn the word into a list of characters
            l[i] = '_'  # change the later to an underscore
            lst[index] = ''.join(l)
 
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

    return prompt_rec(n+1, lst, strng, dont_repeat)

if __name__ == "__main__":
    main()
