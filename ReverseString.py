# Reverse a String 
def reverse_string(input_string):
    reves_str=""
    for char in input_string:
        reves_str= char+reves_str
    return reves_str
string="Taha"
reverse_string=reverse_string(string)
print(f"Revese string is: {reverse_string}")    
