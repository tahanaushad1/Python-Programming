# Remove Duplicate From The List
def remove_duplicate(lst):
    return list(set(lst))
number=[20,40,50,50,60,30,70,50]
remove_duplicate=remove_duplicate(number)
print(f"List After removing elements:{remove_duplicate} ")