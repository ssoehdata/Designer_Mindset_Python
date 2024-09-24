
limit = 100 
name = "John"       # type str can easily be inferred here
my_list: list[int | float | bool| str] = [1, 3, 3.5,False, "HAL" ]


def verify_password(submitted_password: str, stored_hash: str = "123456") -> bool:
    return True

def compute_average(numbers:list[float])-> float:
    a = compute_average
    print(type(a))

##################
# Notes#
##################
# In python -type hints are not required(ignored at runtime), but are helpful for dev e.g. static analysis
# 
# Static vs. Dynamic types(when they are acquired):
# Static  - during compilation phase,allows for optimization
# Dynamic - at runtime 

# Manifest vs. Inferred(how types are being specified and detected):
# Manifest - types of variables, functions etc. explicitly defined
# Inferred - compiler or interpreter infers the type from code context

# Nominal vs. Structural(whether the type ID´d by name or by its structure):
# Nominal - 
# Structural - 

# Duck Type(Python uses this paradigm): - 

# Strong vs. Weak Typing:
# Strong -
# Weak -