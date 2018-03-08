# while True means It'll keep on execute the block of code forever.
while True:
   #A Counter is a container that keeps track of how many times equivalent values are added. 
    counter=1
   # It will ask the user to choose a number.
    print("How many numbers of the fibonacci sequence would you like me to count?")
    # number is the variable
    # int means integer
    # input means the number you want to choose and it'll give you the sequence
    number=int(input())
    # if means condition
    if number>0:
        #fibonacci sequence starts with 1
        print("1")
        a=0
        b=1
        while counter<number:
            a=a+b
            print(a)
            counter=counter+1
            if counter<number:
                b=a+b
                print(b)
                counter=counter+1
    if number<0:
       print("Please enter a positive integer.!")
    if number==0:
       print("Please enter a non-zero integer.!")
                
