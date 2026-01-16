from sentence_transformers import SentenceTransformer, util

# Model load (Ye thoda time lega first time run hone mein)
model = SentenceTransformer('all-MiniLM-L6-v2')

def calculate_gap(resume_text, required_skills):
    found = []
    missing = []
    
    # Resume text ko lowercase kar rahe hain better matching ke liye
    resume_text = resume_text.lower()
    
    for skill in required_skills:
        skill_lower = skill.lower()
        
        # 1. Direct Keyword Check (Fast)
        if skill_lower in resume_text:
            found.append(skill)
        else:
            # 2. ML Semantic Check (Advanced)
            # Agar exact word nahi mila, toh check karo concept match ho raha hai kya
            emb1 = model.encode(skill_lower, convert_to_tensor=True)
            emb2 = model.encode(resume_text, convert_to_tensor=True)
            
            cosine_score = util.cos_sim(emb1, emb2)
            
            if cosine_score > 0.40: # 40% threshold for AI matching
                found.append(skill)
            else:
                missing.append(skill)
                
    return found, missing