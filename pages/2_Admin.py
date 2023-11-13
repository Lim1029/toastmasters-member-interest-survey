from typing import Any

import numpy as np

import streamlit as st
from streamlit.hello.utils import show_code
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import secrets
import string



def reset_pass():
    conn = st.connection("gsheets", type=GSheetsConnection)
    ti_dashboard = pd.read_csv('https://dashboards.toastmasters.org/export.aspx?type=CSV&report=districtperformance~51~9/30/2023~~2023-2024')
    df = pd.DataFrame()
    df['Club Name'] = ti_dashboard['Club Name']
    password_length = 10
    df['password'] = [''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(password_length)) for _ in range(len(df))]
    conn.update(
    worksheet="Sheet2",
    data=df,)

password = st.text_input("Enter master password", type="password")
if(password == "password"):
    st.button("Reset Password",on_click=reset_pass)
