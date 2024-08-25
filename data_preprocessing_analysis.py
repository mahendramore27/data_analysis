#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


raw_csv_data = pd.read_csv('D:/Course/Excel_Data and DB/Data_file/Absenteeism_data.csv')


# In[3]:


raw_csv_data


# In[4]:


#Copy the data
df = raw_csv_data.copy()
df


# In[5]:


df.head()


# In[6]:


df.tail()


# In[7]:


pd.options.display.max_columns = None   #display all the coulumn and row
pd.options.display.max_rows = None


# In[8]:


display(df)


# In[9]:


#Check information about data dtype, non-null, memory
df.info()  #print a concise summary of the Data Frame


# In[10]:


#df.describe()
round(df.describe(),2)  #round by 2


# In[11]:


#Check null value in column
print(df.isnull().sum())


# In[12]:


#Drop ID
#df.drop(['ID'], axis = 1)  # permaently remove


# In[13]:


#Check duplicate value
print(df['ID'].duplicated().sum())


# In[14]:


#drop duplicte
print(df.drop_duplicates('ID'))


# In[15]:


#missing value
print(df.isnull().sum())


# In[16]:


#drop null value value
#print(df.dropna())


# In[17]:


#nan value replavc 30000
#print(df.replace(np.nan,30000))


# In[18]:


#replace nan value to 30000
#df['Salary'] = df['Salary'].replace(np.nan, 30000)


# In[20]:


x = df['Salary'].mean()   #mean, median, mode()[]
df['Salary'].fillna(x, inplace = True)


# In[21]:


# Round the 'Salary' column to two decimal places
df['Salary'] = df['Salary'].round(2)


# In[22]:


df.head(10)


# In[23]:


#use to group the data
df.groupby('Gender').mean()


# In[24]:


print(df['Salary'].mean())


# In[25]:


#bfill backword fill method and ffill backword fill method
#df['Gender'].fillna('Other') - Other add in the blank column
df['Gender'].fillna(method = "bfill")


# In[26]:


df.head()


# In[27]:


df['Gender'].fillna(method = "bfill", inplace = True)


# In[28]:


df.head()


# In[29]:


print(df.isnull().sum())


# In[30]:


#max
df['Reason for Absence'].max()


# In[31]:


#min
df['Reason for Absence'].min()


# In[32]:


#Check unique value
pd.unique(df['Reason for Absence'])


# In[33]:


df['Reason for Absence'].unique() #OR same output


# In[34]:


#len of unique column
len(df['Reason for Absence'].unique())


# In[35]:


#Sort column
sorted(df['Reason for Absence'].unique())


# get_dummies()

# In[36]:


Reason_columns = pd.get_dummies(df['Reason for Absence'])


# In[37]:


display(Reason_columns)


# In[38]:


Reason_columns['check'] = Reason_columns.sum(axis = 1)  #This is a row wise sum


# In[39]:


display(Reason_columns)


# In[40]:


Reason_columns['check'].sum(axis = 0) #Column sum 


# In[41]:


Reason_columns['check'].unique()


# In[42]:


Reason_columns = Reason_columns.drop(['check'],axis = 1) #Row wise columns remove


# In[43]:


display(Reason_columns)


# Group reason for Absence

# In[44]:


df.columns.values


# In[45]:


Reason_columns.columns.values


# In[46]:


df = df.drop(['Reason for Absence'], axis = 1)


# In[47]:


df.head()


# In[48]:


#Reason_coulumn 1 : 28 value can split to 1:4 show the value 
Reason_columns.loc[:, 1:14].max(axis = 1)


# In[49]:


#To combine dummmies variable reason_columns for the reange to Group it
reason_type1 = Reason_columns.loc[:, 1:14].max(axis = 1)
reason_type2 = Reason_columns.loc[:, 15:17].max(axis = 1)
reason_type3 = Reason_columns.loc[:, 18:21].max(axis = 1)
reason_type4 = Reason_columns.loc[:, 22:].max(axis = 1)


# Concaternate .concat() columns value

# In[50]:


df.head()


# In[51]:


df = pd.concat([df,reason_type1,reason_type2,reason_type3, reason_type4], axis = 1)


# In[52]:


df.head(10)


# In[53]:


df.columns.values


# In[54]:


