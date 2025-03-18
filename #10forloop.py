for item in range(90000,100000,100000):
    print(item)

total=0
for number in range(0,11,1):
    total+=number
print(total)


for x in range(4):
    for y in range(3):
        if x!=y:
            continue
        else:
            print(f"({x}, {y})")

for x in range(5):
    if x == 0:
        print('x'*5)
    elif x == 2:
        print('x'*5)
    else:
        print("x"*2)


print("-------------------")

x_counts=[5,2,5,2,2]
for x_count in x_counts:
    print("x"*x_count)

print("-------------------")
print("-------------------")
print("-------------------")

x_counts=[2,2,2,2,5]
for x_count in x_counts:
    output=""
    for x in range(x_count):
        output+="x"
    print(output)
