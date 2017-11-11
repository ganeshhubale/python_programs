import math
def main():
    x = False
    try:    
        while x == False:
            n = int(input("Enter number: "))
            x = perfect(n)
            print(x)
    except Exception as e:
         print("Exception caught ",e)
         main()
    

def perfect(n):
    result = False
    sqrt=int(math.sqrt(n))
    result=n==sqrt * sqrt
    return result

main()
