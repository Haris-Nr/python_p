import time

timeStamp = time.strftime('%H:%M:%S')
print(timeStamp)

# bmi find ?
# bmi = weight/height^2

weight = float(input("enter weight "))
height = float(input("enter height "))

bmi = weight/height**2

print(round(bmi,2))



print(round(674,-3))
