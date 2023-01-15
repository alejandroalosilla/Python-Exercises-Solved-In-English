#  Ex105 - Make a program that has a grades() function that can receive several
# grades from students and will return a dictionary with the following
# information:
#
# - Number of notes
# - the highest grade
# - The lowest grade
# - The average of the class
# - The situation (optional)
#
#  Also add the docstrings of this function for the developer to look
# up.

def grades(*g, sit=False):
    """
    -> Function to analyze notes and situations of several students.
    :param g: One or more student grades (multiple accepted).
    :param sit: Optional value, indicating whether to add the 'situation'.
    :return: Dictionary with various information about the situation of the class.
    """
    d = dict()
    d['Total Grades'] = len(g)
    d['Highest'] = max(g)
    d['Lowest'] = min(g)
    d['Average'] = sum(g) / len(g)
    if sit is True:
        if d['Average'] >= 7:
            d['Situation'] = 'GOOD'
        else:
            d['Situation'] = 'BAD'
    return d


return_data = grades(5.5, 9.5, 10, 6.5, sit=True)
print(return_data)
print()
help(grades)
