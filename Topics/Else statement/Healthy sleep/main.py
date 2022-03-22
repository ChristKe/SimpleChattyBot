A = input()
B = input()
H = input()

if (int(H) >= int(A)) and (int(H) <= int(B)):
    print('Normal')
if int(H) < int(A):
    print('Deficiency')
if int(H) > int(B):
    print('Excess')
