number=[12,0,60,70,90]
for item in number:
    if item==0:
        number.remove(item)
        number.append(item)

print(number)        