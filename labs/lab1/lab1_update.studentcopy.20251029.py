# ==============================
# Main Program
# ==============================
def main():
    while True:
        print("Lab 1 - Python Basics")
        print("1. Draw Diamond")
        print("2. Text Analysis")
        print("3. Caesar Cipher")
        choice = input("Select part to run (1-3): ")
        
        if choice == "1":
            draw_diamond()
        elif choice == "2":
            text_analysis()
        elif choice == "3":
            caesar_cipher()
        else:
            exit()



"""
Lab 1 - Python Basics
Author: <Omer San>
Instructions: Complete each part below. Save your work and commit + sync in Codespaces.
"""

# ==============================
# Part 1: Draw a Diamond
# ==============================
# Ask the user for an odd positive number → this will be the diamond’s height.
# Keep asking until the input is valid (loop with error handling).
# Print the top half of the diamond: start with 1 star, then 3, 5… up to the middle row.
# Print the bottom half: go back down with 3 stars, then 1 star.
# Use spaces on the left to center the stars so the shape looks like a diamond.

def draw_diamond():
    """
    Ask the user for an odd number for the diamond height
    and print a symmetric diamond of that height.
    """
    
    print("you have some work todo!, draw_diamond")
    # TODO: Prompt user for an odd number
while True:
        try:
            height = int(input("Please enter an odd number for the diamond height: "))
            if height % 2 == 1:   # check odd
                break
            else:
                print("Enter an odd number!")
        except ValueError:
            print("Enter a number that is odd!")
# TODO: Draw the top half of the diamond
for i in range(1, height + 1, 2): 
        spaces = (height - i) // 2     
        if i == 1:                     
            print(" " * spaces + "*")
        else:                          
            print(" " * spaces + "*" + " " * (i - 2) + "*")
    # TODO: Draw the bottom half of the diamond
for i in range(height - 2, 0, -2):
        spaces = (height - i) // 2
        if i == 1:                     
            print(" " * spaces + "*")
        else:                          
            print(" " * spaces + "*" + " " * (i - 2) + "*")
# Uncomment to test Part 1
# draw_diamond()


# ==============================
# Part 2: Count Letters, Words, and Sentences
# ==============================
# Ask the user to enter some text (must include at least one letter).
# Count letters → go through each character, only add to count if it’s A–Z or a–z.
# Count words → use split() to break text by spaces and measure length.
# Count sentences → look for punctuation marks ., ?, or !.
# Print the totals: letters, words, and sentences.

def text_analysis():
    """
    Ask the user for a block of text.
    Count and display:
        - Number of letters (only count a-zA-Z)
        - Number of words   (use split())
        - Number of sentences (., ?, !) 
    """

    print("you have some work todo!, text_analysis")
  # TODO: Get user input


'''
##############let's examine theis block##########################################  
while True:
        text = input("Enter some text: ")
        has_letter = False
        for letter in text:
            if letter.isalpha():
                has_letter = True
                break
        if has_letter:
            break
        else:
            print("Type only enter letters not numbers")   
    # TODO: Count letters
#############################################################
    
none of this really makes sense:

has_letter = False
        for letter in text:
            if letter.isalpha():
                has_letter = True
                break
        if has_letter:
            break
        else:
            print("Type only enter letters not numbers")   


1) the user enters some text. You then check if the first character in text
   is alpha, if it is you break oput of the while loop.  None of that is needed

all you need is:

text = input("Enter some text: ")



'''
text = input("Enter some text: ")


'''
###############let's examine this block####################################
letters = 0
for letter in text:
        if letter.isalpha():
            letters += 1   
    # TODO: Count words
words = len(text.split())
     # TODO: Count sentences
sentences = 0
for letter in text:
        if letter in ".!?":
            sentences += 1
#######################################################################
1) we canh do this in 1 loop

words = len(text.split())
sentences = 0
letters = 0
for letter in text:
    if letter.isalpha():
        letters += 1   

    elif letter in ".!?":
        sentences += 1
'''
words = len(text.split())
sentences = 0
letters = 0
for letter in text:
    if letter.isalpha():
        letters += 1   

    elif letter in ".!?":
        sentences += 1


# display results    
    # TODO: Print the results
print(f"Letters: {letters}")
print(f"Words: {words}")        # replace 0
print(f"Sentences: {sentences}")    # replace 0   

# Uncomment to test Part 2
# text_analysis()


# ==============================
# Part 3: Caesar Cipher – Encrypt and Decrypt
# ==============================
# Ask the user to type in some text (must include at least one letter).
# Ask the user for a shift number (integer).
# Ask if they want to encrypt (shift forward) or decrypt (shift backward).
# Go through each character in the text:
# If it’s a letter → shift it in the alphabet (wrap around if needed).
# Keep uppercase and lowercase letters as they are.
# Leave numbers, spaces, and punctuation unchanged.
# Print the original text and the new result (encrypted or decrypted).

def caesar_cipher():
    """
    Ask the user for text and a shift value.
    Provide options to encrypt or decrypt the text using a Caesar cipher.
    """

    print("you have some work todo!, caesar_cypher")

# loop until user enters text with at least one letter    
    # TODO: Get user input text
while True:
        text = input("Enter some text: ")
        has_letter = False
        for letter in text:
            if letter.isalpha():
                has_letter = True
                break
        if has_letter:
            break
        else:
            print("Follow directions, enter text:")
    # TODO: Get shift value
while True:
        try:
            shift = int(input("Please enter an integer shift, an integer shift is you shift each letter forward by the number specified by the shift integer: "))
            break
        except ValueError:
            print("Follow directions and enter a number!")
    # TODO: Ask user whether to encrypt or decrypt
while True:
        choice = input("Type 'e' to encrypt or 'd' to decrypt, to encrypt a message, you shift each letter forward by the number specified by the shift integer, and decrypt is the backward shift : ").lower()
        if choice in ("e", "d"):
            break
        else:
            print("Follow directions please, enter 'e' or 'd'!")
if choice == "d": 
        shift = -shift      
    # TODO: Implement encryption and decryption logic
result = ""
for letter in text:
        if letter.isalpha():
            if letter.isupper():
                base = ord("A")
                result += chr((ord(letter) - base + shift) % 26 + base)
            else:
                base = ord("a")
                result += chr((ord(letter) - base + shift) % 26 + base)
        else:
            result += letter  
    # TODO: Print the final result
print("Original:", text)
print("Result:  ", result)

# Uncomment to test Part 3
caesar_cipher()

if __name__ == "__main__":
    main()