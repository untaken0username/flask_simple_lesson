list = ['apple', 'orange', 'apple', 'pineapple']
result = {}
for x in list:
    if x in result:
        result.update({x: result.get(x) + 1})
    else:
        result.update({x: 1})

for x in result:
    print(x, result.get(x))
