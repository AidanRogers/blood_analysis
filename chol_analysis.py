def HDL_analysis(HDL_level):
        if HDL_level >= 60:
            return "Normal"
        elif 40<= HDL_level <60:
            return "Borderline Low"
        else:
            return "Low"

def cholesterol_analysis():
        print("Cholesterol Analysis")
        HDLinput = input("Enter test result: ")
        test_info = HDLinput.split("=") #splits along the equal sign
        if test_info[0] == "HDL":
            answer = HDL_analysis(int(test_info[1]))
            print("the Level is {} ".format(answer))
            JDL_analysis()


def interface():
    choice = 0
    while True:
        print("Cholesterol Calc")
        print("options")
        print("   0- Quit")
        choice = input("Enter your option:  ")
        if choice == '9':
            return
        elif choice == "1":
            cholesterol_analysis()

if __name__ == "__main__":
    interface()
