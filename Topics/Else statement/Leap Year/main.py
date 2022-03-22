# put your python code here
a = int(input())
m = 4
k = 100
z = 400

if (a % m == 0) and (a % k != 0) or (a % z == 0):
    print("Leap")
else:
    print("Ordinary")