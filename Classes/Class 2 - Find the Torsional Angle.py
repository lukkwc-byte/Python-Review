import math
class Cart():
    def __init__(self, A):
        self.X = A[0]
        self.Y = A[1]
        self.Z = A[2]
    
    def __str__(self):
        return str(self.X) + " " + str(self.Y) + " " + str(self.Z)
    
    def vector(A, B):
        return Cart([B.X - A.X, B.Y - A.Y, B.Z - A.Z])
    
    def dot(A, B):
        return A.X*B.X + A.Y*B.Y + A.Z*B.Z
    
    def cross(A,B):
        return Cart([A.Y * B.Z - A.Z * B.Y, A.Z * B.X - A.X * B.Z, A.X * B.Y - A.Y * B.X])
    
    def mod(A):
        return((A.X**2 + A.Y**2 + A.Z**2)**0.5)

A, B, C, D = [Cart(list(map(float, input().split()))) for i in range(4)]

X = Cart.cross(Cart.vector(A,B), Cart.vector(B,C))
Y = Cart.cross(Cart.vector(B,C), Cart.vector(C,D))

cosPhi = Cart.dot(X,Y) / (Cart.mod(X) * Cart.mod(Y))
PhiRad = math.acos(cosPhi)
PhiDeg = math.degrees(PhiRad)
print(round(PhiDeg,2))


        