"""
This is a module that when run will translate any JSON string into variables
alongside their associated values

Author: Elyas Levens
Date: 7/12/24
"""

import introcs







#helpful functions


def fix_list(list):
    """
    Put a list in get a tuple out
    """



def fetch_json(link):
    """
    This function fetches, reads, and outputs the string from the link provided

    The return will be a string of JSON text

    Precondition: The link must be a string to a valid website/API that will
    return a JSON text in any form
    """

    assert type(link)==type('string')
    result=introcs.urlread(link)
    return result


def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quote characters

    Note that the double quotes must be part of the string.  So "Hello World" is a
    precondition violation, since there are no double quotes inside the string.

    Example: first_inside_quotes('A "B C" D') returns 'B C'
    Example: first_inside_quotes('A "B C" D "E F" G') returns 'B C', because it only
    picks the first such substring.

    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote characters inside
    """
    #assert type(s)==type('string'), 'The input is not a string'
    #assert introcs.count_str(s,'"')>1, 'There is not 2 double quotes in the input'

    first=introcs.find_str(s,'"')
    second=introcs.find_str(s,'"',first+1)
    JSON=s[first+1:second]
    return JSON


def read_var(JSON):
    """
    This function defines the name of variables in the form of strings that are
    read fromJSON text

    Example: '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    The return will be a list of variables
    EX: (A,B,C,D,E)

    Precondition: The input must be a string and in the form of JSON
    """

    total_var=int(introcs.count_str(JSON,',')+1)

    old_comma=0
    var=[None]*total_var

    #tried searching for colons but commas are better because stupid boolean
    #finds first comma, then the first inside quotes before that comma
    #then stores that in a list
    #then finds the next comma starting from i+1 after the last
    for i in range(total_var):
        s_current_comma=introcs.find_str(JSON,',',old_comma) #help
        var[i]=first_inside_quotes(JSON[old_comma:s_current_comma])
        old_comma=s_current_comma + 1

    #just gets rid of the redundant quotes in the list
    for i in range(total_var):
        introcs.strip(var[i],'"')
    print(var)
    return var
    # pain in the ass


def red_var_def(JSON):
    """
    This function defines the value of variables in the form of strings
    that are read from JSON text

    Example: '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    The return will be a list of variable values
    EX: (A,B,C,D,E)

    Precondition: The input must be a string and in the form of JSON
    """
    total_var=int(introcs.count_str(JSON,',')+1)

    old_comma=0
    old_colon=0
    var=[None]*total_var

    #tried searching for colons but commas are better because stupid boolean
    #finds first comma, then the first inside quotes before that comma
    #then stores that in a list
    #then finds the next comma starting from i+1 after the last
    for i in range(total_var):
        s_current_comma=introcs.find_str(JSON,',',old_comma)
        s_current_colon=introcs.find_str(JSON,':',old_colon)

        var[i]=introcs.strip(JSON[s_current_colon+1:s_current_comma])
        var[i]=introcs.strip(var[i],'"')
        old_comma=s_current_comma + 1
        old_colon=s_current_colon + 1
    print(var)
    return var
    # pain in the ass

#Script
link=input('Paste the link you\'d like to fetch the variables of: ')

JSN=fetch_json(link)
var1=read_var(JSN)
var2=red_var_def(JSN)
