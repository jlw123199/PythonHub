
# With the following command to start a steramlit service:
#
# streamlit run streamlit-app.py

import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import time


st.title('Streamlit Application')

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))


# for python 3
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

# Draw a line chart
# You can easily add a line chart to your app with st.line_chart(). We’ll generate a random sample using Numpy and then chart it.

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


# Plot a map
# With st.map() you can display data points on a map. Let’s use Numpy to generate some sample data and plot it on a map of San Francisco.

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

# st.map(map_data)

# Add interactivity with widgets
# With widgets, Streamlit allows you to bake interactivity directly into your apps with checkboxes, buttons, sliders, and more. Check out our API reference for a full list of interactive widgets.
#
# Use checkboxes to show/hide data
# One use case for checkboxes is to hide or show a specific chart or section in an app. st.checkbox() takes a single argument, which is the widget label. In this sample, the checkbox is used to toggle a conditional statement.

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)



'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'

