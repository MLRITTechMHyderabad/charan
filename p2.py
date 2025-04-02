def min_max(numbers):
    min = max = numbers[0]
    for i in numbers:
        if i<min:
            min=i
        if i>max:
            max=i
    return min,max

numbers = [1,5,8,6,4]
min, max = min_max(numbers)
print("minimum no: ",min)
print("maximum no: ",max)