import streamlit as st

st.title("PharmAssist")
st.write("Your Over-the-Counter (OTC) medication recommender")
st.caption("Please note that PharmBot is not a substitute for professional medical advice. Always consult a " \
"healthcare provider when experiencing serious symptoms, if you are pregnant, or taking other medications.")

symptom = st.text_area("Describe your symptoms:")

msg = "Would you like me to find a nearby pharmacy for you?"
errorMsg = "I'm sorry, I couldn't understand your symptoms. Consider consulting a healthcare professional for accurate advice."

medDict = {
    "headache": ["Tylenol", "Ibuprofen (Advil)"],
    "cough": ["Dextromethorphan (Robitussin)", "Honey-based syrups"],
    "allergy": ["Loratadine (Claritin)", "Cetirizine (Zyrtec)"],
    "fever": ["Acetaminophen (Tylenol)", "Ibuprofen (Advil)"],
    "cold": ["Decongestants (Sudafed)", "Saline nasal sprays"],
    "sore throat": ["Lozenges", "Warm salt water gargle"],
    "nausea": ["Bismuth subsalicylate (Pepto-Bismol)", "Ginger supplements"],
    "diarrhea": ["Loperamide (Imodium)", "Oral rehydration solutions"],
    "constipation": ["Fiber supplements", "Stool softeners (Colace)"],
    "heartburn": ["Antacids (Tums)", "H2 blockers (Ranitidine)"],
    "runny nose": ["Antihistamines (Claritin)", "Nasal corticosteroids (Flonase)"],
    "sneezing": ["Antihistamines (Claritin)", "Nasal corticosteroids (Flonase)"],
    "congestion": ["Decongestants (Sudafed)", "Saline nasal sprays"],
    "muscle pain": ["Acetaminophen (Tylenol)", "Ibuprofen (Advil)"],
    ("toothache", "tooth pain", "tooth", "teethache", "teeth ache", "teeth pain"): ["Acetaminophen (Tylenol)", "Ibuprofen (Advil)"],
    ("insomnia", "sleep", "sleeping"): ["Melatonin", "Diphenhydramine (Benadryl)"],
    ("cut", "cuts"): ["Antiseptic ointments (Neosporin)", "Bandages"],
    ("burn", "burns"): ["Aloe vera gel", "Hydrocortisone cream"],
    ("insect bite", "mosquito bite", "bug bite", "bugbite", "bite"): ["Hydrocortisone cream", "Antihistamines (Claritin)"],
    "sunburn": ["Aloe vera gel", "Ibuprofen (Advil)"],
    ("itch", "itchy", "scratchy"): ["Hydrocortisone cream", "Antihistamines (Claritin)"],
    ("earache", "ear pain", "ear", "ears"): ["Acetaminophen (Tylenol)", "Ibuprofen (Advil)"],
    ("dry eyes", "dry eye"): ["Artificial tears", "Lubricating eye ointments"],
    ("stomachache", "indigestion", "stomach ache"): ["Antacids (Tums)", "Bismuth subsalicylate (Pepto-Bismol)"],
    ("menstrual cramps", "period", "menstrual", "period cramp", "menstrual cramp", "cramp", "cramps"): ["Ibuprofen (Advil)", "Naproxen (Aleve)"],
    ("joint pain", "inflammation", "back pain"): ["Acetaminophen (Tylenol)", "Ibuprofen (Advil)"],
    ("fungal", "fungal infection", "fungal infections"): ["Antifungal creams (Lotrimin)", "Antifungal powders"],
    ("acne", "pimple", "pimples"): ["Benzoyl peroxide", "Salicylic acid"],
    "cold sore": ["Docosanol (Abreva)", "Lysine supplements"]
}

def recommend(symptom):
    symptom = symptom.lower() 

    for sympt, meds in medDict.items(): 
        if isinstance(sympt, tuple):
            for s in sympt:
                if s in symptom:
                    return "For your symptom(s), you can consider: " + ", ".join(meds) + ". " + msg
        elif sympt in symptom:
            return "For your symptom(s), you can consider: " + ", ".join(meds) + ". " + msg
    return errorMsg
        

if st.button("Get Recommendation"):
    st.write("### Recommendation:")
    st.success(recommend(symptom))