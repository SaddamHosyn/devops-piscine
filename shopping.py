# =================================================================
# PROJECT: REMEMBER THE APPLE
# -----------------------------------------------------------------
# 
# ### PHASE 1: THE EMPTY LIST CHECK
# The instructions state: "If the input list is empty, return an empty list."
# In Python, an empty list evaluates to False. 
# You can check this at the very beginning of your function.
#
# Logic:
# if not shopping_list:
#     return shopping_list
#
# ### PHASE 2: CHECKING FOR MEMBERSHIP
# You need to see if "apple" is already in the list. Python makes this
# very easy with the 'in' or 'not in' keywords.
#
# 
#
# ### PHASE 3: MODIFYING THE LIST (.append())
# If the apple is missing, you need to add it to the end of the list.
# Use the .append() method.
# Example: shopping_list.append("apple")
#
# 
#
# ### PHASE 4: THE RETURN
# Regardless of whether you added the apple or it was already there, 
# you must return the final version of the list.
#
# ### PHASE 5: THE TEST (In test.py)
# import shopping
# print(shopping.remember_the_apple(["milk", "bread"])) 
# # Should output: ["milk", "bread", "apple"]
#
# -----------------------------------------------------------------
# SUMMARY CHECKLIST:
# [ ] Did I handle the empty list case first?
# [ ] Did I use the .append() method correctly?
# [ ] Does my function return the list at the end?
# [ ] Is the word "apple" spelled exactly as requested (lowercase)?
# =================================================================

# START YOUR CODE BELOW THIS LINE:
def remember_the_apple(shopping_list):
    if not shopping_list:
        return shopping_list
    if "apple" not in shopping_list:
        shopping_list.append("apple")
    return shopping_list

