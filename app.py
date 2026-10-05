import streamlit as st

st.title("🎓 AI-Powered Skill Assessment & Certificate Platform")

name = st.text_input("Enter your name")

skill = st.selectbox(
    "Select your skill",
    ["Python", "Java", "Data Science"]
)

st.subheader("📝 Assessment")

questions = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "def", "function", "define"],
        "answer": "def"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["int", "string", "boolean", "float"],
        "answer": "boolean"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/*", "--"],
        "answer": "#"
    },
    {
        "question": "Which function is used to display output in Python?",
        "options": ["display()", "show()", "print()", "output()"],
        "answer": "print()"
    },
    {
        "question": "Which keyword is used for a loop over a sequence?",
        "options": ["for", "loop", "repeat", "iterate"],
        "answer": "for"
    },
    {
        "question": "Which of these is a Python collection?",
        "options": ["List", "Number", "Character", "Keyword"],
        "answer": "List"
    },
    {
        "question": "Which operator is used for multiplication?",
        "options": ["+", "-", "*", "/"],
        "answer": "*"
    },
    {
        "question": "What is the extension of a Python file?",
        "options": [".java", ".py", ".cpp", ".html"],
        "answer": ".py"
    },
    {
        "question": "Which keyword is used to create a class?",
        "options": ["object", "class", "define", "struct"],
        "answer": "class"
    },
    {
        "question": "Which function gets the length of a list?",
        "options": ["size()", "count()", "length()", "len()"],
        "answer": "len()"
    }
]

answers = []

for i, q in enumerate(questions):
    answer = st.radio(
        f"{i + 1}. {q['question']}",
        q["options"],
        key=f"q{i}"
    )
    answers.append(answer)

if st.button("Submit Assessment"):

    if name.strip() == "":
        st.warning("Please enter your name.")
    else:
        score = 0

        for i, q in enumerate(questions):
            if answers[i] == q["answer"]:
                score += 1

        percentage = (score / len(questions)) * 100

        st.success("Assessment submitted successfully!")

        st.write(f"### Student: {name}")
        st.write(f"### Skill: {skill}")
        st.write(f"### Score: {score}/{len(questions)}")
        st.write(f"### Percentage: {percentage:.0f}%")

        if percentage >= 80:
            certificate = "🥇 Gold Certificate"
            st.success(f"Congratulations! You earned a {certificate}.")

        elif percentage >= 60:
            certificate = "🥈 Silver Certificate"
            st.info(f"Congratulations! You earned a {certificate}.")

        elif percentage >= 50:
            certificate = "🥉 Bronze Certificate"
            st.warning(f"Congratulations! You earned a {certificate}.")

        else:
            certificate = "No Certificate"
            st.error("Sorry! You did not qualify for a certificate.")