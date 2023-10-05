for i in range(5):
    print(f"{i}: *")
    
print("this is the end...")

text = "String"
print(text*3)

a="*"
r=9
for i in range(5):
    if(i>=r//2):
        print(a*(r-i))
    else:
        print(a*(i+1))
    
print("stop")

def print_arrow(n_lines, symbol):
    """Print a 'arrow' of symbols with 'n_lines' lines."""
    for i in range(n_lines):
        print(f"{i}: {symbol*(i+1)}")
        
    print("stop! ", end="")
    print("yes, stop here")
    


def solve_quadratic_eq(.....):
    #function body to complete
    #return ...

#Call my new super function twice
print_arrow(3, "?")
print_arrow(5, "/")