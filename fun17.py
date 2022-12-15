import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
def hello():
    print("Hello World")
    hello()