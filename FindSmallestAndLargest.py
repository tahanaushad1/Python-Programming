def largest_and_smallest(arr):
    if not arr:
        return None,None
    largest=max(arr)
    smallest=min(arr)
    return largest,smallest

array=[20,60,50,60,49]
largest,smallest=largest_and_smallest(array)
print(f"Largest:{largest},smallest:{smallest}")    
