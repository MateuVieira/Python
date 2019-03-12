
# coding: utf-8

# In[ ]:



num =[1,9,9]
for n in num:
    print(n)
print(len(num))


# In[48]:


def add_one(give_array):
    print(give_array)
    carry = 1
    i = len(give_array)-1
    while (i >= 0):
        sum = give_array[i] + carry
        give_array[i] = sum % 10
        if(sum != 10):
            carry = 0
            break
        i -= 1
  
    if(carry == 1):
        give_array[0] = 1
        give_array.append(0)
        return give_array
    
    return give_array


# In[53]:

num = [0]
for i in range(0, 100, 1):
    num = add_one(num)
    print(num)



#%%
