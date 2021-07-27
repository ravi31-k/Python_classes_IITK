# Template for P11

def main():
    # Write your code below. Take care of indentation

    # Take input for temperature in Fahrenheit. Remember to convert the type for the input from string to the required type.
    

    # Calculate the temperature in Celsius (C) using the formula C=(F−32)×5/9. Also, round the value obtained to two decimal places.
    
    TF = float(input())
    TC = (float((TF - 32 )) * (5/9) )
    TC = round(TC , 2)
    # Print the answer.
    print("Fahrenheit temperature", TF ,"is the same as" ,TC, "degrees Celsius.".format())
    #print("Fahrenheit temperature {} is the same as {} degrees Celsius.".format(TF , TC))

# This is required to ensure that we can import your solve function without activating other parts of code
if __name__ == "__main__":
    main()