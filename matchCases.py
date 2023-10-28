#Matchcases in Python,          py 3.10+
#Syntax:
'''
match EXPRESSION/VAR:
    case CONSTANT1:
        ---------------
        ---------------
    case CONSTANT2:
        ---------------
        ---------------
    case CONSTANT3:
        ---------------
        ---------------
    .
    .
    .
    case _:
        ---------------
        ---------------


print("PROGRAM STARTS")
ch = int(input("Enter No from 1 to 3:"))
match ch:
    case 1:
        print("case 1 executed")
    case 2:
        print("case 2 executed")
    case 3:
        print("case 3 executed")
    case _:
        print("default case executed")
print("PROGRAM ENDS")
'''

'''
print("PROGRAM STARTS")

ch = int(input("Enter No from 1 to 7:"))
match ch:
    case 1:
        print("It's Monday!")
    case 2:
        print("It's Tuesday!")
    case 3:
        print("It's Wednesday!")
    case 4:
        print("It's Thursday!")
    case 5:
        print("It's Friday!")
    case 6:
        print("It's Saturday!")
    case 7:
        print("It's Sunday!")
    case _:
        print("Invalid Choice")
        
print("PROGRAM ENDS")
'''

while True:
    ch = int(input("\n\nEnter Choice:\n1.Add\t2.Sub\n3.Mul\t4.Div\n5.Exit"))
    match ch:
        case 1:
            fn = int(input("Enter First Number:"))
            sn = int(input("Enter Second Number:"))
            print("Addition=", fn+sn)
        case 2:
            fn = int(input("Enter First Number:"))
            sn = int(input("Enter Second Number:"))
            print("Subtraction=", fn-sn)
        case 3:
            fn = int(input("Enter First Number:"))
            sn = int(input("Enter Second Number:"))
            print("Multiplication=", fn*sn)
        case 4:
            fn = int(input("Enter First Number:"))
            sn = int(input("Enter Second Number:"))
            print("Division=", fn/sn)
        case 5:
            print("Exiting...")
            break
        case _:
            print("Invalid Choice...")
        


















