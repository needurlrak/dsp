# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.
    
   


    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    printct = count
    if (count >= 10):
        printct =  'many'
    return("Number of donuts: " + str(printct))
    #raise NotImplementedError


def both_ends(s):
   
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    if (len(s) >= 2):
        return(s[:2] + s[len(s) - 2:])
    else:
        return("")
    


def fix_start(s):
   

    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    str_list = list(s)
    first_letter = str_list[0]
    fixed_list = list()
    for letter in str_list[1:]:
        if (letter == first_letter):
            fixed_list.append('*')
        else:
            fixed_list.append(letter)
    return first_letter + ''.join(fixed_list)
   # raise NotImplementedError


def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    a_swapped = b[:2] + a[2:]
    b_swapped = a[:2] + b[2:]
    return (a_swapped + ' ' + b_swapped)
    #raise NotImplementedError


def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    s_len = len(s)
    if (s_len >=3):
        if (s[s_len-3:] == 'ing'):
            return s + 'ly'
        else:
            return s + 'ing'
    else:
        return s
    #raise NotImplementedError


def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    ind_not = s.find('not')
    ind_bad = s.find('bad')
    final_string = s
    
    if (ind_not < ind_bad & ind_bad > -1 & ind_not > -1):
        final_string = s[:ind_not] + 'good' + s[ind_bad + 3:]

    return final_string
    raise NotImplementedError


def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    
    len_a = len(a)
    len_b = len(b)
    a_front = a[:int(math.ceil(len_a/2.0))]
    b_front = b[:int(math.ceil(len_b/2.0))]
    a_back = a[int(math.ceil(len_a/2.0)):]
    b_back = b[int(math.ceil(len_b/2.0)):]
    return(a_front + b_front + a_back + b_back)
    raise NotImplementedError
