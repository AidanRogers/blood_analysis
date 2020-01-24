def cholesterol_analysis():
        print("Cholesterol Analysis")
        HDLinput = inpit ("Enter test result: ")
        test_info = HDLinput.split("=") #splits along the equal sign
        if test_info[0] == "HDL":
            JDL_analysis()


def interface():
    choice = 0
    while True:
        print ("Cholesterol Calc")
        print("options")
        print("   0- Quit")
        choice = input("Enter your option:  ")
        if choice =='9':
            return
        elif choice == "1":
                cholesterol_analysis()

if __name__ == "__main__":
    interface()
