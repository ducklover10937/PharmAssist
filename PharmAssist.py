import streamlit as st

st.set_page_config(
    page_title="PharmAssistant",
    page_icon="PharmAssistFavi.ico",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.markdown("""<style>.stApp { background-color: #93b0b5; color: #152e33; } </style>""", unsafe_allow_html=True)
st.markdown("""<style>.stButton { color: #4d9abf; }</style>""", unsafe_allow_html=True)
st.markdown("<h1 style = 'text-align: center;font-size: 40 px;'>PharmAssistant</h1>", unsafe_allow_html=True)
st.markdown("<p style = 'text-align: center;font-size: 30 px;'>Your Over-the-Counter (OTC) medication recommender</p>", unsafe_allow_html=True)
st.markdown("<p style = 'text-align: center;font-size: 16px; font-style:italic'>Please note that PharmAssistant is not a substitute for professional medical advice. Always confirm with your pharmacist before purchasing an OTC medication!" \
" Be sure to consult a healthcare provider if you are experiencing serious symptoms, are pregnant, or taking other medications.</p>", unsafe_allow_html=True)
st.markdown(""" <style>.stTextInput[aria-label="Describe your symptoms, health concerns, or requests:"] { 
background-color: #4d9abf; }</style> """, unsafe_allow_html=True) 

msg = "Remember to always consult your pharmacist or check the product label for appropriate dosages! \n\n Would you like me to find a nearby pharmacy for you?"
errorMsg = "I'm sorry, I couldn't understand your symptoms. Consider consulting a healthcare professional for more accurate advice."

chatContainer = st.container()
chat = st.text_input("Describe your symptoms, health concerns, or requests:", value="", key="chatInput") #user input

medDict = {
    ("headache","migraine","headaches","head ache","head aches","head pain","head","head pains"): ["Tylenol (Acetaminophen)", "Advil (Acetaminophen/Ibuprofen)", "Motrin IB (Ibuprofen)", "Aleve (Naproxen Sodium)", "Aspirin (Acetylsalicylic Acid)"],
    ("cough","sore throat","coughing","coughs"): ["Advil (Ibuprofen)", "Tylenol (Acetaminophen)", "Cough drops (Honey/Mentol/Glycerin)", "Mucinex (Guaifenesin)"],
    ("allergy","allergies","allergic"): ["Allegra (Fexofenadine)", "Zyrtec (Antihistamine/Cetirizine)", "Benadryl (Diphenhydramine)", "Claritin (Loratadine/Antihistamine)"],
    ("fever","sick", "cold", "sickness"): ["Tylenol (Acetaminophen)", "Advil (Ibuprofen)", "DayQuil/NyQuil (Acetaminophen)", "Alka-Seltzer Plus Cold & Flu (Acetaminophen)"],
    ("nausea", "nauseous"): ["Pepto Bismol (Bismuth Subsalicylate)", "Emetrol (Phosphorated Carbohydrate Solution)", "Dramamine (Antihisamine)", "Nauzene (Sodium Citrate Dihydrate)"],
    ("diarrhea", "loose bowel", "loose bowels"): ["Imodium (Loperamide)", "Pepto Bismol (Bismuth Subsalicylate)"],
    ("constipation", "constipated","constipate"): ["MiraLAX (Polyethylene Glycol)", "Dulcolax (Bisacodyl)", "Metamucil (Psyllium Fiber)", "Stool Softeners (Emollient Laxatives)"],
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

ynDict = {
    ("yes", "sure","yeah", "yea", "yess", "yesss", "yessss", "yesssss", "yup", "yupp", "yups", "ok", "okay", "okok", "okayokay", "okays", "oks", "ye", "yee", "yurp", "yerp"): True, #yes
    ("no", "nah", "nope", "nop", "naw", "nawt", "nay", "nays", "noo", "nooo", "noooo", "nooooo", "never", "na", "nos"): False
}

pharmDict = {
    ("pharmacy", "pharmacies", "drugstore", "drugstores", "pharm"): True
}

if "chatHistory" not in st.session_state:
    st.session_state.chatHistory = [] #empty chat history with Pharmassistant (filled later)

if "ynRespond" not in st.session_state:
        st.session_state.ynRespond = False #if Pharmassistant waits for yes or no 

def respond(chat): #PharmAssistant response format
    chat = chat.lower() 

    for sympt, meds in medDict.items(): 
        for s in sympt:
            if s in chat:
                return "Here are some popular OTC medications you can consider for your symptoms: \n\n    • " + " \n\n    • ".join(meds) + "\n\n" + msg, True
    return errorMsg, False

def yesno(chat): #if Pharmassist gets yes or no response
    chat = chat.lower().strip()
    for yn, tf in ynDict.items(): 
        for response in yn: #if main yes/no is in ynDict
            if response in chat: #if user input has main yes/no response
                return tf #return true/false
    return None

if "pharmacyFind" not in st.session_state:
    st.session_state.pharmFind = False

def checkPharm(chat): #if pharmassistant gets pharmacy find req
    chat = chat.lower().strip()
    for pharmacy, tf in pharmDict.items():
        for response in pharmacy:
            if response in chat:
                return tf
    return None

if st.button("Send") and chat.strip() != "": #user sends message to pharmassistant
    st.session_state.chatHistory.append(chat)
    if st.session_state.ynRespond:
        yn = yesno(chat)
        if yn is True: #if user says yes or asks for pharmacies
            st.session_state.chatHistory.append("What village are you located in? \n\n Here are some nearby pharmacies:")
            st.session_state.chatHistory.append(
                """ 
                <iframe src="https://www.google.com/maps/embed?pb=!1m16!1m12!1m3!1d31037.348342169684!2d144.79071477180486!3d13.494510482085245!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!2m1!1spharmacy%20near%20me!5e0!3m2!1sen!2s" width="600" height="700" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"> </iframe> 
                """
            )
        elif yn is False: #no
            st.session_state.chatHistory.append("Okay, just be sure to always consult your pharmacist or check the product label for appropriate dosages!")
        st.session_state.ynRespond = False
        
    else:
        pharmFind = checkPharm(chat)
        if pharmFind:
            st.session_state.pharmFind = True
            st.session_state.chatHistory.append("What village are you located in? \n\n Here are some nearby pharmacies:")
            st.session_state.chatHistory.append(
                """ 
                <iframe src="https://www.google.com/maps/embed?pb=!1m16!1m12!1m3!1d31037.348342169684!2d144.79071477180486!3d13.494510482085245!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!2m1!1spharmacy%20near%20me!5e0!3m2!1sen!2s" width="600" height="700" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"> </iframe> 
                """
            )
        else:
            recMatch, recAsk = respond(chat) #not a yes/no response -> if user wants recommendation/pharmacy find
            st.session_state.ynRespond = recAsk
            st.session_state.chatHistory.append("Recommendation:")
            st.session_state.chatHistory.append(recMatch)

    st.rerun()

with chatContainer: #saving chat history and displaying it
    for chatEntry in st.session_state.chatHistory:        
        if "<iframe" in chatEntry:
            st.components.v1.html(chatEntry.replace("\n", ""), height=700)
        elif "Recommendation" in chatEntry or "What village are you located in?" in chatEntry or "Here are some popular OTC medications you can consider for your symptoms" in chatEntry or errorMsg in chatEntry or "Okay, just be sure to always consult your pharmacist" in chatEntry:
            st.markdown("<div style='background-color: #536e70; color: #d4f1ff; text-align: left; overflow-wrap:break-word; display:inline-block; padding: 10px; max-width: 70%; border-radius: 20px;'>"+chatEntry+"</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div style='background-color: #d8ebf2; color: #152e33; text-align: left; overflow-wrap:break-word; float: right;display:inline-block; padding: 10px; border-radius: 20px; max-width: 70%'>"+chatEntry+"</div>", unsafe_allow_html=True)





