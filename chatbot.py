import streamlit as st
import io

st.title("Text File Quiz App")

uploaded_file = st.file_uploader("Upload a text file", type="txt")
if uploaded_file is not None:
    # Read the file as text
    wrapper = io.TextIOWrapper(uploaded_file, encoding="utf-8")
    lines = wrapper.readlines()
    # Assume each line is "question,answer"
    questions = []
    answers = []
    for line in lines:
        parts = line.strip().split(",", 1)
        if len(parts) == 2:
            questions.append(parts[0])
            answers.append(parts[1])

    if "current_q" not in st.session_state:
        st.session_state.current_q = 0
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "answered" not in st.session_state:
        st.session_state.answered = False

    total_questions = len(questions)
    if total_questions > 0:
        idx = st.session_state.current_q
        st.markdown(f"**Question {idx+1} of {total_questions}:** {questions[idx]}")
        user_answer = st.text_input("Your answer:", key=f"answer_{idx}")

        if st.button("Submit") and not st.session_state.answered:
            if user_answer.strip().lower() == answers[idx].strip().lower():
                st.success("Correct!")
                st.session_state.score += 1
            else:
                st.error(f"Incorrect. Correct answer: {answers[idx]}")
            st.session_state.answered = True

        if st.session_state.answered:
            if st.button("Next"):
                st.session_state.current_q += 1
                st.session_state.answered = False
                st.experimental_rerun()

        st.markdown(f"**Score:** {st.session_state.score} / {total_questions}")
    else:
        st.warning("No valid questions found in the file.")
