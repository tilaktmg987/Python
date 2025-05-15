# Write a program using functions to find greatest of three numbers.

def greater(num1,num2,num3):
    if(num1>num2 and num1>num3):
        return num1
    elif(num2>num1 and num2>num3):
        return num2
    else:
        return num3
    
print(f"greatest number is: {greater(3,4,5)}")
