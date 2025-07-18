import streamlit as st
import pandas as pd
import os
from modules.data_processor import DataProcessor

# Configure page
st.set_page_config(
    page_title="Data Analytics Platform",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'data' not in st.session_state:
    st.session_state.data = None
if 'processed_data' not in st.session_state:
    st.session_state.processed_data = None
if 'data_processor' not in st.session_state:
    st.session_state.data_processor = DataProcessor()

# Main page
st.title("📊 Data Analytics Platform")
st.markdown("### AI-Powered Data Insights and Exploration")

# Sidebar navigation info
with st.sidebar:
    st.markdown("## Navigation")
    st.markdown("Use the pages in the sidebar to:")
    st.markdown("- 📁 **Data Upload**: Upload and preview your datasets")
    st.markdown("- 🔍 **Data Exploration**: Interactive data analysis")
    st.markdown("- 🤖 **AI Chatbot**: Chat with your data using natural language")
    st.markdown("- 💡 **Insights Generator**: Automated trend detection")
    
    # Data status
    st.markdown("## Data Status")
    if st.session_state.data is not None:
        st.success(f"✅ Data loaded: {st.session_state.data.shape[0]} rows, {st.session_state.data.shape[1]} columns")
    else:
        st.warning("⚠️ No data loaded")

# Main content
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 📁 Data Upload
    Upload CSV or Excel files to start analyzing your data. The platform supports various data formats and automatically detects data types.
    """)

with col2:
    st.markdown("""
    ### 🔍 Data Exploration
    Interactive visualizations and statistical analysis tools to explore your data patterns and relationships.
    """)

with col3:
    st.markdown("""
    ### 🤖 AI Chatbot
    Ask questions about your data in natural language. Get insights, trends, and answers powered by AI.
    """)

# Quick start section
st.markdown("## Quick Start")
st.markdown("1. **Upload your data** using the Data Upload page")
st.markdown("2. **Explore your data** with interactive visualizations")
st.markdown("3. **Chat with your data** using natural language queries")
st.markdown("4. **Generate insights** automatically from your datasets")

# Sample queries section
if st.session_state.data is not None:
    st.markdown("## Sample Questions for AI Chatbot")
    sample_questions = [
        "What are the main trends in this dataset?",
        "Show me correlations between variables",
        "What are the outliers in the data?",
        "Summarize the key statistics",
        "What patterns do you see in the data?"
    ]
    
    for question in sample_questions:
        st.markdown(f"- {question}")
