# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Tuples and lists are similar. Both are essentially indexed lists of objects. The difference is that lists are 'mutable' which means that they are easy to change. Tuples can be used as keys in dictionaries and lists cannot. 

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> A set is an unordered collection of elements with no repeats. A list is an ordered collection of elements with repeats allowed. Sets use a hashtable which allows look up time to be constant. List elements are not hashable so the look up time is linear.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> A lambda function is a very simple, unnamed, 'throwaway' function. Let's say I want to sort a set of integers in decreasing order. One way I could do this is: ```sorted(list_of_ints, key = lambda integer: -integer).``` This line of code will cause sorted to use the negative of each of my integers as a key, and `sorted` automatically sorts in increasing order, so this will create an overall effect of sorting in decreasing order. I have no idea why the font is so large. Sorry about that.

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> list comprehensions are easy and natural ways to create lists. They are sort of an equivalent of 'set notation' in mathematics. Say I wanted to create a list of the cubes of all the numbers from 1 through 5, I could write   
```roots = list(map(lambda num : num**3, range(1,6)))```   
I could also use filter to get the same result:  
```roots = list(filter(lambda num : num**3 in range(), range(1,26)```.  
Since I have no repeats, and I don't particularly care about the ordering, a set comprension could work here as well.  
```roots = set(map(lambda num : num**.5, range(1,6)))``` .  
Say I wanted to create a dictionary that can be used to look up the cube of an integer. That is, the keys would be integers, and the value would be the cubes of their corresponding keys. I could use dictionary comprehension in the following way:  
```root_dict = {a : a**3 for a in range(1,6)}```  

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 907 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





