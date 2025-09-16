
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
        if height % 2 == 1:   
            break
        else:
            print("Enter an odd number!")
    except ValueError:
        print("Enter a number which is odd!")
# TODO: Draw the top half of the diamond
for i in range(1, height + 1, 2):
        spaces = (height - i) // 2
        if i == 1:
            print("" * spaces + "*")
        else:
            print("" * spaces + "" + " " * (i - 2) + "")

    # TODO: Draw the bottom half of the diamond
for i in range(height - 2, 0, -2):
        spaces = (height - i) // 2
        if i == 1:
            print("" * spaces + "*")
        else:
            print("" * spaces + "" + "" * (i - 2) + "")
# Uncomment to test Part 1
# draw_diamond()
