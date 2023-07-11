pattern = r'^(?:[1-6],){4}[1-6]$'

# Explanation of the pattern:

# ^ start of a line.
# (?:[1-6],){4} non-capturing group that matches a number between 1 and 6 followed by a comma. {4} indicates that this group should be repeated exactly 4 times.
# [1-6] : This matches the final digit, which must be between 1 and 6.
# $ the end of a line

# This pattern will match input like 1,2,3,4,5 or 6,5,4,3,2 
# but not 1,2,3,4,5,6 (too many numbers) or 1,2,3,4,7 (7 is not between 1 and 6).