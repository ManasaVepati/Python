import math
n = int(input())
root = int(math.sqrt(n))
if root*root == n:
    print("Perfect square")
else:
    print("not a perfect square")
