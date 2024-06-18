#PIN Opportunity By List Streamlit Docker Code
import streamlit as st
import pandas as pd
#import plotly.express as px
#from skimage import io
import snowflake.connector
import time
from PIL import Image, ImageDraw

st.set_page_config(page_title = "PIN", page_icon="🕹️", layout = "wide", initial_sidebar_state = "expanded")
# Function to connect to Snowflake
def connect_to_snow(user, password):
    try:
        ctx = snowflake.connector.connect(
            user=user,
            password=password,
            account='cw37897.east-us-2.azure',
            warehouse='INGEST_WH_ADF',
            database='TEST_DB',
            role='AUTOMATIONINGEST'
        )
        cs = ctx.cursor()
        st.session_state['snow_conn'] = cs
        st.session_state['is_ready'] = True
        st.write("Connected to Snowflake!")
        return cs
    except Exception as e:
        st.error(f"Error connecting to Snowflake: {e}")
        return None


horizontal_bar = "<hr style='margin-top: 0; margin-bottom: 0; height: 1px; border: 1px solid #635985;'><br>"   

instructionl = f"""<span style="font-size: 26px;">
    <ol>
    <li style="font-size:15px";>Please select an address and provide driving distance in number of minutes.</li>
    <li style="font-size:15px";>Then please choose your target persona and click get list.</li>
    </ol></span>""" 

instruction2 = f"""<span style="font-size: 26px;">
    <p style="font-size:25px">Please select an address and provide driving distance in number of minutes. Then please choose your target persona and click get list. </span>"""    

logo_path = 'MSI Logo-Stacked_RGB_Primary.png' 



with st.sidebar:
    st.image(logo_path, use_column_width=True)
    st.subheader("Enter User Details Here")
    user = st.sidebar.text_input("Username", "")
    password = st.sidebar.text_input("Password", "", type="password")
    
    if st.sidebar.button("Log In"):
        if user and password:
            cs = connect_to_snow(user, password)
            if cs:
                st.success("Connection successful!")
        else:
            st.warning("Please enter username and password")
sc1, sc2 = st.columns(2)
position = (400, 30)
logoImg = Image.open(logo_path).resize((200, 150))
canvas = Image.new('RGB', (800, 800), 'white')
canvas.paste(logoImg, position)

sc2.image(canvas, use_column_width=100)

sc1.title('PIN Opportunity By List')
sc1.markdown(horizontal_bar, True)
sc1.markdown(instruction2, unsafe_allow_html=True)
st.markdown(horizontal_bar, True)
