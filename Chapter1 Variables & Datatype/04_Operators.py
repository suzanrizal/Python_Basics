# Arethmetic operators 
a=3
b=7
c=a+b
print(c)

# Assignment operators 
a = 4-2 #assign 5-2 in a
print(a)
b = 6
b += 3 # increment the value of b by 3 then assign it to b 
b -= 3 # decrement the value of b by 3 then assign it to b 
print(b)

# Comparison operators -- always return boolean values 

d = 15<10
print(d)

# Logical operators -- And , Or and Not

temperature = 25

if temperature >= 20 and temperature <= 30:
    print("The temperature is comfortable")
else:
    print("The temperature is not comfortable")

temperature = 35

if temperature < 10 or temperature > 30:
    print("The temperature is extreme")
else:
    print("The temperature is normal")

temperature = 25

if not temperature > 30:
    print("It is not too hot")
else:
    print("It is too hot")