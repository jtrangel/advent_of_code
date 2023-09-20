input = "pphepp"

print([a for a,b in zip(input, input[1:]) if a == b])
print({a for a,b in zip(input, input[1:]) if a == b})
