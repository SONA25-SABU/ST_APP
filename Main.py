import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Read the CSV file
@st.cache_data
def load_data():
    df = pd.read_csv('CLOTH.csv')
    return df

# Load the data
df = load_data()

# Display the CSV file
st.write(df)

# 3D Scatter Plot
st.subheader('3D Scatter Plot')
fig_scatter = plt.figure()
ax_scatter = fig_scatter.add_subplot(111, projection='3d')
ax_scatter.scatter(df['Age'], df['Rating'], df['Positive Feedback Count'], c=df['Recommended IND'])
ax_scatter.set_xlabel('Age')
ax_scatter.set_ylabel('Rating')
ax_scatter.set_zlabel('Positive Feedback Count')
st.pyplot(fig_scatter)



# Run the app
if __name__ == "__Main__":
    main()
