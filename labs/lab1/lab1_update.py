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
def draw_diamond():
    """
    Ask the user for an odd number for the diamond height
    and print a symmetric diamond of that height.
    """
    
    print("you have some work todo!, draw_diamond")

    # TODO: Prompt user for an odd number
while True:
    try:
        height = int(input("Enter an odd number for the diamond height: "))
        if height % 2 == 1:   
            break
        else:
            print("Enter an odd number")
    except ValueError:
        print("Make sure to enter an odd number")
    # TODO: Draw the top half of the diamond
for i in range(1, height + 1, 2):
        spaces = (height - i) // 2
        print(" " * spaces + "*" * i)

    # TODO: Draw the bottom half of the diamond
for i in range(height - 2, 0, -2):
        spaces = (height - i) // 2
        print(" " * spaces + "*" * i)

# Uncomment to test Part 1
# draw_diamond()


# ==============================
# Part 2: Count Letters, Words, and Sentences
# ==============================
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
            print("Enter letters, not numbers")
    # TODO: Count letters
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
    # TODO: Print the results
print(f"Letters: {letters}")
print(f"Words: {words}")        
print(f"Sentences: {sentences}")    

# Uncomment to test Part 2
# text_analysis()


# ==============================
# Part 3: Caesar Cipher – Encrypt and Decrypt
# ==============================
def caesar_cipher():
    """
    Ask the user for text and a shift value.
    Provide options to encrypt or decrypt the text using a Caesar cipher.
    """

    print("you have some work todo!, caesar_cypher")

    # TODO: Get user input text
    text = input("Enter text: ")

    # TODO: Get shift value
    shift = int(input("Enter shift value (integer): "))

    # TODO: Ask user whether to encrypt or decrypt
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()

    # TODO: Implement encryption and decryption logic
    result = ""

    # TODO: Print the final result
    print("Result:", result)

# Uncomment to test Part 3
# caesar_cipher()




if __name__ == "__main__":
    main()