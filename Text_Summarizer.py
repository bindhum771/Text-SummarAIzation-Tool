import streamlit as st
from transformers import pipeline
import PyPDF2
import re

# ✅ MUST BE FIRST Streamlit Command
st.set_page_config(page_title="AI Text Summarizer", layout="wide")

# Load Hugging Face T5 Summarization Model
@st.cache_resource
def load_model():
    return pipeline("summarization", model="t5-small")

summarizer = load_model()

# ✅ Session State Variables
if "input_text" not in st.session_state:
    st.session_state.input_text = ""

if "summary" not in st.session_state:
    st.session_state.summary = "Your summary will appear here..."

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

# ✅ Dark Mode Toggle
dark_mode = st.toggle("🌙 Dark Mode", st.session_state.dark_mode)
st.session_state.dark_mode = dark_mode

# ✅ Apply Dark/Light Theme
if dark_mode:
    st.markdown("""
        <style>
            body { background-color: #0e1117; color: white; }
            .stTextArea textarea { background-color: #262730; color: white; }
            .stButton button { background-color: #ff4b4b; color: white; border-radius: 10px; }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
            body { background-color: white; color: black; }
            .stTextArea textarea { background-color: #f0f0f0; color: black; }
            .stButton button { background-color: #007BFF; color: white; border-radius: 10px; }
        </style>
    """, unsafe_allow_html=True)

# ✅ Page Title
st.title("📝 AI-Powered Text Summarization")

# ✅ Layout with Two Equal Columns
col1, col2 = st.columns([1, 1])

# ✅ LEFT SIDE - INPUT TEXT
with col1:
    st.subheader("📄 Input Text")

    # ✅ File Upload (PDF/TXT Support)
    uploaded_file = st.file_uploader("Upload Document (PDF or TXT)", type=["pdf", "txt"])

    if uploaded_file is not None:
        if uploaded_file.type == "application/pdf":
            reader = PyPDF2.PdfReader(uploaded_file)
            text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
        else:
            text = uploaded_file.read().decode("utf-8")
        st.session_state.input_text = text

    # ✅ Input Box
    input_text = st.text_area("Paste your text here:", st.session_state.input_text, height=200)

    # ✅ Update Input Text in Session
    st.session_state.input_text = input_text

    # ✅ Word Count
    word_count = len(input_text.split())
    st.write(f"**Word Count:** {word_count}")
    
    # ✅ Summary Length Slider (Now Below Summary Text)
    summary_length = st.slider("Select Summary Length", min_value=30, max_value=150, value=100, step=5)

    

    # ✅ Buttons Below Input Box
    colA, colB = st.columns([0.5, 0.5])
    

   # 🗑️ Delete Button
    with colA:
        if st.button("🗑️ Delete", key="delete"):
            st.session_state.input_text = ""
            st.session_state.summary = "Your summary will appear here..."
            st.rerun()  # ✅ Use this instead of st.experimental_rerun()

    # ⚡ Generate Summary Button
    with colB:
        def ensure_full_sentence(summary):
            """Trim summary to the last complete sentence ending with ., !, or ?"""
            match = re.findall(r'[^.!?]*[.!?]', summary)  # Find all full sentences
            cleaned_summary = "".join(match).strip() if match else summary  # Join complete sentences

    # Ensure the first letter is capitalized
            if cleaned_summary:
                cleaned_summary = cleaned_summary[0].upper() + cleaned_summary[1:]
                return cleaned_summary

        if st.button("⚡ Generate Summary", key="generate"):
            if input_text:
                max_summary_length = summary_length  # User-defined max length
                min_summary_length = max(30, summary_length // 3)  # Ensure flexibility without forcing long output
                raw_summary = summarizer(
                    input_text,
                    max_length=max_summary_length,
                    min_length=min_summary_length,
                    do_sample=False
                    )[0]['summary_text']
                st.session_state.summary = ensure_full_sentence(raw_summary)  # Ensure full sentence
# ✅ RIGHT SIDE - SUMMARY OUTPUT
with col2:
    st.subheader("📃 Summarized Text")

    # ✅ Summary Box Retains Summary
    summary_box = st.text_area("Summary:", st.session_state.summary, height=425)

    # ✅ Word Count for Summary
    summary_word_count = len(st.session_state.summary.split()) if st.session_state.summary != "Your summary will appear here..." else 0
    st.write(f"**Word Count:** {summary_word_count}")

    # ✅ Copy Summary Button (📋 Icon Only)
    if st.button("📋"):
        st.session_state.clipboard = st.session_state.summary
        st.success("Copied to clipboard!")


   