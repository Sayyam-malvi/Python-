a = int(input("Enter the number from 1 to 10"))

match a :
    case 2 :
        print("You won a second prize")
    case  4 :
        print("You won first prize ")
    case 6 :
        print("You won third prize ")
    case _ :
        print(" \'LOL! \' , You won nothing ")