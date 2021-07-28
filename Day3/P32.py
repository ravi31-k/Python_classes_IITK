# Template for P24

def main():
    # Write your code below

    #Take input of the string
    st = str(input())
    # Accordingly modify the string.
    snot = st.find('not')
    sbad = st.find('bad')
    if snot>0 and sbad>0 and sbad > snot:  
            sl = len(st)
            s1 = st[:snot:1]
            s2 = st[sl:sbad+2:-1]
            s2 = s2[::-1]
            print(s1+"good"+s2)
    else :
        print(st)  
    
            # Print the output. Note that the printed strings should have the exact same case as given in the problem statement in order to pass the test cases
   

# This is required to ensure that we can import your solve function without activating other parts of code
if __name__ == "__main__":
    main()