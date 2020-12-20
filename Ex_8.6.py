nums = list()

while True :
    x = input('Enter a number: ')

    if x == 'done' : break
    else:
        nums.append(x)

print(nums)
a = max(nums)
print(a)
print('maximum:', max(nums))
print('minimum:', min(nums))
