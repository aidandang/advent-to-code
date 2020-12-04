# Using readlines() 
file = open('passwords.txt', 'r') 
lines = file.readlines()

arr = []
# Strips the newline character and split by ' '
# to cut each line into time, char and string
for line in lines:
    arr.append(line.strip().split(' '))

def part_one():

    result = 0
    for a in arr:
        # get range of password condition
        smallest, largest = a[0].split('-')
        # get char in that range
        char = a[1][0]
        
        # count char in the string
        count = 0  
        for c in a[2]: 
            if c == char: 
                count += 1

        # check if count in range of password condition
        if count >= int(smallest) and count <= int(largest):
            result += 1
    return result

def part_two():

    result = 0
    for a in arr:
        # get range of password condition
        first_position, second_position = a[0].split('-')
        # minus 1 to match with array index
        first_position = int(first_position) - 1
        second_position = int(second_position) - 1
        # get char in that range
        char = a[1][0]
    
        count = 0
        for i in range(len(a[2])):
            if i == first_position:
                if a[2][i] == char:
                    count += 1 
            if i == second_position:
                if a[2][i] == char:
                    count += 1
              
        
        if count == 1:
            result += 1
    
    return result

print(part_one())
print(part_two())
    