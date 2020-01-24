def HDL_analysis(HDL_level):
    if HDL_level >= 60:
        return "Normal"
    elif 40 <= HDL_level < 60:
        return "Borderline Low"
    else:
        return "Low"

def LDL_analysis(LDL_leve):
    if LDL_level >=190:
        return "Very High"
    elif 160 <= LDL_level < 190:
        return "High"
    elif 130 <= LDL_level < 160:
        return "Borderline High"
    elif LDL_level < 130:
        return "Normal"


def cholesterol_analysis():
    print("Cholesterol Analysis")
    typetest = input("LDL or HDL for type of test '=' it's value: ")
    test_info = typetest.split("=")  # splits along the equal sign
    if test_info[0] == "HDL":
        answer = HDL_analysis(int(test_info[1]))
        print("the Level is {} ".format(answer))
    if test_info[0] == "LDL":
        answer = LDL_analysis(int(test_info[1]))
        print("the Level is {} ".format(answer))



def interface():
    while True:
        print("Cholesterol Calculator")
        print("Options:  ")
        print("  1 - Cholesterol Analysis")
        print("  9 - Quit")
        choice = input("Enter your option:  ")
        if choice == '9':
            return
        elif choice == "1":
            cholesterol_analysis()


if __name__ == "__main__":
    interface()
