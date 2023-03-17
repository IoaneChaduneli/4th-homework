import emojis
x = input(": ")

x = x.split(",")

n = emojis.encode(x[-1])

print(n)