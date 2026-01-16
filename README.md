# 🌐 SkillBridge AI: Professional Skill Gap Analyzer

**SkillBridge AI** is an intelligent career development tool designed to bridge the gap between a user's current expertise and industry requirements. Using **Natural Language Processing (NLP)** and **Machine Learning**, the system provides a deep analysis of a user's profile and generates a personalized learning path.

---

## 🚀 Key Features

* **Semantic Skill Matching:** Uses `Sentence-BERT (all-MiniLM-L6-v2)` to understand the context of skills rather than just simple keyword matching.
* **Hybrid Input System:** Users can either upload their **PDF Resume** or manually type their skills.
* **Job Readiness Score:** A real-time percentage meter showing how well the user fits a specific role.
* **Dynamic Learning Roadmap:** Generates a step-by-step guide to bridge identified gaps with direct links to learning resources.
* **Professional Dashboard:** Built with Streamlit for a clean, interactive, and high-end user experience.

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Frontend:** Streamlit
* **ML Model:** Sentence-Transformers (NLP)
* **Parsing:** PyPDF2
* **Data Handling:** Pandas, CSV
* **Similarity Logic:** Cosine Similarity (Semantic Analysis)

---

## 📂 Project Structure

```text
SkillGap_AI/
├── .streamlit/         # UI Theme configuration
├── data/               # CSV datasets for job roles
├── modules/            # Backend logic (Parser & ML Engine)
├── app.py              # Main Application Entry point
├── requirements.txt    # Project dependencies
```


## 🛠️ How to Run
1. Install requirements: `pip install -r requirements.txt`
2. Run the app: `streamlit run app.py`



