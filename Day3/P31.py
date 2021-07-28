# Template for P21

def main():
    # Write your code below
     
    # Take inputs for the four assessments. Keep in mind that the input will be in order as given in the question.
    q = int(input())
    e = int(input())
    a = int(input())
    p = int(input())
    if q<0 :
        print('ERROR: Invalid Marks',q,'<'' 0')
    elif q>20 : 
        print('ERROR: Invalid Marks',q,'>'' 20')
    elif e<0 :
        print('ERROR: Invalid Marks',e,'<'' 0')
    elif e>100 : 
        print('ERROR: Invalid Marks',e,'>'' 100')
    elif a<0 :
        print('ERROR: Invalid Marks',a,'<'' 0')
    elif a>100 : 
        print('ERROR: Invalid Marks',a,'>'' 100')
    elif p<0 :
        print('ERROR: Invalid Marks',p,'<'' 0')
    elif p>50 : 
        print('ERROR: Invalid Marks',p,'>'' 50')
    else :    
    # Calculate the GPA.
        qw = (q/20)*0.15
        ew = (e/100)*0.40
        aw = (a/100)*0.20
        pw = (p/50)*0.25
        GPA = ((qw + ew + aw + pw)) * 10
        # Round the GPA to two decimal places
        GPA = round(GPA , 2)

        # Print the GPA
        print(GPA)

# This is required to ensure that we can import your solve function without activating other parts of code
if __name__ == "__main__":
    main()