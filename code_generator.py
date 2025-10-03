import base64
from google import genai
from dotenv import load_dotenv
import streamlit as st
import os

# Load API key
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

col3,col4 = st.columns([1,2])
with col3:
    st.image("https://media.istockphoto.com/id/987365514/vector/software-web-development-programming-concept-abstract-programming-language-and-program-code.jpg?s=612x612&w=0&k=20&c=H-Q688NXMmw_3vhfrT63EklLOwPdihbKiEGZDK9BTYs=",width=200)
    
with col4:
    st.title(" AI Code Automation Tool")

# Sidebar instructions
with st.sidebar:
    st.header("📌 How to Use")
    st.markdown("""
    Welcome to **AI Code Automation Tool**!  

    Follow these steps to generate and view your code:

    1️⃣ **Enter your requirement** in the text box (e.g., *"Create a calculator in Python"*).  

    2️⃣ **Select the file type** you want to generate (Python, HTML, C++, Java, etc.).  

    3️⃣ **Enter a file name** for your code.  

    4️⃣ Click on **🚀 Generate Code** button.  

    5️⃣ For **webpage-friendly files** (HTML), a clickable link will appear to **open your page in the browser**.  

    6️⃣ You can also use **⬇️ Download Code** button to save your file locally.  

    💡 *Tip: Give clear and specific instructions for better code results.*
    """)


file_types = ['.cpp','.js','.py','.html','.java']
col1 ,col2 = st.columns([3,1])
with col1:
    prompt = st.text_area("Enter your prompt to generate what you want:", height=150)
with col2:
    file_name = st.text_input("Enter file name (without extension)")
    file_type = st.selectbox("Select file type:", file_types)

if st.button("🚀 Generate Code"):
    if prompt.strip() == "":
        st.warning("⚠️ Please enter a prompt.")
    else:
        try:
            # Gemini API call
            client = genai.Client()
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"write a code {file_name}{file_type} file for the given prompt {prompt} give only the codes"
            )
            retext = response.text

            # browser_friendly = [".html", ".htm"]  # jo types browser me directly open ho sakte hain

            # if file_type in browser_friendly:
            #     b64 = base64.b64encode(retext.encode()).decode()
            #     href = f'<a href="data:text/html;base64,{b64}" target="_blank">🌐 Click here to open your webpage</a>'
            #     st.markdown(href, unsafe_allow_html=True)
            # else:
            #     st.info("📄 Download your code file below:")
            # Encode HTML to base64 (works for browser link)
            if file_type == ".html":
                b64 = base64.b64encode(retext.encode()).decode()
                href = f'<a href="data:text/html;base64,{b64}" target="_blank">🌐 Click here to open your webpage</a>'
                st.markdown(href, unsafe_allow_html=True)
            else:
                st.info(f"Sorry this type or file {file_type} is not directly run in Broser so you need to run this file in your code editior")
                st.info("📄 Download your code file below:")


            # Download button
            st.download_button("⬇️ Download Code", retext, f"{file_name}{file_type}")

        except Exception as e:
            st.error(f"❌ Error: {e}")

     


