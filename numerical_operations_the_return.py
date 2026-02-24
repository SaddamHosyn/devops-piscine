# =================================================================
# PROJECT: NUMERICAL OPERATIONS - THE RETURN
# -----------------------------------------------------------------
# 
# ### PHASE 1: HANDLING DIVISION BY ZERO (The "Safety Net")
# Before performing any division or modulo, you MUST check if 'b' is 0.
# If 'b' is 0, the function should 'return 0' immediately.
#
# Logic:
# if b == 0:
#     return 0
#
# 
#
# ### PHASE 2: THREE TYPES OF DIVISION
# Python has specific operators for different mathematical results:
#
# 1. modulo(a, b) -> Returns the REMAINDER.
#    Operator: %  (Example: 10 % 3 is 1)
#
# 2. divide(a, b) -> Returns a FLOAT (decimal).
#    Operator: /  (Example: 10 / 3 is 3.333...)
#
# 3. integer_division(a, b) -> Returns an INTEGER (rounds down).
#    Operator: // (Example: 10 // 3 is 3)
#
# 
#
# ### PHASE 3: THE TEST (In test.py)
# import numerical_operations_the_return as num_op
# print(num_op.divide(10, 0))  # Should print 0, not crash!
#
# -----------------------------------------------------------------
# SUMMARY CHECKLIST:
# [ ] Did I add the "if b == 0" check to ALL THREE functions?
# [ ] Did I use / for float division and // for integer division?
# [ ] Is the filename exactly: numerical_operations_the_return.py?
# =================================================================

# START YOUR CODE BELOW THIS LINE:

def modulo(a, b):
    if b == 0:
        return 0
    return a % b

def divide(a, b):
    if b == 0:
        return 0
    return a / b

def integer_division(a, b):
    if b == 0:
        return 0
    return a // b


