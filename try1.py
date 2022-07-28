#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import pygal
import numpy as np
from sklearn.cluster import DBSCAN


# In[3]:


from IPython.display import display, HTML
base_html = """
<!DOCTYPE html>
<html>
  <head>
  <script type="text/javascript" src="http://kozea.github.com/pygal.js/javascripts/svg.jquery.js"></script>
  <script type="text/javascript" src="https://kozea.github.io/pygal.js/2.0.x/pygal-tooltips.min.js""></script>
  </head>
  <body>
    <figure>
      {rendered_chart}
    </figure>
  </body>
</html>
"""


# In[4]:


dataFrame = pd.read_json(r"C:\Users\GEORGIE\Downloads\MOCK2.json")
dataFrame.head()


# In[5]:


disp_dict = {}
for index, row in dataFrame.iterrows():
    if row['user'] not in disp_dict.keys():
        disp_dict[row['user']] = [(row['Latitude'], row['Longitude'])]
    else:
        disp_dict[row['user']].append((row['Latitude'], row['Longitude']))
xy_chart = pygal.XY(stroke=False)
[xy_chart.add(k,v) for k,v in sorted(disp_dict.items())]
display(HTML(base_html.format(rendered_chart=xy_chart.render(is_unicode=True))))


# In[6]:


safe_distance = 0.0018288 # a radial distance of 6 feet in kilometers
model = DBSCAN(eps=safe_distance, min_samples=2, metric='haversine').fit(dataFrame[['Latitude', 'Longitude']])
core_samples_mask = np.zeros_like(model.labels_, dtype=bool)
core_samples_mask[model.core_sample_indices_] = True
labels = model.labels_
dataFrame['Cluster'] = model.labels_.tolist()


# In[7]:


disp_dict_clust = {}
for index, row in dataFrame.iterrows():
    if row['Cluster'] not in disp_dict_clust.keys():
        disp_dict_clust[row['Cluster']] = [(row['Latitude'], row['Longitude'])]
    else:
        disp_dict_clust[row['Cluster']].append((row['Latitude'], row['Longitude']))
print(len(disp_dict_clust.keys()))
from pygal.style import LightenStyle
dark_lighten_style = LightenStyle('#F35548')
xy_chart = pygal.XY(stroke=False, style=dark_lighten_style)
[xy_chart.add(str(k),v) for k,v in disp_dict_clust.items()]
display(HTML(base_html.format(rendered_chart=xy_chart.render(is_unicode=True))))


# In[8]:


inputName = "Dave"
inputNameClusters = set()
for i in range(len(dataFrame)):
    if dataFrame['user'][i] == inputName:
        inputNameClusters.add(dataFrame['Cluster'][i])


# In[9]:


infected = set()
for cluster in inputNameClusters:
    if cluster != -1:
        namesInCluster = dataFrame.loc[dataFrame['Cluster'] == cluster, 'user']
        for i in range(len(namesInCluster)):
            name = namesInCluster.iloc[i]
            if name != inputName:
                infected.add(name)
                    


# In[ ]:




