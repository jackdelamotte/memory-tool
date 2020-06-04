# this is a script to help a user memorize some text
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

    
    for i in range(n):

        index = random.randint(0, len(lst) - 1)

        lst[index] = '_' * len(lst[index])

 
    attempt = ''

    while(attempt != strng):

        # to clear the console
        count = 0
        while (count < 50):
            print()
            count += 1

        print(" ".join(lst))

        attempt = input("using the partial text above, type the original text, then press enter: ")
        print()

    return prompt_rec(n+1, lst, strng)

if __name__ == "__main__":
    main()
