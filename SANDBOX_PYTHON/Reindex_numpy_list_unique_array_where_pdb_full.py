#!/usr/bin/env python
# coding: utf-8

# In[26]:


import numpy as np

A = np.array([(1,2,4),(5,3,7),(8,3,6)])
print(A)
print(np.unique(A))
print()

B = A[1:,1:]
print('B=',B)
print()


#Initially I wanted to look for min but we will see that np.unique allows us to find each value of interest in B :)
    #Id_init = np.unique(B)
    #print(Id_init)
    #print(B.min())
    #print(np.argmin(B))
    #print(np.amin(B))


#Best solution turns out to be np.where function

List = np.where(B == np.amin(B))
print('List=',List)
print(type(List))
print()

List_test_2 = np.where(B == np.unique(B))
print('List=',List_test_2)
print(type(List_test_2))
print()

ListOfCoordinates = list(zip(List[0], List[1]))
print('ListOfCoordinates=',ListOfCoordinates)
print(type(ListOfCoordinates))
print()

print('########################### FOR INFORMATION ###########################')
###Conversion is useless we can use directly the ListOfCoordinates to extract the value of interest in B ###
#We keep active those functions to show their nature
ListArray = np.array(ListOfCoordinates)
print('ListArray=',ListArray)
print(type(ListArray))
print()

ListArray_row0 = ListArray[0]
print('ListArray_row0=',ListArray_row0)
print(type(ListArray_row0))
print('ListArray_row0[0]=',ListArray_row0[0])
print(type(ListArray_row0[0]))
print()

x = B [1]
print('x=',x)
print(type(x))
print()

y = B [1,1]
print('y=',y)
print(type(y))
print()

z = B[[1,1]]
print('z=',z)
print(type(z))
print()


print('#####################################################################')
print()

#THE ONLY USEFULE NOTATION IN THIS PROBLEM:
w = B[(1,1)]
print('w=',w)
print(type(w))
print()

#C = B[:] #Initialize the target array. #CAUTION: With this instruction, every modification on C will be applied on B
C = np.zeros((2,2), dtype=int)# Instead we prefer to initialize an empty array same size than B
print('C=',C)
C[ListOfCoordinates[0]] = 1 # = C[(0,0)] Voir la liste ListOfCoordinates
C[ListOfCoordinates[1]] = 1 # = C[(1,0)] Voir la liste ListOfCoordinates

print('C=',C)
print('B=',B) 


# In[21]:


print('unique_id_list_B=',np.unique(B))
print(type(np.unique(B)))


# In[49]:


D = np.zeros((2,2), dtype=int)
B_unique_ID = np.unique(B)
for i in range(len(B_unique_ID)-1):
    List_i = np.where(B == B_unique_ID[i])
    ListOfCoordinates_i = list(zip(List_i[0], List_i[1]))
    for k in range(len(ListOfCoordinates_i) - 1):
        import pdb, pdb.set_trace()
        D[ListOfCoordinates_i[k]] = i + 1
print(D)
    


# In[45]:


print(len(B_unique_ID))


# In[46]:


print(B_unique_ID)


# In[ ]:




