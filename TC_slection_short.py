import turtle
from timeit import default_timer as timer
num = [10,9,8,7,6,5,4,3,2,1,20,19,18,17,16,15,14,12,11]
small = num[0]
lst = []

def shrt(num):
    while len(num)!=0:
        small = num[0]
        for i in num:
            if small > i:
                small = i
        lst.append(small)
        num.remove(small)

class test_graph():
    def __init__(data):
        data.x=[]
        data.y=[]
    def test(data,func,xval):
        x=0
        while x <= xval :
            num = [i for i in range(x,0,-1)]
            start = timer()
            shrt(num)
            end = timer()
            x += 1
            data.x.append(x)
            data.y.append(round(end-start,9)*10000)

test1 = test_graph()
test1.test(shrt,950)
t1 = turtle.Turtle()
t1.penup()
t1.goto(-500,-340)
t1.pendown()

for i in range(len(test1.y)):
    t1.goto(-500+test1.x[i],-340+test1.y[i])
    
