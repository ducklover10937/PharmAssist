import streamlit as st

st.set_page_config(
    page_title="PharmAssist",
    page_icon="PharmAssistFavi.ico",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.title("PharmAssist")
st.write("Your Over-the-Counter (OTC) medication recommender")
st.caption("Please note that PharmBot is not a substitute for professional medical advice. Always confirm with your pharmacist before purchasing an OTC medication!" \
"Be sure to consult a healthcare provider if you are experiencing serious symptoms, are pregnant, or taking other medications.")

symptom = st.text_area("Describe your symptoms:")

msg = "Remember to always consult your pharmacist or check the product label for personal appropriate dosages! \
Would you like me to find a nearby pharmacy for you?"
errorMsg = "I'm sorry, I couldn't understand your symptoms. Consider consulting a healthcare professional for more accurate advice."

medDict = {
    ("headache","migrane","headaches","head ache","head aches","head pain","head","head pains"): ["Tylenol (Acetaminophen)", "Advil (Acetaminophen/Ibuprofen)", "Motrin IB (Ibuprofen)", "Aleve (Naproxen Sodium)", "Aspirin (Acetylsalicylic Acid)"],
    ("cough","sore throat","coughing","coughs"): ["Advil (Ibuprofen)", "Tylenol (Acetaminophen)", "Cough drops (Honey/Mentol/Glycerin)", "Mucinex (Guaifenesin)"],
    ("allergy","allergies","allergic"): ["Allegra (Fexofenadine)", "Zyrtec (Antihistamine)", "Benadryl (Diphenhydramine)", "Claritin (Loratadine/Antihistamine)"],
    ("fever","sick", "cold", "sickness"): ["Tylenol (Acetaminophen)", "Advil (Ibuprofen)", "DayQuil/NyQuil (Acetaminophen)", "Alka-Seltzer Plus Cold & Flu (Acetaminophen)"],
    ("nausea", "nauseous"): ["Pepto Bismol (Bismuth Subsalicylate)", "Emetrol (Phosphorated Carbohydrate Solution)", "Dramamine (Antihisamine)", "Nauzene (Sodium Citrate Dihydrate)"],
    "diarrhea": ["Imodium (Loperamide)", "Pepto Bismol (Bismuth Subsalicylate)"],
    ("constipation", "constipated","constipate"): ["MiraLAX (Polyethylene Glycol)", "Dulcolax (Bisacodyl)", "Metamucil (Pysllium Fiber)", "Stool Softeners (Emollient Laxatives)"],
    ("heartburn","heart burn","indigestion", "indigest","sour","sour stomach"): ["Tums (Calcium Carbonate)", "Alka-Seltzer (Sodium Bicarbonate/Calcium Carbonate)", "Rolaids (Calcium Carbonate)"],
    ("runny nose","runny"): ["Claritin (Loratadine/Antihistamine)", "Zyrtec (Antihistamine)"],
    ("sneezing", "sneeze"): ["Claritin (Loratadine/Antihistamine)", "Zyrtec (Antihistamine)", "Allegra (Fexofenadine)"],
    ("congestion","stuffy", "stuffed nose", "stuffy nose", "nose congestion", "congest"): ["Sudafed (Pseudoephedrine)", "Tylenol Sinus (Phenylephrine/Decongestant)", "Mucinex Sinus-Max (Phenylephrine/Decongestant)", "Sinex (Oxymetazoline)", "Vicks VapoRub (Menthol/Camphor)"],
    ("muscle pain", "sore muscle", "sore muscles", "muscle sore", "muscle sores", "muscle", "muscles"): ["Acetaminophen (Tylenol)", "Ibuprofen (Advil)", "Advil (NSAID)"],
    ("toothache", "tooth pain", "tooth", "teethache", "teeth ache", "teeth pain"): ["Motrin (Ibuprofen)", "Advil (Ibuprofen)", "Orajel (Benzocaine)", "Advil (NSAID)"],
    ("insomnia", "sleep", "sleeping"): ["Melatonin (Hormone Inducer)", "ZzzQuil (Diphenhydramine)", "Benadryl (Diphenhydramine)"],
    ("cut", "cuts"): ["Antiseptic ointments (Neosporin)", "Bandages"],
    ("burn", "burns"): ["Aloe vera gel", "Hydrocortisone cream"],
    ("insect bite", "mosquito bite", "bug bite", "bugbite", "bite"): ["Hydrocortisone cream", "Antihistamines (Claritin)"],
    ("sunburn", "sun burn"): ["Aloe vera gel", "Ibuprofen (Advil)"],
    ("itch", "itchy", "scratchy"): ["Hydrocortisone cream", "Antihistamines (Claritin)"],
    ("earache", "ear pain", "ear", "ears"): ["Acetaminophen (Tylenol)", "Ibuprofen (Advil)"],
    ("dry eyes", "dry eye"): ["Artificial tears", "Lubricating eye ointments"],
    ("stomachache", "stomach ache"): ["Antacids (Tums)", "Bismuth subsalicylate (Pepto-Bismol)"],
    ("menstrual cramps", "period", "menstrual", "period cramp", "menstrual cramp", "cramp", "cramps"): ["Ibuprofen (Advil)", "Naproxen (Aleve)"],
    ("joint pain", "inflammation", "back pain"): ["Acetaminophen (Tylenol)", "Ibuprofen (Advil)"],
    ("fungal", "fungal infection", "fungal infections"): ["Antifungal creams (Lotrimin)", "Antifungal powders"],
    ("acne", "pimple", "pimples"): ["Benzoyl peroxide", "Salicylic acid"],
    ("cold sore", "cold sores", "coldsore"): ["Docosanol (Abreva)", "Lysine supplements"],
    ("lactose", "lactose intolerance", "lactose intolerant", "intolerant"): ["Lactase supplements (Lactaid)"]
}

def recommend(symptom):
    symptom = symptom.lower() 

    for sympt, meds in medDict.items(): 
        if isinstance(sympt, tuple):
            for s in sympt:
                if s in symptom:
                    return "For your symptom(s), you can consider: " + ", ".join(meds) + ". " + msg
        elif sympt in symptom:
            return "Here are some popular OTC medications you can consider: " + ", ".join(meds) + ". " + msg
    return errorMsg
        

if st.button("Get Recommendation"):
    st.write("### Recommendation:")
    st.success(recommend(symptom))
