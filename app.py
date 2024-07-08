# Import the Streamlit library
import streamlit as st
import numpy as np
import pandas as pd
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)


# Create a new DataFrame 'dataframe2' with random data
dataframe2 = pd.DataFrame(
    np.random.randn(10, 20),  # Generate a 10x20 array of random numbers
    columns=('col %d' % i for i in range(20)))  # Create column names 'col 0' to 'col 19'

# Display the DataFrame using Streamlit's dataframe function
# Apply styling to highlight the maximum value in each column
st.dataframe(dataframe2.style.highlight_max(axis=0))

dataframe3 = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe3)


chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

'''---'''
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)
'''code of silder'''
'''
```python
x = st.silder('x')
st.srite(x, 'squared is', x*x)
```
'''
'''---'''
st.text_input("Your name", key="name")
st.session_state.name
'''code of text input'''
'''
```python
st.text_input("Your name", key="name")
st.session_state.name
```
'''
'''---'''
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])
    st.line_chart(chart_data)
'''code of checkbox'''
'''
```python
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])
    st.line_chart(chart_data)
```
'''
'''---'''
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
    })
option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option
'''code of selectbox'''
'''
```python
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
    })
option = st.selectbox(
    'Which number do you like best?',
     df['first column'])
'You selected: ', option
```
'''
'''---'''

add_selectbox2=st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

add_silde2=st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
add_silde3=st.sidebar.text(
'''code of sidebar
```python
add_selectbox2=st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

add_silde2=st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
```
''')
left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!") 


import streamlit as st
import time

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

