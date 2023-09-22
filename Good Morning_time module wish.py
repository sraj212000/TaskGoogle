name = input("Enter Your name : ")
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp1 = int(time.strftime('%H'))
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)
if (timestamp1 >= 4 and timestamp1 < 12):
    print("Good Morning", name)
elif (timestamp1 >=12 and timestamp1 < 16):
    print("Good Afternoon", name)
elif (timestamp1 >= 16 and timestamp1 < 20):
    print("Good Evening", name)
else:
    print("Good Night", name)
