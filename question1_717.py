def exponentMod(A, B, C):
     
    # Base Cases
    if (A == 0):
        return 0
    if (B == 0):
        return 1
     
    # If B is Even
    y = 0
    if (B % 2 == 0):
        y = exponentMod(A, B / 2, C)
        y = (y * y) % C
     
    # If B is Odd
    else:
        y = A % C
        y = (y * exponentMod(A, B - 1,
                             C) % C) % C
    return ((y + C) % C)
 
# Driver Code
A = 7
B = 262
C = 13
print("Power is", exponentMod(A, B, C))