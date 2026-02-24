# =================================================================
# PROJECT: THE LIST CLEANER
# -----------------------------------------------------------------
# 
# ### PHASE 1: THE MILK CHECK
# Before you start formatting, check if 'milk' is in the list.
# 1. If 'milk' NOT in list: append 'milk' to the list.
# 2. If the list is empty: the instructions say return an empty list.
#    (Hint: Handle the empty list check BEFORE adding milk).
#
# ### PHASE 2: THE LOOP (Iteration)
# You need to go through the list one by one. Since you need an 
# index number starting from 1, the 'enumerate' function is your friend!
#
# Logic:
# for index, item in enumerate(shopping_list, start=1):
#
# 
#
# ### PHASE 3: STRING FORMATTING (The 3 Rules)
# For every 'item' in your loop, apply these in order:
# 1. CLEAN: item.strip() (removes outer spaces)
# 2. CASE:  item.capitalize() (First letter up, rest down)
# 3. PREFIX: f"{index}/ {cleaned_item}"
#
# 
#
# ### PHASE 4: COLLECTING RESULTS
# Create a new empty list (e.g., cleaned_final = []) before the loop.
# Inside the loop, 'append' your newly formatted string to that list.
#
# ### PHASE 5: THE RETURN
# Return your final list of formatted strings.
#
# -----------------------------------------------------------------
# SUMMARY CHECKLIST:
# [ ] Did I handle the empty list case first?
# [ ] Did I add 'milk' ONLY if it was missing?
# [ ] Does my index start at 1 (not 0)?
# [ ] Is there a space after the slash? (Example: "1/ Item")
# =================================================================

# START YOUR CODE BELOW THIS LINE:
def clean_list(shopping_list):
    # Rule: If input is empty, return empty list
    if not shopping_list:
        return []

    # Rule: Add 'milk' if not present (before formatting)
    if "milk" not in shopping_list:
        shopping_list.append("milk")
    
    cleaned_final = []
    
    # Rule: Index starting from 1 + formatting
    for index, item in enumerate(shopping_list, start=1):
        # Rule: Strip spaces and Capitalize only first letter
        cleaned_item = item.strip().capitalize()
        formatted_item = f"{index}/ {cleaned_item}"
        cleaned_final.append(formatted_item)
    
    return cleaned_final
