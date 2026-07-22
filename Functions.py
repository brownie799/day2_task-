
def greet(name): 
    """This function greets the person passed in as a parameter."""
    return f"Hello, {name}!"

def add_numbers(a, b=0): 
    return a + b

message = greet("Bob")
print(message) 

sum_result = add_numbers(5, 3)
print(f"Sum: {sum_result}") 
default_sum = add_numbers(10)
print(f"Default Sum: {default_sum}") 