column_names = ['ID', 'Date', 'Gender', 'Transportation Expense',
       'Distance to Work', 'Age', 'Daily Work Load Average',
       'Body Mass Index', 'Education', 'Children', 'Pets',
       'Absenteeism Time in Hours', 'Salary', 'reason_1', 'reason_2', 'reason_3', 'reason_4']


# In[55]:


df.columns = column_names


# In[56]:


df.head()


# Reorder columns

# In[57]:


columns_name_reorder = ['ID', 'reason_1', 'reason_2', 'reason_3', 'reason_4', 'Date', 'Gender', 
                        'Transportation Expense', 'Distance to Work', 'Age', 'Daily Work Load Average', 
                        'Body Mass Index', 'Education', 'Children', 'Pets', 'Absenteeism Time in Hours', 'Salary']


# In[58]:


df = df[columns_name_reorder]


# In[59]:


df.head()


# In[60]:


# Round the 'Salary' column to 0 decimal places and convert to integer
df['Salary'] = df['Salary'].round(0).astype(int)


# In[61]:


df.head()


# Create a check point 

# In[62]:


df_reason_mod = df.copy()


# In[63]:


df_reason_mod.head()


# Date:

# In[64]:


type(df_reason_mod['Date'])  #Date is 07/07/2015


# In[65]:


type(df_reason_mod['Date'][0])


# In[66]:


#Coverted timestamp pd.to_datetime()
df_reason_mod['Date'] = pd.to_datetime(df_reason_mod['Date'])


# In[67]:


df_reason_mod['Date'] #Date 2015-07-07 year-month-day


# In[68]:


type(df_reason_mod['Date'][0])


# In[69]:


#Format %d day, %m month, %Y year , %H hour, %M minute  %S secound
df_reason_mod['Date'] = pd.to_datetime(df_reason_mod['Date'], format = '%d /%m /%Y')


# In[70]:


type(df_reason_mod['Date'][0])


# In[71]:


df_reason_mod.info() #Date type see


# In[72]:


#Extract the month value
df_reason_mod['Date'][0]


# In[73]:


df_reason_mod['Date'][0].month


# In[74]:


df_reason_mod['Date'][0].year


# In[75]:


df_reason_mod['Date'][0].day


# In[76]:


df_reason_mod['Date'][699]


# In[77]:


#WeekDay
df_reason_mod['Date'][0].weekday()


# In[78]:


list_month = []


# In[79]:


list_month


# In[80]:


df_reason_mod.shape


# In[81]:


for i in range(df_reason_mod.shape[0]):
    list_month.append(df_reason_mod['Date'][i].month)


# In[82]:


#Same as for loop
#for i in range(700):
#    list_month.append(df_reason_mod['Date'][i].month)


# In[83]:


list_month


# In[84]:


len(list_month)


# In[85]:


df_reason_mod['Month Value'] = list_month


# In[86]:


df_reason_mod.head()


# In[87]:


df_reason_mod['Date'][0]


# In[88]:


def date_to_weekday(date_value):
    return date_value.weekday()


# In[89]:


df_reason_mod['Day of the week'] = df_reason_mod['Date'].apply(date_to_weekday)


# In[90]:


df_reason_mod.head()


# In[91]:


df_reason_date_mod = df_reason_mod.copy()


# In[92]:


df_reason_date_mod.head()


# In[93]:


type(df_reason_date_mod['Transportation Expense'][0])


# In[94]:


type(df_reason_date_mod['Distance to Work'][0])


# In[95]:


type(df_reason_date_mod['Age'][0])


# In[96]:


type(df_reason_date_mod['Daily Work Load Average'][0])


# In[97]:


type(df_reason_date_mod['Body Mass Index'][0])


# In[98]:


#Eduction Children pets


# In[99]:


df_reason_date_mod.head()


# In[100]:


df_reason_date_mod['Education'].unique()


# In[101]:


df_reason_date_mod['Education'].value_counts()


# In[102]:


#converted into 2 part only (0,1)  1 - high school 2 graduate 3 post graduate 4 a master or a doctor
df_reason_mod['Education'] = df_reason_date_mod['Education'].map({1:0, 2:1, 3:1, 4:1})


# In[103]:


df_reason_mod['Education'].unique()


# In[104]:


df_reason_mod['Education'].value_counts()


# Final Check point

# In[105]:


df_preprocessed = df_reason_mod.copy()
df_preprocessed.head()


# In[ ]:




