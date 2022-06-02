print("please write an integer number which is an armstrong number!...")

num = input("Write here: ")
num_set = list(num)
pw = len(num_set)
a = 0
if num.isdigit():
    for i in num_set:
        i = int(i)
        a = a + i**pw
    if int(num) == a:
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")
else:
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
