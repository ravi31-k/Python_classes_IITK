# Template for P12

#from typing_extensions import Unpack


def main():
    # Write your code below.  Take care of indentation

    # Take inputs for u, a and t. Remember to convert the type for each of the input from string to the required type.
    u = float(input())
    a = float(input())
    t = int(input())

    # Calculate the final velocity (v) using the formula v = u + at. Also, round the value obtained to two decimal places.
    v = (a + (u * t ))
    v = round(v,2)
    # Print the answer. Note that the printed strings should have the exact same case as given in the problem statement in order to pass the test cases
    print("The final velocity is" ,v,)

# This is required to ensure that we can import your solve function without activating other parts of code
if __name__ == "__main__":
    main()



