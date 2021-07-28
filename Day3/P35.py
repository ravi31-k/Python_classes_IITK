# Template for P35

def main():
    # Take input for four assessments.
    # write your code here
    n = int(input())
    for i in range(1,n+1) :
       
       for j in range(1,i+1) :
           k = chr(j+64)
           if k == 'A' :
                print("_{}_".format(k),end='')     
           else :
            print("{}_".format(k),end='')

       print() 
     

if __name__ == "__main__":
    main()
