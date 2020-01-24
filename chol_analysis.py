def HDL_analysis(HDL_level):
    if HDL_level >= 60:
        return "Normal"
    elif 40 <= HDL_level < 60:
        return "Borderline Low"
    else:
        return "Low"

def LDL_analysis(LDL_level):
    if LDL_level >= 190:
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
    print(test_info[0].strip(" "))
    print(test_info[1].strip(" "))
    if test_info[0] == "HDL":
        answer = HDL_analysis(int(test_info[1]))
        print("The HDL Level is {} ".format(answer))
    if test_info[0] == "LDL":
        answer = LDL_analysis(int(test_info[1]))
        print("The LDL Level is {} ".format(answer))



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
