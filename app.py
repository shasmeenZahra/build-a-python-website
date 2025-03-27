import streamlit as st

def home():
    st.title("🏠 Welcome to My Website")
    st.write("This is a simple multipage website built with Streamlit.")
    st.subheader("📌 What is Python?")
    st.write("Python is a high-level, interpreted programming language known for its simplicity and readability.")
    st.write("It is used in various fields such as web development, data science, AI, machine learning, automation, and more.")
    
    st.subheader("📌 Features of Python:")
    st.markdown("""
    - **Easy to Learn**: Simple syntax similar to English.
    - **Interpreted Language**: No need for compilation.
    - **Dynamically Typed**: No need to declare variable types.
    - **Large Standard Library**: Built-in modules for various applications.
    - **Community Support**: One of the largest programming communities.
    """)

def about():
    st.title("ℹ️ About Me")
    st.write("Hello! My name is **Shasmeen**, and I am a **12th-class student** as well as a **GIAIC student (Section A, under Sir Zia's supervision)**. I am passionate about programming and have already explored various technologies including **Python, TypeScript, JavaScript, HTML, and CSS**.")
    st.write("Now, I am diving into the exciting world of **Artificial Intelligence (AI)** to expand my knowledge and skills.")
    st.write("I love coding and building projects that enhance my learning experience. This website is an example of how Streamlit can be used to create interactive web applications.")
    st.write("Feel free to explore and test your Python knowledge with the quiz!")


def contact():
    st.title("📞 Contact Us")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send")
        if submitted:
            st.success("Thank you! Your message has been sent.")

def quiz():
    st.title("📝 Python Quiz")
    st.write("Test your Python knowledge with this multiple-choice quiz!")
    
    questions = {
        "What type of language is Python?": ["Compiled", "Interpreted", "Machine Language", "Assembly"],
        "Which keyword is used to define a function in Python?": ["define", "func", "def", "lambda"],
        "Which data type is immutable in Python?": ["List", "Dictionary", "Tuple", "Set"],
        "Which of the following is used for comments in Python?": ["//", "#", "/* */", "<!-- -->"],
        "Which of the following is a valid Python variable name?": ["2var", "my_var", "my-var", "my var"],
        "Which module is used to work with dates in Python?": ["datetime", "time", "calendar", "date"],
        "What will `print(type([]))` output?": ["<class 'list'>", "<class 'tuple'>", "<class 'dict'>", "<class 'set'>"],
        "How do you start a loop in Python?": ["loop", "for", "repeat", "iterate"],
        "Which function is used to get user input in Python?": ["scanf", "cin", "input", "get"],
        "What does `len([1, 2, 3])` return?": ["3", "2", "1", "None"]
    }
    
    score = 0
    correct_answers = {
        "What type of language is Python?": "Interpreted",
        "Which keyword is used to define a function in Python?": "def",
        "Which data type is immutable in Python?": "Tuple",
        "Which of the following is used for comments in Python?": "#",
        "Which of the following is a valid Python variable name?": "my_var",
        "Which module is used to work with dates in Python?": "datetime",
        "What will `print(type([]))` output?": "<class 'list'>",
        "How do you start a loop in Python?": "for",
        "Which function is used to get user input in Python?": "input",
        "What does `len([1, 2, 3])` return?": "3"
    }
    
    for question, options in questions.items():
        answer = st.radio(question, options)
        if answer == correct_answers[question]:
            score += 1
    
    if st.button("Submit Quiz"):
        st.success(f"You scored {score}/{len(questions)}!")

st.set_page_config(page_title="My Python Website", page_icon="🐍", layout="wide")

menu = st.sidebar.radio("Navigation", ["Home", "About", "Contact", "Python Quiz"])

if menu == "Home":
    home()
elif menu == "About":
    about()
elif menu == "Contact":
    contact()
elif menu == "Python Quiz":
    quiz()
