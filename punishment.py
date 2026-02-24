# =================================================================
# PROJECT: THE AUTOMATED PUNISHMENT BOT
# -----------------------------------------------------------------
# 
# ### PHASE 1: CLEANING THE INPUTS (.strip())
# The instructions say to remove leading/trailing spaces. 
# Use the .strip() method on both 'first_part' and 'second_part'.
# Example: clean_first = first_part.strip()
#



#
# ### PHASE 2: BUILDING THE SENTENCE
# Combine your two cleaned strings with:
# 1. A space " " in between them.
# 2. A period "." followed by a newline character "\n" at the end.
# Hint: The "\n" tells Python to move to the next line.







# ### PHASE 3: THE MULTIPLICATION TRICK
# In Python, you can "multiply" a string by a number!
# Example: "Hello" * 3  results in  "HelloHelloHello"
# Use this with your 'nb_lines' variable to repeat the sentence.
#






#
# ### PHASE 4: THE TEST (In test.py)
# Your test file should look like this:
#    import punishment
#    result = punishment.do_punishment("  I will  ", "  not talk  ", 3)
#    print(result, end='')
#
# Expected Output:
# I will not talk.
# I will not talk.
# I will not talk.
#
# -----------------------------------------------------------------
# SUMMARY CHECKLIST:
# [ ] Did I use .strip() on both input strings?
# [ ] Did I add the "." and the "\n" (newline) to the sentence?
# [ ] Did I multiply the final sentence by 'nb_lines'?
# [ ] Is the function named 'do_punishment' exactly?
# =================================================================

# START YOUR CODE BELOW THIS LINE:


def do_punishment(first_part, second_part, nb_lines):
    # Step 1: Clean the strings (Remove leading/trailing spaces)
    clean_first = first_part.strip()
    clean_second = second_part.strip()
    
    # Step 2: Create the single sentence with a space, a period, and a newline
    # The \n (newline) ensures each repetition starts on a new line
    sentence = clean_first + " " + clean_second + ".\n"
    
    # Step 3: Multiply the sentence by the number of lines and return it
    return sentence * nb_lines
