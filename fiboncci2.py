while True:
    counter=1
    print("How many numbers of the fibonacci sequence would you like me to count?")
    number=int(input())
    if number>0:
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
