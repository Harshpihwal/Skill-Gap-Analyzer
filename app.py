import streamlit as st
import pandas as pd
import re
from modules.parser import get_resume_text
from modules.ml_engine import calculate_gap

# --- UI CONFIGURATION ---
st.set_page_config(page_title="SkillBridge AI Pro", page_icon="🧠", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #1e2130; padding: 15px; border-radius: 10px; border: 1px solid #3e4255; }
    .stButton>button { width: 100%; background-color: #ff4b4b; color: white; font-weight: bold; border-radius: 8px; height: 3em; }
    </style>
    """, unsafe_allow_html=True)

# --- 🧠 NLP PREPROCESSING LAYER (New Feature) ---
def normalize_text(text):
    
    text = text.lower()
    
    # Dictionary of common tech abbreviations
    acronyms = {
        r"\bml\b": "machine learning",
        r"\bai\b": "artificial intelligence",
        r"\bjs\b": "javascript",
        r"\bts\b": "typescript",
        r"\breactjs\b": "react",
        r"\bnode\b": "node.js",
        r"\baws\b": "amazon web services",
        r"\bdsa\b": "data structures algorithms",
        r"\bui/ux\b": "ui ux design",
        r"\bfe\b": "frontend",
        r"\bbe\b": "backend"
    }
    
    for pattern, replacement in acronyms.items():
        text = re.sub(pattern, replacement, text)
    
    return text

# --- HEADER ---
st.title("🧠 SkillBridge AI: Intelligent Gap Analyzer")
st.divider()

# --- MAIN LAYOUT ---
col_left, col_mid, col_right = st.columns([1, 3, 1])

with col_mid:
    # 1. TARGET ROLE
    st.subheader("🎯 Step 1: Select Your Target Goal")
    try:
        df = pd.read_csv("data/jobs_dataset.csv")
        target_role = st.selectbox("I want to become a:", df['Role'].unique())
    except:
        st.error("Dataset not found!")
        st.stop()
    
    st.write("")

    # 2. INPUT SKILLS
    st.subheader("⌨️ Step 2: Input Your Skills")
    
    input_method = st.radio("Method:", ["📄 Upload CV (PDF)", "⌨️ Type Skills Manually"], horizontal=True)
    user_skills_text = ""

    if input_method == "📄 Upload CV (PDF)":
        uploaded_file = st.file_uploader("Drop Resume", type="pdf")
        if uploaded_file:
            raw_text = get_resume_text(uploaded_file)
            user_skills_text = normalize_text(raw_text) # Apply NLP Cleaning
            st.success("Resume Parsed & Normalized successfully!")
    else:
        raw_input = st.text_area("Type skills (e.g., 'I know ML and JS')", height=150)
        user_skills_text = normalize_text(raw_input) # Apply NLP Cleaning

    st.write("")

    # 3. ANALYSIS ENGINE
    if st.button("🚀 Run Intelligent Analysis"):
        if user_skills_text:
            with st.spinner('Translating acronyms & analyzing gaps...'):
                
                # Get Requirements
                required_skills_str = df[df['Role'] == target_role]['Required_Skills'].values[0]
                required_skills = [s.strip() for s in required_skills_str.split(",")]
                
                # ML Engine Logic
                found, missing = calculate_gap(user_skills_text, required_skills)
                
                # Scoring
                score = (len(found) / len(required_skills)) * 100
                
                # --- RESULTS ---
                st.divider()
                c1, c2 = st.columns([1, 2])
                with c1:
                    st.metric("AI Match Score", f"{int(score)}%")
                with c2:
                    st.progress(score / 100)
                    if score > 80: st.caption("Excellent Profile!")
                
                st.write("---")
                
                rc1, rc2 = st.columns(2)
                with rc1:
                    st.success("✅ Skills Detected (AI Matched)")
                    for s in found: st.write(f"• {s}")
                with rc2:
                    st.error("🚩 Missing Skills")
                    for m in missing: st.write(f"• {m}")

                # Roadmap
                if missing:
                    st.divider()
                    st.subheader("🎓 Adaptive Learning Path")
                    for m in missing:
                        with st.expander(f"Learn {m}"):
                            st.write(f"AI suggests focusing on {m}.")
                            st.write(f"- [YouTube: {m} Full Course](https://www.youtube.com/results?search_query={m.replace(' ', '+')}+tutorial)")
        else:
            st.warning("Please enter some skills first.")

# --- FOOTER ---
st.divider()
st.caption("Powered by Natural Language Processing (NLP) | Handles Synonyms & Acronyms")