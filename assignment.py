#変数へ代入：assignment
print("Hello World")

a = "Hello World"
print(a)

b = "How are you doing"

print(a + b)

#
#変数の命令規則
#文字から始まる
#文字、数字、＿（アンダースコア）を使う
#Case sensitive(Helloとhelloは別の変数)

# format
print("hello{}".format("World"))
print("{} {}".format(a, b))

name = "John"
print("Hey, {}!! How are you doing?".format(name))

# fstring
print(f"{b} {name}")
print(f"Hey, {name}!! How are you doing?")

