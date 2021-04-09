for x in range(10, 25):
    if x > 1:
        for y in range(2,x):
            if(x % y) == 0:
                print(x, "bukan prima")
                break
        else:
            print(x,"adalah bilangan prima")
