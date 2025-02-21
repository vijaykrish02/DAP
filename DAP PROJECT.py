#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[2]:


import pandas as pd
data=pd.read_csv(r'C:\Users\raji0\OneDrive\Documents\anudip\Anudip Project\Netflix_userdatasets.csv')
print(data)


# In[24]:


import pandas as pd 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
data=pd.read_csv(r'C:\Users\raji0\OneDrive\Documents\anudip\Anudip Project\Netflix_userdatasets.csv')
print(data.head())


# In[25]:


print(data.head(10))


# In[41]:


print(df.tail(4))


# In[42]:


data.describe()


# In[15]:


data.isnull().sum() #checking the null values


# In[16]:


data.columns #check the column names


# In[57]:


counts = data['Gender'].value_counts()# Replace 'Category' with the actual column name
myexplode=[0.05,0.02]
plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=140, colors=['red', 'blue'],explode=myexplode)
plt.title("Category Distribution in Dataset")
plt.legend(title='Gender Distribution',loc='upper left')
plt.show()


# In[29]:


plt.figure(figsize=(8, 5))
sns.countplot(x='Subscription Type', data=df, palette='coolwarm')  # Replace with actual column name
plt.title("Number of Users per Subscription Type")
plt.xlabel("Subscription Type")
plt.ylabel("Count")
plt.show() 


# In[65]:


data.columns


# In[69]:


x=data['Age']
y=data['Country']
plt.scatter(x,y,color='m',alpha=0.2)
plt.xlabel('Age')
plt.ylabel('Country')
plt.title('Scatter Distribution of AGE vs COUNTRY')
plt.show()


# In[72]:


print(data.duplicated().sum())


# In[88]:


plt.figure(figsize=(8, 5))
plt.hist(df['Age'], bins=15, color='blue', edgecolor='black', alpha=0.7)  # Adjust bins as needed
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age Distribution of Netflix Users")
plt.show()


# In[135]:


plt.figure(figsize=(8, 5))
plt.hist(df['Monthly Revenue'],bins=10, color='green', edgecolor='black', alpha=0.7)
plt.xlabel("Monthly Revenue ($)")
plt.title("Monthly Revenue Distribution of Netflix Users") 
plt.show()


# In[151]:


plt.figure(figsize=(20,10))
plt.hist(df['Country'], bins=30, color='purple', edgecolor='black', alpha=0.8)
plt.xlabel("Country")
plt.ylabel("Frequency")
plt.title("Watching Hours Distribution by Country")
plt.show()



# In[90]:


plt.figure(figsize=(8, 5))
plt.boxplot(df['Monthly Revenue'], patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.xlabel("Monthly Spending")
plt.ylabel("Amount ($)")
plt.title("Box Plot for Monthly Revenue")
plt.show()


# In[97]:


import seaborn as sns

plt.figure(figsize=(8, 5))
sns.violinplot(y=df['Age'], color='purple')

# Add labels and title
plt.title("Violin Plot for Age Distribution")
plt.ylabel("Age")

# Show plot
plt.show()


# In[100]:


plt.figure(figsize=(8, 5))
sns.violinplot(x=df['Age'], y=df['Subscription Type'], palette='coolwarm')  # Replace column names

# Add labels and title
plt.xlabel("Subscription Type")
plt.ylabel("Monthly Revenue")
plt.title("Violin Plot for Monthly Revenue per Subscription Type")

# Show plot
plt.show()


# In[102]:


Dummy=data.drop(columns=['Monthly Revenue'])
Dummy


# In[109]:


sns.lineplot(data=data,x='Subscription Type',y='Device')


# In[118]:


a=np.random.randint(100,size=(100))
b=np.random.randint(100,size=(100))
colors=np.random.randint(100,size=(100))
sizes=10*np.random.randint(100,size=(100))

plt.scatter(a,b,c=colors,cmap='nipy_spectral',s=sizes,alpha=0.6)
plt.xlabel('Monthly Revenue')
plt.ylabel('Subscription Type')
plt.colorbar()
plt.title('Monthly revenue VS Subscription Type')
plt.show()


# In[119]:


datasets=sns.get_dataset_names()
print(datasets)


# In[120]:


data_sets=sns.load_dataset('diamonds')
data_sets


# In[126]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r'C:\Users\raji0\OneDrive\Documents\anudip\Anudip Project\Netflix_userdatasets.csv')

# Select only two numerical columns (replace 'Column1' and 'Column2' with actual column names)
selected_columns = df[['Age','Monthly Revenue']]  # Example: Replace with your columns

# Compute correlation
correlation_matrix = selected_columns.corr()

# Print correlation matrix
print(correlation_matrix)


# In[128]:


plt.figure(figsize=(5, 4))  # Set figure size
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=1, square=True)

# Add title
plt.title("Heatmap of Monthly Revenue Vs Age")

# Show plot
plt.show()


# In[129]:


pivot_table = df.pivot_table(values='Monthly Revenue', index='Age', columns='Subscription Type', aggfunc='mean')

# Print Pivot Table
print(pivot_table)


# In[163]:


counts = data['Country'].value_counts()# Replace 'Category' with the actual column name
myexplode=[0.05,0.02,0.03,0.02,0.02,0.02,0.02,0.02,0.02,0.02]
plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=140,explode=myexplode)
plt.title("Country Distribution in Dataset")
plt.show()


# In[180]:


counts = data['Subscription Type'].value_counts()
myexplode=[0.07,0.02,0.06]
plt.pie(counts,labels=counts.index, autopct='%1.1f%%', startangle=140,explode=myexplode,colors=['red','green','purple'])
plt.title("Subscription Type Distribution using piechart")
plt.show()


# In[ ]:




