# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time

import numpy as np

import streamlit as st
from streamlit.hello.utils import show_code

import streamlit as st
from streamlit.hello.utils import show_code
from streamlit_gsheets import GSheetsConnection




st.set_page_config(page_title="Club Quality Analysis", page_icon="📹")
st.markdown("# Club Quality Analysis")
st.sidebar.header("Club Quality Analysis")
st.markdown("### Select a club to view the Club Quality Analysis")
# st.write("Feature coming soon.")



conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read()
selection = st.selectbox("Select a club", df[2].unique())

password = st.text_input("Enter the password (obtain from Ming Kang at mk1029@hotmail.com)", type="password")
password_list = conn.read(worksheet="Sheet2")
if password == password_list[password_list['Club Name'] == selection]['password'].values[0]:

    chosen = df.iloc[:, 27:42][(df[2] == selection)]

    columns = ['Welcoming',
    'Friendly/relaxed atmosphere',
    'Positive/Supportive',
    'Organized meetings',
    'Supportive club leaders',
    'Opportunities to participate',
    'Creative Table Topics®',
    'Effective evaluations',
    'Provides professional development',
    'A networking environment',
    'Promotion of club in the community',
    'Varied and fun meetings',
    'Toastmasters sponsoring new members recognized',
    'Member achievements formally recognized with ceremony',
    'Club and member achievements publicized',]

    chosen.columns = columns

    # for column in columns:
    #     avg_score = chosen[column].mean()
    #     avg_score = round(avg_score, 2)  # round to 2 decimal places

    #     st.markdown(f"### {column} : {avg_score}")
    #     # st.markdown(f"## {avg_score}")

    st.markdown("### Club Quality Analysis")
    st.write("Number of responses: ", len(chosen))
    # st.dataframe(round(chosen.mean(),2))
    import pandas as pd
    import streamlit as st

    st.data_editor(
        round(chosen.mean(),2),
        column_config={
            "0": st.column_config.ProgressColumn(
                "Average Score",
                help="Average Score",
                format="%f",
                min_value=0,
                max_value=5,
            ),
        },
        hide_index=False,
        use_container_width=True
    )
    chosen = df.iloc[:, 42:][(df[2] == selection)]
    st.markdown('### What do you like most about your club?')
    st.write(chosen[chosen.columns[0]])
    st.markdown('### What do you like least about your club?')
    st.write(chosen[chosen.columns[1]])
    st.markdown('### What recommendations for improvement can you provide?')
    st.write(chosen[chosen.columns[2]])
    st.markdown('### Is there anything more specific you would like to learn about?')
    st.write(chosen[chosen.columns[3]])
    # st.dataframe(chosen[chosen.columns[0].values],use_container_width=True)