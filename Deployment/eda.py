import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run(): # Agar ga langsung muncul pada saat disatuin di satu app

    st.sidebar.title('StreamThis Streaming Platform')
    st.sidebar.title('About this page')
    st.sidebar.write('This page describes the Customers behaviour from StreamThis Platform and their likelihood to Churn')


    st.title('StreamThis Customers Analysis')

    st.write('This is a Data Analysis from StreamThis Customer Behaviour')

    st.image('https://delighted.com/wp-content/uploads/2022/08/customer-churn-2022-08-feat-2.png?w=1200', width=800, caption='Churn Customer')

    st.write('## Data Information:')
    st.write('This is the data from Customers StreamThis')
    st.write('This data contains the customers behaviour in the StreamThis Service and their likelihood to leave our services')

    df = pd.read_csv("Milestone2_Daffa.csv", index_col = 0)
    df.dropna(inplace = True)
    col_int = ['Age', 'Tenure', 'Usage Frequency', 'Support Calls', 'Payment Delay', 'Total Spend', 'Last Interaction', 'Churn']
    df[col_int] = df[col_int].astype(int)
    st.dataframe(df)

    

    # Visualization 1
    st.write('## Data Visualization Count within Categorical Column')
    edacat_col = ['Gender', 'Subscription Type', 'Contract Length', 'Churn']
    plt.figure(figsize=(6,3))  


    for i, col in enumerate(edacat_col[:3], start=1):
        '''
        Function to plot each categorical column count related with the target label
        Iterate for the categorical column except for the churn column
        '''
        st.subheader(f'Count Plot of {col}')
        
        # Create a Matplotlib figure and axis
        fig, ax = plt.subplots(figsize = (7,5))
        
        # Group by churn with related column
        counts = df.groupby(['Churn', col]).size().reset_index(name='count')
        
        # Plotting
        sns.barplot(x='Churn', y='count', hue=col, data=counts, ax=ax)
        
        # Setting the title column
        ax.set_title(f'Count Plot of {col}')
        
        # Display the plot
        st.pyplot(fig)


    st.write('## Data Distribution')
    option = st.selectbox('Choose Statistics',
                        options= ['Age', 'Tenure', 'Usage Frequency', 'Support Calls', 'Payment Delay', 'Total Spend', 'Last Interaction'])


    # Visualization 2 - Distribution 
    st.write(f'### Distribution {option}')
    fig = plt.figure(figsize = (7,5))
    sns.distplot(df[option])
    st.pyplot(fig) # Ini kaya plt.show
