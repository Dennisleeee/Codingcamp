#!/usr/bin/env python
# coding: utf-8

# In[23]:


# practice 1
def comlist(x):
    di = ''
    if type(x) == list:
        for i in range(len(x)):
            di = di+str(x[i])
        if di.isdigit():
            print(di)
        
# test 1
comlist([8,3,3])


# In[ ]:





# In[42]:


# practice 2
import random
def main():
    q = random.randint(1, 100)
    guess(q)

def guess(q):
    a = input('enter your guess between 1 to 100')
    if a.isdigit():
        if int(a) < q:
            print('lower than the correct value')
            guess(q)
        if int(a) > q:
            print('higher than the correct value')
            guess(q)
        if int(a) == q:
                print('correct!')
    else:
        print('require a digit between 1 to 100')
        guess(q)
main()


# 
