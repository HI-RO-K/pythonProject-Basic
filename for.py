# forループ
fruits = ['apple', 'peach', 'grapes', 'banana']
#
# for fruit in fruits:
#     print(f"I love {fruit}!!")
#
# for char in "hello world!!":
#     print(f"char: {char}")

# iterationとiterable

# challenge1
print(fruits)
# favorite = input("あなたの好きなフルーツはなんですか？")
#
# for fruit in fruits:
#     if fruit == favorite:
#         print("I love {}!!".format(fruit))
#     else:
#         print("{}は別に普通です".format(fruit))

# challenge2
favorite_fruits = []
normal_fruits = []
for fruit in fruits:
    like = input("{}は好きですか？y/n".format(fruit))
    if like == "y":
        print("{}は好きです".format(fruit))
        favorite_fruits.append(fruit)
    elif like == "n":
        print("{}は別に普通です".format(fruit))
        normal_fruits.append(fruit)

print(f"favorite fruits: {favorite_fruits}")
print(f"normal fruits: {normal_fruits}")




