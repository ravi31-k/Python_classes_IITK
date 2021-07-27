# Template for P14

def main():
    # Write your code below

    # Take an integer input s, denoting the number of seconds elapsed for a certain event.
    s = int(input())
    
    # Find the number of hours, minutes and seconds from the input.
    hh = int(round(s/3600 , 4))
    mm = int(round((s-hh*3600)/60, 4))
    ss = int(round(s-hh*3600 - mm*60, 4))
    hh = str(hh)
    mm= str(mm)
    ss= str(ss)
    # Print the output as hh:mm:ss
    print(hh + ":" + mm + ":" + ss)
print("mssg is (msg)")
# This is required to ensure that we can import your solve function without activating other parts of code
if __name__ == "__main__":
    main()