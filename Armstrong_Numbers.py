# Python Programs - Armstrong Numbers
# In this python programming tutorial you will learn about the Armstrong numbers.


N = int(input("Give me a range from \"0\" to a \"n\" number to find the Armstrong Numbers in the range: "))

for i in range(N+1):
    num = i
    result = 0
    L = len(str(i))
    while(i != 0):
        digit = i % 10
        result = result + digit**L
        i = i//10
    if result == num:
        print(f"The Armstrong in the given list is : {num}")
