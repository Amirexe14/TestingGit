s = input("enter numbers, ill sort em: ")
# asdasdsadasd
numbers = []

for number in s:
    numbers.append(int(number))

for i in range(len(numbers)):
    for n in range(len(numbers)-1):
        if numbers[n] > numbers[n+1]:
            numbers[n], numbers[n+1] = numbers[n+1], numbers[n]

print("This be your numbers?", numbers)