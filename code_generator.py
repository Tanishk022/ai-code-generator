# import base64
# from google import genai
# from dotenv import load_dotenv
# import streamlit as st
# import os

# # Load API key
# load_dotenv()
# API_KEY = os.getenv("GEMINI_API_KEY")

# col3,col4 = st.columns([1,2])
# with col3:
#     st.image("https://media.istockphoto.com/id/987365514/vector/software-web-development-programming-concept-abstract-programming-language-and-program-code.jpg?s=612x612&w=0&k=20&c=H-Q688NXMmw_3vhfrT63EklLOwPdihbKiEGZDK9BTYs=",width=200)
    
# with col4:
#     st.title(" AI Code Automation Tool")

# # Sidebar instructions
# with st.sidebar:
#     st.header("📌 How to Use")
#     st.markdown("""
#     Welcome to **AI Code Automation Tool**!  

#     Follow these steps to generate and view your code:

#     1️⃣ **Enter your requirement** in the text box (e.g., *"Create a calculator in Python"*).  

#     2️⃣ **Select the file type** you want to generate (Python, HTML, C++, Java, etc.).  

#     3️⃣ **Enter a file name** for your code.  

#     4️⃣ Click on **🚀 Generate Code** button.  

#     5️⃣ For **webpage-friendly files** (HTML), a clickable link will appear to **open your page in the browser**.  

#     6️⃣ You can also use **⬇️ Download Code** button to save your file locally.  

#     💡 *Tip: Give clear and specific instructions for better code results.*
#     """)


# file_types = ['.cpp','.js','.py','.html','.java']
# col1 ,col2 = st.columns([3,1])
# with col1:
#     prompt = st.text_area("Enter your prompt to generate what you want:", height=150)
# with col2:
#     file_name = st.text_input("Enter file name (without extension)")
#     file_type = st.selectbox("Select file type:", file_types)

# if st.button("🚀 Generate Code"):
#     if prompt.strip() == "":
#         st.warning("⚠️ Please enter a prompt.")
#     else:
#         try:
#             # Gemini API call
#             client = genai.Client()
#             response = client.models.generate_content(
#                 model="gemini-2.5-flash",
#                 contents=f"write a code {file_name}{file_type} file for the given prompt {prompt} give only the codes"
#             )
#             retext = response.text

#             # browser_friendly = [".html", ".htm"]  # jo types browser me directly open ho sakte hain

#             # if file_type in browser_friendly:
#             #     b64 = base64.b64encode(retext.encode()).decode()
#             #     href = f'<a href="data:text/html;base64,{b64}" target="_blank">🌐 Click here to open your webpage</a>'
#             #     st.markdown(href, unsafe_allow_html=True)
#             # else:
#             #     st.info("📄 Download your code file below:")
#             # Encode HTML to base64 (works for browser link)
#             if file_type == ".html":
#                 b64 = base64.b64encode(retext.encode()).decode()
#                 href = f'<a href="data:text/html;base64,{b64}" target="_blank">🌐 Click here to open your webpage</a>'
#                 st.markdown(href, unsafe_allow_html=True)
#             else:
#                 st.info(f"Sorry this type or file {file_type} is not directly run in Broser so you need to run this file in your code editior")
#                 st.info("📄 Download your code file below:")


#             # Download button
#             st.download_button("⬇️ Download Code", retext, f"{file_name}{file_type}")

#         except Exception as e:
#             st.error(f"❌ Error: {e}")


import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("regression_model_2.pkl", "rb"))
if st.button("Information about AQI Range"):
        st.image("Screenshot 2025-10-03 113142.png")
col1,col2 = st.columns([2,2])
with col1:
    st.image("https://medicaldialogues.in/wp-content/uploads/2016/11/AIR-POLLUTION.jpg")
with col2:
    st.title("Air Quality Prediction App")

# st.image("Screenshot 2025-10-03 113142.png")
with st.sidebar:
# User inputs
    # City = st.text_input("City")fil
    PM10  = st.number_input("Enter PM10", min_value=0.0,max_value=50.0, step=1.0)
    PM2_5 = st.number_input("Enter PM2.5", min_value=0.0,max_value=30.0, step=1.0)
    NO2   = st.number_input("Enter NO2", min_value=0.0,max_value=40.0, step=1.0)
    O3    = st.number_input("Enter O3", min_value=0.0,max_value=50.0, step=1.0)
    CO    = st.number_input("Enter CO", min_value=0.0,max_value=1.0, step=1.0)
    SO2   = st.number_input("Enter SO2", min_value=0.0,max_value=40.0, step=1.0)
    NH3   = st.number_input("Enter NH3", min_value=0.0,max_value=200.0, step=1.0)
    # AQI  = st.number_input("Enter AQI", min_value=0.0, step=1)

if st.button("Predict Air Quality"):
    # 'PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO', 'SO2', 'O3',
    #    'Benzene', 'Toluene'
    # features = np.array([[PM2.5, PM10, NO, NO2, NOx, NH3, CO, SO2, O3, Benzene, Toluene]])

    features = np.array([[PM10,PM2_5, NO2, O3, CO, SO2,NH3]])


    # features = np.array([[T, TM, TT, SLP, H, VV, V, VM]])
    y_pred = model.predict(features)[0]
    # prediction = np.clip(prediction, 0, 500)


    st.subheader(f"Predicted AQI: {round(y_pred,2)}")

    # Easy explanation block
    st.subheader("Leval of Concern")
    if y_pred >= 0 and y_pred <= 51:
        st.subheader("Good Air Quality")
        st.success("There are negligible levels of pollutants like particulate matter and ground-level ozone, the air is fresh and crisp, and you can breathe easily without any respiratory discomfort.")

    elif y_pred >= 51 and y_pred <= 100:
        st.subheader("Moderate Air Quality")
        st.info("Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution..")
        
    elif y_pred >= 101 and y_pred <= 150:
        st.subheader("Unhealthy for Sensitive Groups")
        st.warning("Members of sensitive groups may experience health effects. The general public is less likely to be affected.")
    elif y_pred >= 151 and y_pred <= 200:
        st.subheader("Unhealthy")
        st.warning("Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects.")
    elif y_pred >= 201 and y_pred <= 300:
        st.subheader("Very Unhealthy")
        st.warning("Health alert –The risk of health effects is increased for everyone.")
    else:
        st.write("Hazardous")
        st.error("– Serious health risks, stay indoors and avoid exposure.]")




