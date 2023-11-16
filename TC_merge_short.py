import turtle
from timeit import default_timer as timer

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    # Compare elements from both halves and merge them in sorted order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Append the remaining elements from both halves (if any)
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result

class test_graph():
    def __init__(data):
        data.x=[]
        data.y=[]
    def test(data,func,xval):
        x=0
        while x <= xval :
            num = [i for i in range(x,0,-1)]
            start = timer()
            func(num)
            end = timer()
            x += 1
            data.x.append(x)
            data.y.append(round(end-start,9)*10000)

test1 = test_graph()
test1.test(merge_sort,950)
t1 = turtle.Turtle()
t1.penup()
t1.goto(-500,-340)
t1.pendown()

for i in range(len(test1.y)):
    t1.goto(-500+test1.x[i],-340+test1.y[i])
