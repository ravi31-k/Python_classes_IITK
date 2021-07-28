# Template for P33

def main():
    # Take input for four assessments.
    # write your code here
   num = int(input())
    # initialize sum
   sum = 0

    # find the sum of the cube of each digit
   temp = num
   while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    # display the result
   if num == sum:
        print("Sum of Cubes is {}. It is the same as the number {}.".format(sum,num))
   else:
         print("Sum of Cubes is {}. It is NOT same as the number {}.".format(sum,num))
     

if __name__ == "__main__":
    main()
