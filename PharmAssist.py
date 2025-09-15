import streamlit as st

st.set_page_config(
    page_title="PharmAssistant",
    page_icon="PharmAssistFavi.ico",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.title("PharmAssistant")
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
    ("allergy","allergies","allergic"): ["Allegra (Fexofenadine)", "Zyrtec (Antihistamine/Cetirizine)", "Benadryl (Diphenhydramine)", "Claritin (Loratadine/Antihistamine)"],
    ("fever","sick", "cold", "sickness"): ["Tylenol (Acetaminophen)", "Advil (Ibuprofen)", "DayQuil/NyQuil (Acetaminophen)", "Alka-Seltzer Plus Cold & Flu (Acetaminophen)"],
    ("nausea", "nauseous"): ["Pepto Bismol (Bismuth Subsalicylate)", "Emetrol (Phosphorated Carbohydrate Solution)", "Dramamine (Antihisamine)", "Nauzene (Sodium Citrate Dihydrate)"],
    "diarrhea": ["Imodium (Loperamide)", "Pepto Bismol (Bismuth Subsalicylate)"],
    ("constipation", "constipated","constipate"): ["MiraLAX (Polyethylene Glycol)", "Dulcolax (Bisacodyl)", "Metamucil (Pysllium Fiber)", "Stool Softeners (Emollient Laxatives)"],
    ("heartburn","heart burn","indigestion", "indigest","sour","sour stomach"): ["Tums (Antacids/Calcium Carbonate)", "Alka-Seltzer (Sodium Bicarbonate/Calcium Carbonate)", "Rolaids (Calcium Carbonate)"],
    ("runny nose","runny"): ["Claritin (Loratadine/Antihistamine)", "Zyrtec (Antihistamine)"],
    ("sneezing", "sneeze"): ["Claritin (Loratadine/Antihistamine)", "Zyrtec (Antihistamine)", "Allegra (Fexofenadine)"],
    ("congestion","stuffy", "stuffed nose", "stuffy nose", "nose congestion", "congest"): ["Sudafed (Pseudoephedrine)", "Tylenol Sinus (Phenylephrine/Decongestant)", "Mucinex Sinus-Max (Phenylephrine/Decongestant)", "Sinex (Oxymetazoline)", "Vicks VapoRub (Menthol/Camphor)"],
    ("muscle pain", "sore muscle", "sore muscles", "muscle sore", "muscle sores", "muscle", "muscles"): ["Acetaminophen (Tylenol)", "Ibuprofen (Advil)", "Advil (NSAID)"],
    ("toothache", "tooth pain", "tooth", "teethache", "teeth ache", "teeth pain"): ["Motrin (Ibuprofen)", "Advil (Ibuprofen)", "Orajel (Benzocaine)", "Advil (NSAID)"],
    ("insomnia", "sleep", "sleeping"): ["Melatonin (Hormone Inducer)", "ZzzQuil (Diphenhydramine)", "Benadryl (Diphenhydramine)"],
    ("cut", "cuts","scratch","open wound"): ["Neosporin (Neomycin Sulfate)", "Polysporin (Bacitracin Zinc)"],
    ("burn", "burns", "blister", "blisters"): ["Neosporin (Neomycin Sulfate)", "Polysporin (Bacitracin Zinc)", "Advil (Ibuprofen)", "Motrin (Ibuprofen)", "Tylenol (Acetaminophen)", "Vaseline (Petroleum Jelly)", "Aloe Vera Gel"],
    ("insect bite", "mosquito bite", "bug bite", "bugbite", "bite"): ["Hydrocortisone cream", "Calamine lotion (Zinc Oxide)", "Tylenol (Acetaminophen)", "Advil (Ibuprofen)", "Motrin (Ibuprofen)", "Zyrtec (Antihistamine/Cetirizine)"],
    ("sunburn", "sun burn", "flakey", "flake", "flakes"): ["1% Hydrocortisone cream", "Advil (Ibuprofen)", "Aloe Vera Gel", "Calamine lotion (Zinc Oxide)"],
    ("itch", "itchy", "scratchy", "rash"): ["Calamine lotion (Zinc Oxide)"],
    ("earache", "ear pain", "ear", "ears"): ["Tylenol (Acetaminophen)", "Advil (Ibuprofen)", "Motrin (Ibuprofen)"],
    ("dry eyes", "dry eye"): ["Visine (Tetrahydrozoline)", "Artificial tears", "Systane Ultra (Polyethylene Glycol/Propylene Glycol)"],
    ("stomachache", "stomach ache"): ["Tums (Antacids/Calcium Carbonate)", "Pepto-Bismol (Bismuth Subsalicylate)", "Simethicone"],
    ("menstrual cramps", "period", "menstrual", "period cramp", "menstrual cramp", "cramp", "cramps"): ["Advil (Ibuprofen)", "Motrin (Ibuprofen)", "Aleve (Naproxen Sodium)"],
    ("joint pain", "inflammation", "back pain"): ["Aspirin (NSAID)", "Tylenol (Acetaminophen)", "Motrin IB (Ibuprofen)", "Advil (Ibuprofen)"],
    ("fungal", "fungal infection", "fungal infections"): ["Lotrimin (Antifungal/Clotrimazole)"],
    ("acne", "pimple", "pimples"): ["Differin gel (Adapalene)", "Neutrogena On-the-Spot Acne Treatment (Benzoyl Peroxide)", "Cerave Acne Control Cleanser (Salicylic Acid)"],
    ("cold sore", "cold sores", "coldsore"): ["Abreva (Docosanol)", "Orajel (Benzocaine)"],
    ("lactose", "lactose intolerance", "lactose intolerant", "intolerant"): ["Lactaid (Lactase Enzyme)"]
}

def recommend(symptom):
    symptom = symptom.lower() 

    for sympt, meds in medDict.items(): 
        if isinstance(sympt, tuple):
            for s in sympt:
                if s in symptom:
                    return "Here are some popular OTC medications you can consider for your symptoms: \n\n• " + " \n\n• ".join(meds) + "\n\n" + msg
        elif sympt in symptom:
            return "Here are some popular OTC medications you can consider for your symptoms: \n\n• " + " \n\n• ".join(meds) + "\n\n" + msg
    return errorMsg
        

if st.button("Get Recommendation"):
    st.write("### Recommendation:")
    st.success(recommend(symptom))


