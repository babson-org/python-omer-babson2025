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