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

from typing import Any

import numpy as np

import streamlit as st
from streamlit.hello.utils import show_code
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.set_page_config(page_title="Individual Results", page_icon="📹")
st.markdown("# Individual Results")
st.sidebar.header("Individual Results")
st.markdown("### Select a club to view the member results")

conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read()

selection = st.selectbox("Select a club", df[2].unique())
member = st.selectbox("Select a member", df[df[2] == selection][1].unique())
chosen = df.iloc[:, 2:22][(df[2] == selection) & (df[1] == member)]
columns = ['Improve critical-thinking skills',
           'Improve meeting-management skills',
           'Improve listening skills',
           'Improve leadership skills',
        #    'Which leadership skills?',
           'Improve communication skills',
        #    'Which communication skills?',
           'Improve evaluation skills',
           'Serve as a mentor for a new member',
           'Help increase club membership',
           'Serve as a club officer',
        #    'Which club officer position?',
           'Help the club with public relations or publicity',
           'Contribute to or edit the club newsletter or website',
           'Learn about parliamentary procedure',
           'Lead or help with a Speechcraft program',
           'Lead or help with a Youth Leadership program',
           'Lead or help with a youth communication module',
           'Visit other Toastmasters clubs',
           'Compete in a speech contest',
           'Judge a speech contest',
           'Organize a new Toastmasters club',
           'Serve as a district officer',
        #    'Which district officer position?',
           ]

chosen.reset_index(inplace=True, drop=True)
chosen.columns = columns
chosenT = chosen.T
st.markdown(f"### {member}")
for interest in ['High Interest', 'Some Interest', 'No Interest']:
    chosenT[interest] = chosenT[0].apply(lambda x: '✔️' if x == interest else '')
chosenT = chosenT.drop(0, axis=1)
st.dataframe(chosenT,use_container_width=True,height=750)

quality = df.iloc[:, 28:42][(df[2] == selection) & (df[1] == member)]
quality_columns = ['Welcoming','Friendly/relaxed atmosphere',
                   'Positive/Supportive','Organized meetings',
                   'Supportive club leaders','Opportunities to participate'
                   'Creative Table Topics®','Effective evaluations',
                   'Provides professional development','A networking environment',
                   'Promotion of club in the community',
                   'Varied and fun meetings',
                   'Toastmasters sponsoring new members recognized',
                   'Member achievements formally recognized with ceremony',
                   'Club and member achievements publicized'
                   ]
quality.reset_index(inplace=True, drop=True)
quality.columns = quality_columns
qualityT = quality.T
# st.markdown(f"### {member}")
for score in [1,2,3,4,5]:
    qualityT[score] = qualityT[0].apply(lambda x: '✔️' if x == score else '')
qualityT = qualityT.drop(0, axis=1)
st.dataframe(qualityT,use_container_width=True,height=550)

written = df.iloc[:, 22:27][(df[2] == selection) & (df[1] == member)]
written.reset_index(inplace=True, drop=True)
written = written.iloc[0]
# st.dataframe(written,use_container_width=True)
st.markdown('### What leadership skills you would like to develop?')
st.write(written[23])
st.markdown('### What communication skills you would like to develop?')
st.write(written[24])
st.markdown('### Which club officer position you are interested?')
st.write(written[25])
st.markdown('### Which district officer position you are interested?')
st.write(written[26])
st.markdown('### Other interests')
st.write(written[27])