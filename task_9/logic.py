#define main function to take user input and give expected output
def main():
    str = input("Input: ")
    print(f"Output: {remove(str)}")

#remove vowels from the input create vowels as string and create an empty string to append
#letters after iterating and choosing the expected one
def remove(str):
    new_str = ""
    remove_str = "aAeEiIoOuU"
    for letter in str:
        if letter not in remove_str:
            new_str += letter
        # when use the return function in for loop you get output of first letter if it is consonant
        # if it is vowel you will get empty string
        # when you indent it outside of for loop it will finish to iterate over whole string and you will get the expected result       
    return new_str

main()