
# coding: utf-8

# In[7]:


for x in range(1,10):
    if(x<6):
        for y in range(1,x+1):
            print("*",end=" ")
    else:
        for y in range(1,11-x):
            print("*",end=" ")
    print()

