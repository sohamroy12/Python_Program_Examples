# Python Pattern Program - Number Pattern (Printing Numbers in Pyramid Shape)
# learn How to print numbers in pyramid shape in detail.
# To print numbers in pyramid shape we will use nested for loops.


num = int(input("Enter the number of rows: "))
print(f'your input is {num}')
# Need to keep in mind that range is always denoted as range(start,end) end is always omited and "end-1" value is considered.
for i in range(1, num+1):
    for j in range(1, num-i+1):
        print(" ", end="")  # same as print(end=" ")
    for j in range(i, 0, -1):
        print(j, end="")
    for j in range(2, i+1):
        print(j, end="")
    print()
