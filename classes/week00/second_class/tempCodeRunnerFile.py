import utils as ut
import basic_update as bs
def myProgram_3():
    ut.clear_screen()

    while True:
        print("5 to start")
        print("6 to stop")

        txt = "Enter 5 or 6: "
        while True:
            try:
                choice = int(input(txt))
                break
            except ValueError:
                txt = "Try again, enter 5 or 6: "

        if choice == 5:
            start()
            bs.run_basic()  # Call a function from another module
        elif choice == 6:
            stop()
            print("__name__ in this script:", __name__)
        else:
            print("Exiting menu...")
            break

if __name__ == "__main__":
    myProgram_3()
else:
    print("Imported as a module, __name__ is:", __name__)