#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 


# In[2]:


data1=pd.read_csv('Sales_April_2019.csv')


# In[3]:


data2=pd.read_csv('Sales_August_2019.csv')


# In[7]:


data=pd.concat([data1,data2])
data


# #cleaning data

# In[11]:


data.isna().sum()


# In[12]:


data=data.dropna(how='all')


# In[17]:


data=data[data['Order Date'].str[0:2]!='Or']
data


# In[19]:


data['Quantity Ordered']=pd.to_numeric(data['Quantity Ordered'])
data['Price Each']=pd.to_numeric(data['Price Each'])


# In[20]:


data.head()


# In[ ]:





# In[18]:


data['Month']=data['Order Date'].str[0:2]
data['Month']=data['Month'].astype('int32')
data


# add sales column

# In[21]:


data['Sales']=data['Quantity Ordered']*data['Price Each']


# In[22]:


data


# what is the best month for sales

# In[29]:


results=data.groupby('Month').sum()
results


# In[ ]:





# what is city had th heighst number of sales

# In[35]:


data


# In[ ]:


#add city column 


# In[50]:



data['city ']=data['Purchase Address'].apply(lambda x: x.split(',')[1]+''+x.split(',')[2].split(' ')[1])


data


# In[58]:


result2=data.groupby('city ').sum()
result2


# In[64]:


cities=[city for city ,df in data.groupby('city ')]
plt.bar(cities,result2['Sales'])
plt.xticks(cities,rotation='vertical',size=8)
plt.xlabel('city name')
plt.ylabel('price')
plt.show()


# In[ ]:





# In[70]:


data['Order Date']=pd.to_datetime(data['Order Date'])
data['Hour']=data['Order Date'].dt.hour
data['date']=data['Order Date'].dt.date
data['minute']=data['Order Date'].dt.minute
data
data


# In[75]:



hours=[hour for hour ,df in data.groupby('Hour')]
plt.plot(hours,data.groupby('Hour').count())
plt.xticks(hours)
plt.xlabel('hour')
plt.ylabel('number of order')
plt.grid()
plt.show()


# In[78]:


#top 10 products
top_product=data.sort_values(by='Sales',ascending=False)
top_product=high_product.head(10)
print(top_product['Product'])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




