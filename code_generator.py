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


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

df=pd.read_csv("city_day.csv")

print(df.head())

print(df.info())

print(df.describe())

print(df.isnull().sum())


# df=df.drop('Date',axis=1)
df=df.drop('NO',axis=1)
df=df.drop('NOx',axis=1)
df=df.drop('Benzene',axis=1)
df=df.drop('Toluene',axis=1)
df=df.drop('Xylene',axis=1)
df=df.drop('AQI_Bucket',axis=1)

print(df.shape)

print(df["AQI"].value_counts())

# print("CHECK_POINT1")
df=df.drop('Date',axis=1)


sns.heatmap(df.isnull(),yticklabels=False,cbar=True,cmap='viridis')
plt.show()

# print("CHECK_POINT2")

#pairplot which show reletionship
sns.pairplot(df)
plt.show()

# print("CHECK_POINT3")

#correlation heatmap
plt.figure(figsize=(8,8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.show()

# print("CHECK_POINT4")

# EDA Handling Missing Values

df.fillna({
    "PM2.5": df["PM2.5"].mean(),
    "PM10": df["PM10"].mean(),
    "NO2":df["NO2"].mean(),
    "NH3": df["NH3"].mean(),
    "CO":df["CO"].mean(),
    "SO2":df["SO2"].mean(),
    "O3": df["O3"].mean(),
    "AQI":df["AQI"].mean()
}, inplace=True)


# print("CHECK_POINT5")


# Dividing the Data into X and Y

x=df.iloc[:,1:8].values #independent features
y=df.iloc[:,-1].values # dependent features


# print("CHECK_POINT6")

print(x)
print(y)

# print("CHECK_POINT7")


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.3,random_state=0)

# print("CHECK_POINT8")


from sklearn.linear_model import LinearRegression
linreg=LinearRegression()
linreg.fit(x_train,y_train)


# print("CHECK_POINT9")

print(linreg.coef_)

print(linreg.intercept_)

# print("CHECK_POINT10")


y_pred=linreg.predict(x_test)
y_pred

print("CHECK_POINT11")

y_pred.shape


# model evaluation

x=df.iloc[:,1:8]
y=df.iloc[:,-1]


# print("CHECK_POINT12")

print(x.columns)
print(y)

coef_df=pd.DataFrame(linreg.coef_,x.columns,columns=["Coefficient"])
coef_df

plt.scatter(y_test,y_pred)
plt.show()

# print("CHECK_POINT13")


# prediction already hai X_test ke liye
y_pred = linreg.predict(x_test)
# Scatter Plot

plt.figure(figsize=(6.2,4.5))
plt.scatter(y_test, y_pred, color='blue', alpha=0.6)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')  # diagonal line
plt.xlabel('Actual AQI')
plt.ylabel('Predicted AQI')
plt.title('Actual vs Predicted AQI')
plt.show()

sns.distplot((y_test-y_pred),bins=50)
plt.show()

# print("CHECK_POINT14")


from sklearn import metrics

print('MAE:', metrics.mean_absolute_error(y_test, y_pred))
print('MSE:', metrics.mean_squared_error(y_test, y_pred))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))


# open a file, where you ant to store the data
file = open('regression_model_2.pkl', 'wb')
# dump information to that file
pickle.dump(linreg, file)


print("file is safe")


# print(y.head())


