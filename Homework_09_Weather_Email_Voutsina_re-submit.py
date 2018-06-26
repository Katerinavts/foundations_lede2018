
# coding: utf-8

# In[46]:


import requests


# In[47]:


url = "https://api.darksky.net/forecast/774ea94cf1327518daefd039a796df62/40.7128,-74.0060"
response = requests.get(url)
response


# In[48]:


data = response.json()


# In[49]:


data.keys()
data 


# In[50]:


daily_forecasts[0].keys()


# In[51]:


daily_forecasts = data['daily']['data']
day = data['daily']['data'][0]

print("Right now it is", data['currently']['temperature'], "degrees out and", data['currently']['summary'])

temp = day['temperatureMax']
temp2 = day['temperatureMin']
temp_feel = day['apparentTemperatureHigh']

print(" Today will be", temp_feel,  "with a high of", temp, " and a low of", temp2)
print ('----------------------')
part1 = ''
if temp > 85:
        part1 = "It is going to be hot out!"
elif temp > 65:
        part1 = "It is going to be warm out."
else:
        part1 = "It is going to be cold out."
        
part2 = ''
rain = day['precipProbability']  
if rain > 0:
        part2 = " It is rainy today!  Bring your umbrela"


# In[52]:


feeling = "Right now it is " + str(data['currently']['temperature']) +  " degrees out and " +  str.lower(data['currently']['summary'])
temp_today = " Today will be " + str(temp_feel) + " with a high of " + str(temp) + " and a low of " + str(temp2)


# In[53]:


import datetime
right_now = datetime.datetime.now()
date_string = right_now.strftime("%B %d, %Y")


# In[54]:


date_string


# In[55]:


requests.post(
        "hasbeendeleted",
        auth=("api", "hasbeendeleted0"),
        data={"from": "ME" <"hasbeendeleted">",
              "to": ["hasbeendeleted", ""],
              "subject": "8AM Weather Forecast:"+date_string,
              "text": feeling+ temp_today+ part1+ part2}) 

