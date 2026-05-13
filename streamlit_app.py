import streamlit as st
import requests

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Enterprise Secure RAG",
    page_icon="🤖",
    layout="wide"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

.main {
    background-color: #0f172a;
}

h1, h2, h3 {
    color: white;
}

.stTextInput label,
.stTextArea label {
    color: white !important;
    font-weight: bold;
}

.answer-box {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 12px;
    color: white;
    font-size: 17px;
    line-height: 1.7;
    border-left: 5px solid #38bdf8;
}

.source-box {
    background-color: #111827;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 10px;
    color: white;
    border-left: 5px solid #22c55e;
}

.title-style {
    text-align: center;
    color: white;
    font-size: 42px;
    font-weight: bold;
}

.subtitle-style {
    text-align: center;
    color: #cbd5e1;
    font-size: 18px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================

st.markdown(
    "<div class='title-style'>Enterprise Secure RAG Assistant</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle-style'>Role-Based Secure AI Retrieval System</div>",
    unsafe_allow_html=True
)

st.markdown("---")

# =====================================================
# SIDEBAR LOGIN
# =====================================================

st.sidebar.title("User Login")

username = st.sidebar.text_input("Username")

password = st.sidebar.text_input(
    "Password",
    type="password"
)

st.sidebar.markdown("---")

st.sidebar.info("""
Sample Users

admin / admin123

hr_user / hr123

finance_user / finance123

technical_user / tech123
""")

# =====================================================
# MAIN QUERY INPUT
# =====================================================

st.subheader("Ask Enterprise Question")

query = st.text_area(
    "",
    height=150,
    placeholder="Example: Show Q1 revenue report..."
)

# =====================================================
# SUBMIT BUTTON
# =====================================================

submit = st.button("Generate Answer")

# =====================================================
# API REQUEST
# =====================================================

if submit:

    # EMPTY QUERY CHECK
    if query.strip() == "":

        st.warning("Please enter a query")

    else:

        with st.spinner("Retrieving enterprise knowledge..."):

            try:

                response = requests.post(

                    "http://127.0.0.1:8000/ask",

                    json={
                        "username": username,
                        "password": password,
                        "query": query
                    }
                )

                result = response.json()

                # =========================================
                # ERROR
                # =========================================

                if result.get("success") == False:

                    st.error(result.get("error"))

                else:

                    # =====================================
                    # USER INFO
                    # =====================================

                    col1, col2 = st.columns(2)

                    with col1:

                        st.success(
                            f"Logged in as : {result['user']}"
                        )

                    with col2:

                        st.info(
                            f"Role : {result['role']}"
                        )

                    st.markdown("---")

                    # =====================================
                    # ANSWER SECTION
                    # =====================================

                    st.subheader("Generated Answer")

                    st.markdown(
                        f"""
                        <div class='answer-box'>
                        {result['answer']}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    st.markdown("---")

                    # =====================================
                    # SOURCES SECTION
                    # =====================================

                    st.subheader("Retrieved Sources")

                    for source in result["sources"]:

                        st.markdown(
                            f"""
                            <div class='source-box'>

                            <b>Source File :</b>
                            {source['source']}

                            <br><br>

                            <b>Department :</b>
                            {source['department']}

                            <br><br>

                            <b>Confidence Score :</b>
                            {source['confidence_score']}

                            </div>
                            """,
                            unsafe_allow_html=True
                        )

            except Exception as e:

                st.error(f"Connection Error : {e}")

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.caption(
    "Enterprise Secure RAG System | FastAPI + FAISS + LangChain + Streamlit"
)
