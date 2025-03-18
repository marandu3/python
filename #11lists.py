names = ['john', 'wilbard', 'marandu', 'james', 'bernard']
print(names)
print(names[:])


numbers=[2,5,1,6,9,4,3,8,0]
max=numbers[0]
for number in numbers:
    if number > max:
        max = number
print (max)

print("hello world")

print(len(numbers))



matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[1][2])

for row in matrix:
    for item in row:
        print (item)


#######lis functions or methods

number=[5,2,1,7,4]
number.append(13)
print(number)

number.insert(3,37)
number.remove(4)
##.pop()
#.remove()
#instead of index should use in operator
print(number.index(37))

print(number)