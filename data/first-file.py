#!/usr/bin/env python
# coding: utf-8

# In[22]:


from bokeh.plotting import figure,output_file,show
import pandas

df = pandas.read_csv("./HistoryExchangeReport.csv",parse_dates=["Date"])




# In[39]:


p = figure(width=1000,height=800,title="Currency updown Rate",x_axis_type="datetime",tools=[''])
p.toolbar.logo=None
p.line(df["Date"],df["Rate"])
output_file("first-file.html")
show(p)

