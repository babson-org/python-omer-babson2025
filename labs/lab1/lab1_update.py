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
# The program asks the user for a number, but it has to be odd and positive. 
# If the user types something wrong, it gently asks again until the input is valid.
# Once we have the height, the code first builds the top half of the diamond, starting with 1 star in the middle, then 3, then 5, and so on, always centering them with spaces.
# After reaching the widest row (the middle of the diamond), the code switches to the bottom half, shrinking the rows back down: 3 stars, then 1 star.
# The little formula (height - i) // 2 just figures out how many spaces to put on the left so the stars line up in the center.
def draw_diamond():
    """
    Ask the user for an odd number for the diamond height
    and print a symmetric diamond of that height.
    """
    
    print("you have some work todo!, draw_diamond")
# keep prompting until user enters a valid odd integer
    # TODO: Prompt user for an odd number
while True:
    try:
        height = int(input("Enter an odd number for the diamond height: "))
        if height > 0 and height % 2 == 1:   
            break
        else:
            print("Enter an odd number")
    except ValueError:
        print("Make sure to enter an odd number")

# print top half of diamond (including middle row)
    # TODO: Draw the top half of the diamond
for i in range(1, height + 1, 2):
        spaces = (height - i) // 2
        print(" " * spaces + "*" * i)

# print bottom half of diamond
    # TODO: Draw the bottom half of the diamond
for i in range(height - 2, 0, -2):
        spaces = (height - i) // 2
        print(" " * spaces + "*" * i)

# Uncomment to test Part 1
# draw_diamond()


# ==============================
# Part 2: Count Letters, Words, and Sentences
# ==============================
#The program asks the user to type in some text. 
# If the user only types numbers or symbols, it keeps asking until there’s at least one real letter.
# Once it has the text, it goes through each character and counts only the letters (ignoring numbers, spaces, and punctuation).
# To get the word count, it uses Python’s split() function, which separates the text at spaces and counts how many pieces there are.
# To find the sentence count, it checks for punctuation marks that usually end sentences (., ?, !) and adds them up.
# Finally, it neatly prints out all three numbers: how many letters, how many words, and how many sentences were found in the input.
def text_analysis():
    """
    Ask the user for a block of text.
    Count and display:
        - Number of letters (only count a-zA-Z)
        - Number of words   (use split())
        - Number of sentences (., ?, !) 
    """

    print("you have some work todo!, text_analysis")

# loop until user enters text that includes at least one letter    
    # TODO: Get user input

while True:
        text = input("Enter some text: ")
        has_letter = any(ch.isalpha() for ch in text)
        if has_letter:
            break
        else:
            print("Enter letters, not just numbers/punctuation.")

# count alphabetic characters only    
    # TODO: Count letters
letters = 0
for letter in text:
        if letter.isalpha():
            letters += 1

# split text on spaces to count words    
    # TODO: Count words
words = len(text.split())

# count punctuation marks that end sentences    
    # TODO: Count sentences
sentences = 0
for letter in text:
        if letter in ".!?":
            sentences += 1

# display results    
    # TODO: Print the results
print(f"Letters: {letters}")
print(f"Words: {words}")        
print(f"Sentences: {sentences}")    

# Uncomment to test Part 2
# text_analysis()


# ==============================
# Part 3: Caesar Cipher – Encrypt and Decrypt
# ==============================
# The program first asks the user to type in some text. It makes sure the text contains at least one real letter (so you can’t just enter numbers or symbols).
# Next, it asks the user for a shift value — this is the number of positions each letter will be moved in the alphabet. 
# Then, the program asks whether you want to encrypt (hide the message) or decrypt (bring it back to normal). If decrypt is chosen, the shift is flipped to work backwards.
# The code goes through the text one character at a time:
# If the character is a letter, it shifts it forward or backward in the alphabet.
# Uppercase and lowercase letters are handled separately so the case is preserved.
# Non-letters (spaces, punctuation, numbers) are left exactly the same.
# Finally, it prints both the original message and the resulting transformed text so you can compare them.
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
        if any(ch.isalpha() for ch in text):
            break
        else:
            print("Enter text with letters:")

# validate numeric shift input
    # TODO: Get shift value
while True:
        try:
            shift = int(input("Please enter an integer shift: "))
            break
        except ValueError:
            print("Enter a number!")
    
# validate choice (encrypt or decrypt)
    # TODO: Ask user whether to encrypt or decrypt
while True:
        choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
        if choice in ("e", "d"):
            break
        else:
            print("Follow directions, enter 'e' or 'd'!")
# if decrypt, invert the shift
if choice == "d":
        shift = -shift   
    
# build the result string character by character   
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

# show original and transformed text    
    # TODO: Print the final result
print("Original:", text)
print("Result:  ", result)

# Uncomment to test Part 3
caesar_cipher()

if __name__ == "__main__":
    main()