# Template for P22

def main():
    # Write your code below

    # Take input, the text and the key.
    santance = str(input()) 
    word = str(input())
    # Find the number of occurrences of the key in the text.
    count = santance.count(word)

    # Print the count."The count of",word,"is",
    print(count)

# This is required to ensure that we can import your solve function without activating other parts of code
if __name__ == "__main__":
    main()