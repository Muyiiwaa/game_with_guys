import streamlit as st
import time
import pandas as pd
from utils import get_questions

questions = get_questions()
# Initialize session state variables
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "feedback" not in st.session_state:
    st.session_state.feedback = ""
if "show_next" not in st.session_state:
    st.session_state.show_next = False
if "wrong_answers" not in st.session_state:
    st.session_state.wrong_answers = 0
if "answered_questions" not in st.session_state:
    st.session_state.answered_questions = []  # Track answered questions

# Display the current question inside a container with fixed height
with st.container(height=250):
    current_q = questions[st.session_state.current_question]
    st.write(f"**Question {st.session_state.current_question + 1}:** {current_q['question']}")
    selected_option = st.radio("Choose an answer:", current_q["options"], disabled=st.session_state.current_question in st.session_state.answered_questions)

st.divider()
# Submit button to process the answer
if st.button("Submit Answer"):
    if selected_option == current_q["answer"]:
        st.session_state.feedback = "Correct! 🎉"
        st.session_state.score += 1
    else:
        st.session_state.feedback = f"Wrong! 😢 The answer is '{current_q['answer']}'."
        st.session_state.wrong_answers += 1

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
            st.write(f"Quiz complete! Your score: {st.session_state.score}/{len(questions)}")
st.divider()
# Display correct vs wrong answers as a bar chart in a new container
with st.container():
    st.subheader("Quiz Performance")
    performance_data = pd.DataFrame(
        {
            "result": ["Correct", "Wrong"],
            "count": [st.session_state.score, st.session_state.wrong_answers]
        }
    )
    st.bar_chart(performance_data,x = "result", y="count", color="result")