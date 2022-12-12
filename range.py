# range(start, stop, step)

# for i in [1, 2, 3, 4, 5, 6]: →

# for i in range(10):
#     print(i)
#     print("hello")

# challenge
for i in range(1, 51):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)


