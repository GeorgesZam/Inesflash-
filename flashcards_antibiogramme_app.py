
import streamlit as st

# Define flashcards (questions and answers)
flashcards = [
    # Dynamics questions
    {"question": "Qu'est-ce que le poids ?", 
     "answer": "Le poids est une force exercée par la gravité sur un objet. Il s'exprime en Newtons (N)."},
    {"question": "Quelle est la différence entre le poids et la masse ?", 
     "answer": "La masse est une grandeur exprimée en kilogrammes (kg), tandis que le poids est une force exprimée en Newtons (N)."},
    {"question": "Où s'applique le poids d'un objet ?", 
     "answer": "Le poids s'applique sur le centre de gravité de l'objet."},
    {"question": "Dans un système en équilibre, pourquoi les forces se compensent-elles ?", 
     "answer": "Les forces se compensent car elles sont de même intensité, de direction opposée et agissent sur la même ligne d'action."},
    {"question": "Citez une force qui agit à distance.", 
     "answer": "La gravité ou la force électromagnétique."},
    {"question": "Citez une force qui nécessite un contact pour agir.", 
     "answer": "La force de frottement ou la tension d'un câble."},
    {"question": "Qu'est-ce qu'un référentiel ?", 
     "answer": "Un référentiel est un point de vue depuis lequel on observe le mouvement des objets."},
    {"question": "Quelle est la loi universelle de la gravitation ?", 
     "answer": "Deux objets s'attirent avec une force proportionnelle à leurs masses et inversement proportionnelle au carré de la distance qui les sépare."},
    
    # Chemistry questions
    {"question": "Quels produits sont toujours formés lors d'une réaction de combustion complète ?", 
     "answer": "Du dioxyde de carbone (CO2) et de l'eau (H2O)."},
    {"question": "Comment sait-on si une réaction chimique est totale ou non ?", 
     "answer": "Une réaction est totale si tous les réactifs sont consommés pour former les produits."}
]

# Initialize session state to track progress
if "current_index" not in st.session_state:
    st.session_state.current_index = 0

# Header
st.title("Flashcards : Dynamique et Chimie (Niveau Brevet)")
st.write("Pensez à la réponse, dites-la à haute voix, puis vérifiez en affichant la solution.")

# Display current flashcard
if st.session_state.current_index < len(flashcards):
    card = flashcards[st.session_state.current_index]
    st.write(f"**Question {st.session_state.current_index + 1}:** {card['question']}")
    
    if st.button("Afficher la réponse"):
        st.write(f"**Réponse :** {card['answer']}")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Question précédente", key="prev"):
            if st.session_state.current_index > 0:
                st.session_state.current_index -= 1
                st.experimental_rerun()
    with col2:
        if st.button("Question suivante", key="next"):
            if st.session_state.current_index < len(flashcards) - 1:
                st.session_state.current_index += 1
                st.experimental_rerun()
else:
    st.write("**Fin des questions.**")
    if st.button("Recommencer"):
        st.session_state.current_index = 0
        st.experimental_rerun()
