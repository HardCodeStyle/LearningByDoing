import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.title('Earthquake Data Explorer')
st.text('This is a web app to allow exploration of Earthquake Data')
upload_file = st.file_uploader('Upload a file containing earthquake data')

if upload_file is not None:
    # Read the file to a dataframe using pandas
    # df = pd.read_csv(upload_file)
    df = pd.read_csv(upload_file)

    st.header('Statistics of Dataframe')
    st.write(df.describe())
    # Create a section for the dataframe header
    st.header('Header of Dataframe')
    st.dataframe(df)
    print(df)
    fig, ax = plt.subplots(1, 1)
    ax.scatter(x=df['Datum'], y=df['Eröffnungskurs'])
    ax.set_xlabel('Datum')
    ax.set_ylabel('Eröffnungskurs')
    st.pyplot(fig)
