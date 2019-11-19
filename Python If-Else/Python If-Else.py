
if __name__ == '__main__':
    n = int(input().strip())
    if(n in range(1,101)):
        if(n%2==1):
            print("Weird")
        elif(1< n <6):
            print("Not Weird")
        elif(n in range(6,21)):
            print("Weird")
        elif(n>20):
            print("Not Weird")


        
