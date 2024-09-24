import streamlit as st
import pandas as pd

# Data Science Course Information
courses = [
    {
        'id': 1,
        'title': 'Foundations of Data Science',
        'description': 'Introduction to the core concepts and methods in data science.',
        'topics': [
            'Data wrangling', 
            'Data ethics', 
            'Introduction to machine learning', 
            'Data visualization'
        ]
    },
    {
        'id': 2,
        'title': 'Programming for Data Science',
        'description': 'Learn programming fundamentals with Python and R.',
        'topics': [
            'Data structures', 
            'Libraries (NumPy, Pandas)', 
            'Best practices in data manipulation'
        ]
    },
    {
        'id': 3,
        'title': 'Statistical Methods for Data Science',
        'description': 'Detailed exploration of statistical techniques used in data science.',
        'topics': [
            'Probability distributions', 
            'Hypothesis testing', 
            'Regression analysis',
            'Bayesian methods'
        ]
    },
    {
        'id': 4,
        'title': 'Big Data Analytics',
        'description': 'Focus on tools and techniques for managing and analyzing large datasets.',
        'topics': [
            'MapReduce and Hadoop',
            'Spark for big data',
            'NoSQL databases',
            'Real-time analytics'
        ]
    },
    {
        'id': 5,
        'title': 'Machine Learning',
        'description': 'Introduction to machine learning concepts and algorithms.',
        'topics': [
            'Supervised learning (regression, classification)', 
            'Unsupervised learning (clustering)', 
            'Neural networks',
            'Model evaluation and selection'
        ]
    },
    {
        'id': 6,
        'title': 'Natural Language Processing',
        'description': 'Application of machine learning techniques to natural language data.',
        'topics': [
            'Text preprocessing', 
            'Sentiment analysis', 
            'Word embeddings',
            'Applications in chatbots'
        ]
    },
    {
        'id': 7,
        'title': 'Data Visualization',
        'description': 'Techniques for communicating insights from data using visual methods.',
        'topics': [
            'Principles of graphical design',
            'Interactive visualization tools',
            'Dashboards',
            'Storytelling with data'
        ]
    },
    {
        'id': 8,
        'title': 'Cloud Computing for Data Science',
        'description': 'Utilizing cloud platforms for scalable data processing and analysis.',
        'topics': [
            'Cloud architecture (AWS, Azure)', 
            'Data storage (S3, BigQuery)', 
            'Serverless computing', 
            'Deploying machine learning models on the cloud'
        ]
    },
    {
        'id': 9,
        'title': 'Deep Learning',
        'description': 'Focused course on neural networks and deep learning applications.',
        'topics': [
            'Convolutional Neural Networks (CNNs)', 
            'Recurrent Neural Networks (RNNs)', 
            'Autoencoders and GANs',
            'Applications in image processing'
        ]
    }
]

# Sidebar for navigation
st.sidebar.title("University of Regina Data Science Program")
page = st.sidebar.selectbox("Main Navigation", ["Introduction", "Courses", "Program Statistics"])

# Introduction Page
if page == "Introduction":
    st.title("Welcome to the University of Regina Data Science Program")
    st.subheader("Program Overview")
    st.write("""
        The University of Regina's Data Science Program provides students with the tools and knowledge 
        to excel in the growing field of data science. The program offers a wide range of courses that 
        focus on core topics like machine learning, statistical methods, big data analytics, and deep learning. 
        Whether you're interested in data analysis, programming, or AI-driven solutions, our program is designed 
        to help you succeed.
    """)
    st.image("What-is-data-science-2.jpg", caption="Explore Data Science at URegina")

# Courses Page
elif page == "Courses":
    st.title("Data Science Courses")
    st.subheader("List of Courses")
    
    for course in courses:
        st.markdown(f"### {course['title']}")
        st.write(course['description'])
        st.markdown("#### Topics Covered:")
        for topic in course['topics']:
            st.write(f"- {topic}")
        st.write("---")  # Line separator

# Program Statistics Page
elif page == "Program Statistics":
    st.title("Program Statistics")

    # Sample data for program statistics
    program_fees = 12000  # Example: Tuition fees in USD
    acceptance_rate = 18   # Example: Acceptance rate in percentage
    avg_salary = 85000     # Example: Expected salary after graduation in USD

    st.write(f"**Program Fees**: ${program_fees} per year")
    st.write(f"**Acceptance Rate**: {acceptance_rate}%")
    st.write(f"**Expected Salary After Graduation**: ${avg_salary}/year")

    # Create sample data for graphical representation
    years = [1, 2, 3, 4, 5]
    avg_salary_data = [70000, 75000, 80000, 85000, 90000]
    fees_data = [12000, 12000, 12000, 12000, 12000]

    # Create DataFrames for Streamlit charts
    salary_df = pd.DataFrame({'Years After Graduation': years, 'Expected Salary ($)': avg_salary_data})
    fees_df = pd.DataFrame({'Year of Study': years, 'Tuition Fees ($)': fees_data})

    st.subheader("Expected Salary Growth Over 5 Years")
    st.line_chart(salary_df.set_index('Years After Graduation'))

    st.subheader("Tuition Fees (Fixed over 4 years)")
    st.bar_chart(fees_df.set_index('Year of Study'))

# Footer Information in Sidebar
st.sidebar.title("About")
st.sidebar.info("This application i built by kapeesh-kaul displays information about a hypothetical Data Science Program at the University of Regina, including available courses and program statistics.")