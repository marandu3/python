def findmax(numbers):
    maximum=numbers[0]
    for number in numbers:
        if number>maximum:
            maximum=number
    print(f"the greatest number is {maximum}")
