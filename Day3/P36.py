# Template for P36

def main():
    # 1. The output value is computed as a list of integers. Use Python's print(...) to print it.
    # 2. Negative integers and ZERO are allowed in the input.
    # 3. Use python's spilt(...) function to process the input string.
    # write your code here
    st = str(input())
    num = st.split(',')
    List=[]
    for ele in num:
        List.append(int(ele) + int(ele))
      
# printing result 
    print (List)

     

if __name__ == "__main__":
    main()


