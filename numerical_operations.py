# =================================================================
# PROJECT: NUMERICAL OPERATIONS
# -----------------------------------------------------------------
# 
# ### PHASE 1: THE IMPORT (The 'math' toolbox)
# At the very top of your file, you should include: 
#    import math
# This allows you to use pre-built functions like math.sqrt().
#
import math 



# ### PHASE 2: FUNCTION SIGNATURES
# You need to define 5 functions. Each takes arguments 'a' and 'b' 
# (except square_root, which only takes 'a').
#
# 1. add(a, b)          -> Uses the + operator
# 2. subtract(a, b)     -> Uses the - operator
# 3. multiply(a, b)     -> Uses the * operator
# 4. power(a, b)        -> Uses the ** operator (or math.pow)
# 5. square_root(a)     -> Uses math.sqrt(a)
#

def add(a, b):
      return a + b

def subtract(a, b):
      return a - b

def multiply(a, b):
      return a * b

def power(a, b):
      return a ** b

def square_root(a):
      return math.sqrt(a)

#
# ### PHASE 3: THE VIRTUAL ENVIRONMENT (Optional but Recommended)
# If you want to keep your system clean, use these terminal commands:
#    $ conda create --name my_env python=3.10
#    $ conda activate my_env
#
# ### PHASE 4: THE TEST (In test.py)
# Create a test.py in the same folder and add:
#    import numerical_operations
#    print(numerical_operations.add(10, 5))
#    print(numerical_operations.square_root(16))
#

