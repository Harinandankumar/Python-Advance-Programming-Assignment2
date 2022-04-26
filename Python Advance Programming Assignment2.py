#!/usr/bin/env python
# coding: utf-8

# 1. Write a function that takes a positive integer num and calculates how many
# dots exist in a pentagonal shape around the center dot on the Nth iteration.
# In the image below you can see the first iteration is only a single dot. On the
# second, there are 6 dots. On the third, there are 16 dots, and on the fourth
# there are 31 dots.
# 
# Return the number of dots that exist in the whole pentagon on the Nth
# iteration.
# Examples
# pentagonal(1) ➞ 1
# pentagonal(2) ➞ 6
# pentagonal(3) ➞ 16
# pentagonal(8) ➞ 141
# 
# 
# 
# 
# 
# 
# Nas:-

# In[2]:


def pentagonal(in_num):
    output = 1
    if in_num >=1:
        for ele in range(in_num):
            output = output + (5*ele)
        print(f'pentagonal({in_num}) ➞ {output}')
    else:
        print("Enter a Positive Number as Input")
        
pentagonal(1) 
pentagonal(2)
pentagonal(3)
pentagonal(8)


# 2. Make a function that encrypts a given input with these steps:
# Input: &quot;apple&quot;
# Step 1: Reverse the input: &quot;elppa&quot;
# Step 2: Replace all vowels using the following chart:
# a =&gt; 0
# e =&gt; 1
# i =&gt; 2
# o =&gt; 2
# u =&gt; 3
# # &quot;1lpp0&quot;
# 
# Step 3: Add &quot;aca&quot; to the end of the word: &quot;1lpp0aca&quot;
# Output: &quot;1lpp0aca&quot;
# Examples
# encrypt(&quot;banana&quot;) ➞ &quot;0n0n0baca&quot;
# encrypt(&quot;karaca&quot;) ➞ &quot;0c0r0kaca&quot;
# encrypt(&quot;burak&quot;) ➞ &quot;k0r3baca&quot;
# encrypt(&quot;alpaca&quot;) ➞ &quot;0c0pl0aca&quot;
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[3]:


def encrypt(in_string):
    vowels = {'a':'0','e':'1','i':'2','o':'2','u':'2'}
    out_string = ''
    for ele in in_string[::-1]:
        if ele in vowels.keys():
            out_string += vowels[ele]
        else:
            out_string += ele
    out_string += "aca"
    print(f'encrypt({in_string}) ➞ {out_string}')
        
encrypt("banana")
encrypt("karaca")
encrypt("burak")
encrypt("alpaca") 


# 3. Given the month and year as numbers, return whether that month contains
# a Friday 13th.(i.e You can check Python&#39;s datetime module)
# Examples
# has_friday_13(3, 2020) ➞ True
# has_friday_13(10, 2017) ➞ True
# has_friday_13(1, 1985) ➞ False
#                
#                
#                
#                
#                
#                
#                
#                
#                
#                
#                
#                
# Ans:-

# In[4]:


import datetime
def has_friday_13(month,year):
    output = False
    if datetime.datetime(year,month,13).strftime('%A') == 'Friday':
        output = True
    print(f'has_friday_13{month,year} ➞ {output}')

has_friday_13(3, 2020)
has_friday_13(10, 2017)
has_friday_13(1, 1985)


# 4. Write a regular expression that will help us count how many bad cookies
# are produced every day. You must use RegEx negative lookbehind.
# Example
# lst = [&quot;bad cookie&quot;, &quot;good cookie&quot;, &quot;bad cookie&quot;, &quot;good cookie&quot;, &quot;good cookie&quot;]
# pattern = &quot;yourregularexpressionhere&quot;
# len(re.findall(pattern, &quot;, &quot;.join(lst))) ➞ 2
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[5]:


import re
lst = ["bad cookie", "good cookie", "bad cookie", "good cookie", "good cookie"]
pattern = r'(?<!good)\scookie'# Regex Negative lookbehind expression
data = re.findall(pattern,' '.join(lst))
print(f'No of Bad cookies produced per day ➞ {len(data)}')


# 5. Given a list of words in the singular form, return a set of those words in the
# plural form if they appear more than once in the list.
# Examples
# pluralize([&quot;cow&quot;, &quot;pig&quot;, &quot;cow&quot;, &quot;cow&quot;]) ➞ { &quot;cows&quot;, &quot;pig&quot; }
# pluralize([&quot;table&quot;, &quot;table&quot;, &quot;table&quot;]) ➞ { &quot;tables&quot; }
# 
# pluralize([&quot;chair&quot;, &quot;pencil&quot;, &quot;arm&quot;]) ➞ { &quot;chair&quot;, &quot;pencil&quot;, &quot;arm&quot; }
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[6]:


def pluralize(in_list):
    out_set = set()
    for ele in set(in_list):
        if in_list.count(ele) > 1:
            out_set.add(ele+'s')
        else:
            out_set.add(ele)
    print(f'pluralize({in_list})  ➞ {out_set}')
    
pluralize(["cow", "pig", "cow", "cow"])
pluralize(["table", "table", "table"])
pluralize(["chair", "pencil", "arm"]) 

