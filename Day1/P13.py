# Template for P13

def main():
    # Write your code below. Take care of indentation

    # Take inputs for u, a and t. Remember to convert the type for each of the input from string to the required type.
    u = float(input())
    a = float(input())
    t = int(input())
    d = float((u*t) + ((1/2)*a*(t**2)) ) 
    d = round(d,2)
    # Calculate the displacement (d) using the formula d = ut + (1/2)at^2. Also, round the value obtained to two decimal places
    
    # Print the answer. Note that the printed strings should have the exact same case as given in the problem statement in order to pass the test cases
    print("The Diplacement is ",d,)

# This is required to ensure that we can import your solve function without activating other parts of code
if __name__ == "__main__":
    main()