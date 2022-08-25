from ast import If
import math

counter = int(input("tedad estefade?"))
while counter > 0 :

    cal = input(" 1)Basic \n 2)Advance \n")
    if cal == 'Basic' or cal == "1" or cal == "basic":

        ex = input("chekar mikhay bkoni? \n 1) + \n 2)- \n 3)* \n 4)/ \n 5)% \n 6)^ \n 7)// \n")

        num_1 = float(input("Enter first number  "))
        num_2 = float(input("Enter secound number  "))

        if ex =='+' or ex == "sum" or ex == "Sum" or ex == "plas" or ex =="Plas" or ex =="1":
            res = num_1 + num_2

        elif ex == "-" or ex == "subtraction" or ex == "Subtraction" or ex =="2":
            res = num_1 - num_2

        elif ex == "*" or ex == "multiplication" or ex == "Multiplication" or ex =="3":
            res = num_1 * num_2

        elif ex == "/"or ex == "division" or ex == "Division"or ex =="4":
            if num_2 ==0:
                print("oh noo cant /0 ")

            else:    
                res = float(num_1 / num_2)

        elif ex == "%" or ex== " Divide remaining" or ex =="divide remaining" or ex =="remainder" or ex =="Remainder" or ex =="5":
            res = num_1 % num_2

        elif ex == "^" or ex == "tavan" or ex == "Tavan" or ex =='power' or ex == "Power" or ex =="6":
            res = num_1 ** num_2

        elif ex=="//" or ex == "Correct division" or ex == "Correct Division" or ex =='correct division' or ex == "correct Division" or ex =="7" :
            res = int (num_1 / num_2)

        counter=counter-1       
        print("in",cal , "your numbers are " , num_1,"and ",num_2 ,"the function is ", ex , "your answer is ", res,"the counter can try: ",counter )
    
    
    elif cal == 'Advance' or cal == "2" or cal == "advance":

        ex = input("chekar mikhay bkoni? \n 1)Squared \n 2)Squared Root \n 3)Absolute value \n 4)Sin \n 5)Cos \n 6)Tan \n 7)Prime \n")
        num_1 = int(input("Enter your number "))

        if ex == "t2"or ex == "squared" or ex == "Squared" or ex== "**" or ex =="1" :
            res = num_1 ** 2

        elif ex == "sqrt" or ex == "square root" or ex == "Square root"or ex == "Square Root" or ex == "square Root"or ex =="2":
            res = math.sqrt(num_1)

        elif ex == "||" or ex == "Absolute value" or ex == "Absolute Value"or ex == "absolute value" or ex == "ghadr motlagh"or ex =="3":

            if num_1 >= 0 :
                res = num_1

            else:
                res = -(num_1)

        elif ex == "sin"or ex =="4":
            res = math.sin(num_1)

        elif ex == "cos"or ex =="5":
            res = math.cos(num_1)

        elif ex == "tan"or ex =="6":
            res = math.tan(num_1)



        elif  ex == "aval" or ex == "prime" or ex== "Prime" or ex =="7":
            i=0
            accumulator = 0

            
            for i in range(1, num_1+1):

                if num_1%i == 0:
                    accumulator+=1

            if accumulator==2:
                    print('your number is prime')
            else:
                    print('your number is not prime')
            
            break



        counter=counter-1
        print("in",cal , "your numbers is " , num_1,"the function is", ex , "your answer is ", res,"the counter can try:",counter)

    else:
            print("noting :)")