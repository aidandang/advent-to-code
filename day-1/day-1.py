# Using readlines() 
file = open('numbers.txt', 'r') 
lines = file.readlines() 

arr = []
# Strips the newline character 
for line in lines:
    arr.append(int(line.strip()))

def get_multi_by_2_numbers():
    numbers = {}
    for a in arr:
        numbers[a] = 2020 - a
    for a in arr:
        if numbers[a] in numbers:
            return numbers[a] * a

def get_multi_by_3_numbers():
    for i in range(len(arr)):
        first_num = arr[i]
        numbers = {}
        for a in arr:
            if a is not arr[i]:
                numbers[a] = 2020 - first_num - a

        for a in arr:
            if a is not arr[i]:
                if numbers[a] in numbers:
                    return numbers[a] * a * first_num

print(get_multi_by_2_numbers())
print(get_multi_by_3_numbers())