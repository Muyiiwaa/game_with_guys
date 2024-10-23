import streamlit as st
import time
import pandas as pd
from utils import get_questions

questions = get_questions()

# List of player names
players = ["Semilore", "Tomisin", "Joel", "Monica", "Lekan"]

# Lock player selection after choosing
if "selected_player" not in st.session_state:
    st.session_state.selected_player = None

if st.session_state.selected_player is None:
    selected_player = st.selectbox("Select your name:", players)
    if st.button("Lock Player"):
        st.session_state.selected_player = selected_player
        st.rerun()
else:
    st.write(f"**Player:** {st.session_state.selected_player}")

# Initialize session state for each player's score and wrong answers
if "scores" not in st.session_state:
    st.session_state.scores = {player: 0 for player in players}
if "wrong_answers" not in st.session_state:
    st.session_state.wrong_answers = {player: 0 for player in players}
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "feedback" not in st.session_state:
    st.session_state.feedback = ""
if "show_next" not in st.session_state:
    st.session_state.show_next = False
if "answered_questions" not in st.session_state:
    st.session_state.answered_questions = []  # Track answered questions

# Display the current question inside a container with fixed height
with st.container():
    current_q = questions[st.session_state.current_question]
    st.write(f"**Question {st.session_state.current_question + 1}:** {current_q['question']}")
    selected_option = st.radio(
        "Choose an answer:", 
        current_q["options"], 
        disabled=st.session_state.current_question in st.session_state.answered_questions
    )

st.divider()

# Submit button to process the answer
if st.button("Submit Answer"):
    if selected_option == current_q["answer"]:
        st.session_state.feedback = "Correct! 🎉"
        st.session_state.scores[st.session_state.selected_player] += 1
    else:
        st.session_state.feedback = f"Wrong! 😢 The answer is '{current_q['answer']}'."
        st.session_state.wrong_answers[st.session_state.selected_player] += 1

    if "Correct" in st.session_state.feedback:
        st.success(st.session_state.feedback)
    else:
        st.error(st.session_state.feedback)

    # Add the current question to answered questions
    st.session_state.answered_questions.append(st.session_state.current_question)

    # Display a spinner/loader during the 3-second wait
    with st.spinner("Loading next question..."):
        time.sleep(3)  # Wait for 3 seconds

    # Trigger a UI refresh to show the "Next" button
    st.session_state.show_next = True
    st.rerun()

# Show the Next Question button if ready
if st.session_state.show_next:
    if st.button("Next Question"):
        if st.session_state.current_question < len(questions) - 1:
            st.session_state.current_question += 1
            st.session_state.feedback = ""  # Reset feedback
            st.session_state.show_next = False  # Hide the Next button
            st.rerun()  # Refresh the app to move to the next question
        else:
            st.write("Quiz complete!")
            st.write(f"Your score: {st.session_state.scores[st.session_state.selected_player]}/{len(questions)}")

st.divider()

# Display correct vs wrong answers for all players as a bar chart
with st.container():
    st.subheader("Quiz Performance of All Players")
    performance_data = pd.DataFrame(
        {
            "Player": players,
            "Score": [st.session_state.scores[player] for player in players]
        }
    )

    # Display the score comparison as a bar chart
    st.bar_chart(data=performance_data, x='Player', y='Score', color='Player')
