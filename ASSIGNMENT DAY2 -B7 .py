#!/usr/bin/env python
# coding: utf-8

# #  1. LIST  AND ITS DEFAULT FUNCTIONS 

# In[4]:


lst =  [ "ketan", 1, 2, 3, 4, [ 21, 22, 23]]


# In[5]:


lst


# In[8]:


lst.append("ketan1")


# In[9]:


lst[0]


# In[10]:


lst


# In[12]:


lst[5][2]


# In[13]:


lst[-2]


# In[14]:


lst[-2][-1]


# In[15]:


lst.count(lst)


# In[22]:


lst.count(lst[3])


# In[23]:


lst.pop()


# In[24]:


lst.remove("ketan")


# In[25]:


lst


# In[30]:


lst.append("ketan1""ketan2" "ketan3")


# In[31]:


lst


# # 2. Dictionary AND ITS DEFAULT FUNCTIONS

# In[32]:


dit = { " name ": " Ketan ", " age ": "25" , 
      "number": 123456789 , " email ": "ketan.sharma095"}


# In[33]:


dit


# In[34]:


#retrieving a value from dictionary 

dit.get(' name ')


# In[35]:


dit


# In[39]:


dit.pop(' name ')


# In[40]:


dit.pop('number')


# In[41]:


dit


# In[45]:


dit.update()


# In[46]:


dit


# In[48]:


dit.update(dit)


# In[49]:


dit


# In[50]:


dit.items()


# In[54]:


dit


# #  3. SETS AND ITS FUNCTIONS 

# In[55]:


# Sets are used for storing unique values in the python,
# Sets are complex data structures.
# Sets are Class in Python , whose object can be derived 
# Sets are mostly used for finding UNION ,disjoin and findings common and uncommons in the python data type


# In[56]:


st = {"ketan","letsupgrade",1,2,3,4,5,6,7,8,9 }


# In[57]:


st


# In[58]:


st1 ={"sharma", "letsupgrade", 21, 22, 23, 24 }


# In[59]:


st.issuperset(st1)


# In[60]:


st2 = { "ketan", 5}


# In[61]:


st2


# In[62]:


st1


# In[63]:


st2.issubset(st)


# In[64]:


st2.issubset(st1)


# In[65]:


st.issuperset(st2)


# In[67]:


st.add('56,57,')


# In[68]:


st


# In[69]:


st1.union(st)


# In[70]:


st


# In[71]:


st1


# In[75]:


st.update('sharma123')


# In[73]:


st


# In[76]:


st


# In[78]:


st.remove('ketan')


# In[79]:


st


# # 4. TUPLES AND ITS FUNCTIONS

# In[80]:


# Tuples are ORDERED immutable collection/sequence of objects 
# Once the data is written its in that forever
# it cant be changed


# In[81]:


tup = ("ketan",'@',".sharma095")


# In[83]:


tup


# In[86]:


tup.count('.sharma095')


# In[87]:


tup.index('@')


# In[88]:


tup


# # 5. STRINGS AND ITS FUNCTIONS

# In[89]:


name = 'sarabjit'
name1 = 'mercury man '


# In[91]:


name


# # 

# In[92]:


name1


# In[96]:


name+ ' is a ' +name1


# In[97]:


type(name)


# In[98]:


name.capitalize()


# In[99]:


name


# In[100]:


name1.capitalize()


# In[105]:


name3 = name.join(name1)


# In[106]:


name3


# In[108]:


name3.count(name)


# In[109]:


name


# In[110]:


name3


# In[111]:


name1.index(name1)


# In[112]:


name3.index(name3)

