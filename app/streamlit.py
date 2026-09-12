import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st

from pages_content.upload import render_upload
from pages_content.preview import render_preview
from pages_content.cleaning import render_cleaning
from pages_content.summary import render_summary
from pages_content.visualization import render_visualization
from pages_content.ai_chat import render_ai_chat
from pages_content.chat import render_chat
from pages_content.insights import render_insights

st.set_page_config(page_title="AI Data Analyst", page_icon="📊", layout="wide")

# --- Simple custom styling ---
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #4b6cb7, #182848);
        padding: 24px;
        border-radius: 10px;
        color: white;
        margin-bottom: 20px;
    }
    .main-header h1 { margin: 0; color: white; }
    .main-header p { margin: 4px 0 0 0; color: #dbe4ff; }
    div[data-testid="stMetric"] {
        background-color: #f5f7fb;
        border: 1px solid #e0e4ee;
        border-radius: 8px;
        padding: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- Header banner ---
st.markdown("""
<div class="main-header">
    <h1>🤖 AI Data Analyst</h1>
    <p>Chat With Your CSV — Upload, clean, analyze, visualize, and ask questions about your data.</p>
</div>
""", unsafe_allow_html=True)

with st.expander("ℹ️ About this app & how it works", expanded=False):
    st.write(
        "This application lets you upload a CSV file and explore it step by step — "
        "clean the data, view statistics and charts, ask questions in plain English, "
        "and get AI-generated insights."
    )

    st.markdown("""
    **Workflow**

    📂 Upload CSV → 🧹 Clean Data → 📊 Analyze Data → 📈 Visualize → 💬 Ask Questions → 🤖 Get AI Insights
    """)

    st.markdown("""
    **Key Features**
    - 📂 CSV Upload
    - 📊 Data Analysis
    - 📈 Interactive Visualizations
    - 💬 Natural Language Questions
    - 🤖 AI-Powered Insights
    """)

    st.markdown("""
    **Quick Start**
    1. Upload a CSV file from the sidebar.
    2. Preview and clean your dataset in the tabs below.
    3. Explore statistics and charts.
    4. Ask questions in natural language.
    5. Generate AI-powered insights.
    """)

# --- Upload always visible in sidebar ---
render_upload()

# --- Organize the rest into tabs ---
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "🔍 Preview", "🧹 Cleaning", "📈 Summary", "📊 Visualization", "💬 Ask Your Data", "🤖 AI Assistant", "✨ AI Insights"
])

with tab1:
    render_preview()

with tab2:
    render_cleaning()

with tab3:
    render_summary()

with tab4:
    render_visualization()

with tab5:
    render_chat()

with tab6:
    render_ai_chat()

with tab7:
    render_insights()