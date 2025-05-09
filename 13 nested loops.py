## nested loops: A loop within another loop (outer, inner)
#           outer loop:
#               inner loop:


for i in range(1,4):
    for x in range(1,11):
        print(x, end="")
    print("\n")


rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end='')
    print("\n")
