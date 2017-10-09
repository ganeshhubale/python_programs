n=int(input("Select \n 1. Celsius to farenheit \n 2. Farenheit to celsius\n"))

if n == 1:
    c = float(input("Enter temperature in Celsius: "))
    print("\nCelsius  Fahrenheit")
    print("%7.1f %9.2f " % ( c, (c*1.8)+32))
elif n == 2:
    f = float(input("Enter temperature in farenheit: "))
    print("\nFahrenheit  Celsius")
    print("%7.1f %9.2f " % (f, ((f-32)/1.8)))
else:
    print("invalid input")
                             
