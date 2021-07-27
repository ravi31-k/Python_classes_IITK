# Template for P23

def main():
    # Write your code below

    # Take input of the string
    ss = str(input())
    s = ss.lower()
    rs = s[::-1]
    # Check for palindrome
    if (s == rs) : 
         print(ss,"True")
    else : 
         print(ss,"False")

    # Print the output. Note that the printed strings should have the exact same case as given in the problem statement in order to pass the test cases
  #  print()

# This is required to ensure that we can import your solve function without activating other parts of code
if __name__ == "__main__":
    main()