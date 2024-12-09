
import streamlit as st

# Define flashcards (questions and answers)
flashcards = [
    {"question": "Qu'est-ce qu'un antibiogramme ?", 
     "answer": "Un test permettant de vérifier la sensibilité d'une bactérie à différents antibiotiques."},
    {"question": "Quelle est la signification d'une grande auréole autour d'un disque d'antibiotique ?",
     "answer": "Cela signifie que l'antibiotique est efficace contre la souche bactérienne testée."},
    {"question": "Que représente le diamètre de l'auréole dans un antibiogramme ?", 
     "answer": "La sensibilité de la bactérie à l'antibiotique testé."},
    {"question": "Pourquoi teste-t-on plusieurs antibiotiques en même temps ?", 
     "answer": "Pour identifier l'antibiotique le plus efficace contre la bactérie étudiée."},
    {"question": "Citez un antibiotique couramment utilisé pour les antibiogrammes.", 
     "answer": "La pénicilline ou la vancomycine."}
]

# Initialize session state to track progress
if "current_index" not in st.session_state:
    st.session_state.current_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0

# Header
st.title("Application de révision : Flashcards sur l'antibiogramme")
st.write("Répondez aux questions et testez vos connaissances.")

# Display current flashcard
if st.session_state.current_index < len(flashcards):
    card = flashcards[st.session_state.current_index]
    st.write(f"**Question {st.session_state.current_index + 1}:** {card['question']}")
    
    # Input for the answer
    user_answer = st.text_input("Votre réponse :", key=f"answer_{st.session_state.current_index}")
    
    if st.button("Valider"):
        if user_answer.lower() == card['answer'].lower():
            st.success("Bonne réponse !")
            st.session_state.score += 1
        else:
            st.error(f"Mauvaise réponse. La réponse correcte est : {card['answer']}")
        
        # Move to the next question
        st.session_state.current_index += 1
        st.experimental_rerun()
else:
    # Final score
    st.write("**Quiz terminé !**")
    st.write(f"Votre score final est : {st.session_state.score} / {len(flashcards)}")
    if st.session_state.score == len(flashcards):
        st.balloons()

# Reset button
if st.button("Recommencer"):
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.experimental_rerun()
