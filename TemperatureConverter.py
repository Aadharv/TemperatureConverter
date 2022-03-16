celsius = float(input("Please enter the temperature in celsius:"))
farenheit = (celsius*1.8)+32
print("%0.1f Degree celsius is = %0.1f Degree farenheit"% (celsius,farenheit))

temp = farenheit

if(temp>=104):
    print("Its hot")
elif(temp<=50):
    print("Its cool")
else:
    print("The temperature is nice")