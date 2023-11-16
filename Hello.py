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

import streamlit as st
from streamlit.logger import get_logger
from streamlit_star_rating import st_star_rating
import pandas as pd
from datetime import datetime
import time


LOGGER = get_logger(__name__)

import streamlit as st
from streamlit_gsheets import GSheetsConnection

def reset_form():
    st.session_state.name = None

def run():
    st.set_page_config(
        page_title="Survey Form",
        page_icon="👋",
    )

    st.write("# Welcome to Toastmasters Member Interest Survey (MIS)!")
    ti_dashboard = pd.read_csv('https://dashboards.toastmasters.org/export.aspx?type=CSV&report=districtperformance~51~9/30/2023~~2023-2024')
    
    st.sidebar.success("MIS Survey form")


    st.title("MIS Survey form")
    st.write("This form is adapted from the Toastmasters International Member Interest Survey (MIS) to help you identify your interests and goals. The survey results will be used to help you find opportunities to develop your skills and achieve your goals. The survey results will also be used to help your club and district leaders identify ways to improve your club experience.")   
    # st.dataframe(df)

    results = {}

    with st.form('Survey Form'):
        results[1] = st.text_input('Name', key='name')
        results[2] = st.selectbox('Club Name (quick search in the select box)', ti_dashboard['Club Name'].unique())
        st.markdown('## Interests')
        st.markdown('### Personal and Vocational')
        results[3] = st.radio(
        "Improve critical-thinking skills",
        ["High Interest", "Some Interest", "No Interest"],
        horizontal=True,
        index=None,
    )
        results[4] = st.radio(
        "Improve meeting-management skills",
        ["High Interest", "Some Interest", "No Interest"],
        horizontal=True,
        index=None,
    )
        results[5] = st.radio(
        "Improve listening skills",
        ["High Interest", "Some Interest", "No Interest"],
        horizontal=True,
        index=None,
    )
        results[6] = st.radio(
        "Improve leadership skills",
        ["High Interest", "Some Interest", "No Interest"],
        horizontal=True,
        index=None,
    )
        results[23] = st.text_input('What leadership skills?')

        results[7] = st.radio(
        "Improve communication skills",
        ["High Interest", "Some Interest", "No Interest"],
        horizontal=True,
        index=None,
    )
        results[24] = st.text_input('What communication skills?')

        results[8] = st.radio(
        "Improve evaluation skills",
        ["High Interest", "Some Interest", "No Interest"],
        horizontal=True,
        index=None,
    )
        st.markdown('### Club Involvement')
        results[9] = st.radio(
        "Serve as a mentor for a new member",
        ["High Interest", "Some Interest", "No Interest"],
        horizontal=True,
        index=None,
    )        
        results[10] = st.radio(
        "Help increase club membership",
        ["High Interest", "Some Interest", "No Interest"],
        horizontal=True,
        index=None,
    )        
        results[11] = st.radio(
        "Serve as a club officer",
        ["High Interest", "Some Interest", "No Interest"],
        horizontal=True,
        index=None,
    )        
        results[25] = st.text_input('Which position?')
        
        results[12] = st.radio(
        "Help the club with public relations or publicity",
        ["High Interest", "Some Interest", "No Interest"],
        horizontal=True,
        index=None,
    )        
        results[13] = st.radio(
        "Contribute to or edit the club newsletter or website",
        ["High Interest", "Some Interest", "No Interest"],
        horizontal=True,
        index=None,
    ) 

        results[14] = st.radio(
        "Learn about parliamentary procedure",
        ["High Interest", "Some Interest", "No Interest"],
        horizontal=True,
        index=None,
    )       
        st.markdown('### Outside the Club')
        results[15] = st.radio(
        "Lead or help with a Speechcraft program",
        ["High Interest", "Some Interest", "No Interest"],
        horizontal=True,
        index=None,
    )    
        results[16] = st.radio(
        "Lead or help with a Youth Leadership program",
        ["High Interest", "Some Interest", "No Interest"],
        horizontal=True,
        index=None,
    )    
        results[17] = st.radio(
        "Lead or help with a youth communication module",
        ["High Interest", "Some Interest", "No Interest"],
        horizontal=True,
        index=None,
    )    
        results[18] = st.radio(
        "Visit other Toastmasters clubs",
        ["High Interest", "Some Interest", "No Interest"],
        horizontal=True,
        index=None,
    )    
        results[19] = st.radio(
        "Compete in a speech contest",
        ["High Interest", "Some Interest", "No Interest"],
        horizontal=True,
        index=None,
    )    
        st.markdown('### Within the District')
        results[20] = st.radio(
        "Judge a speech contest",
        ["High Interest", "Some Interest", "No Interest"],
        horizontal=True,
        index=None,
    )    
        results[21] = st.radio(
        "Organize a new Toastmasters club",
        ["High Interest", "Some Interest", "No Interest"],
        horizontal=True,
        index=None,
    )    
        results[22] = st.radio(
        "Serve as a district leader",
        ["High Interest", "Some Interest", "No Interest"],
        horizontal=True,
        index=None,
    )    
        results[26] = st.text_input('Which district position?')
        st.markdown('### Other interests')

        results[27] = st.text_input('Please specify other interests not listed above')

        st.markdown('## Club Quality Characteristics')
        st.markdown('### Rate your satisfaction on each of the following club quality characteristics.')
        st.write('Welcoming')
        results[28] = st_star_rating("", maxValue=5, defaultValue=1, key="welcoming",size=25)
        
        st.write('Friendly/relaxed atmosphere')
        results[29] = st_star_rating("", maxValue=5, defaultValue=1, key="friendly",size=25)

        st.write('Positive/Supportive')
        results[30] = st_star_rating("", maxValue=5, defaultValue=1, key="positive",size=25)

        st.write('Organized meetings')
        results[31] = st_star_rating("", maxValue=5, defaultValue=1, key="organized",size=25)

        st.write('Supportive club leaders')
        results[32] = st_star_rating("", maxValue=5, defaultValue=1, key="supportive",size=25)

        st.write('Opportunities to participate')
        results[33] = st_star_rating("", maxValue=5, defaultValue=1, key="participate",size=25)
        
        st.write('Creative Table Topics®')
        results[34] = st_star_rating("", maxValue=5, defaultValue=1, key="creative",size=25)

        st.write('Effective evaluations')
        results[35] = st_star_rating("", maxValue=5, defaultValue=1, key="effective",size=25)

        st.write('Provides professional development')
        results[36] = st_star_rating("", maxValue=5, defaultValue=1, key="professional",size=25)

        st.write('A networking environment')
        results[37] = st_star_rating("", maxValue=5, defaultValue=1, key="networking",size=25)

        st.write('Promotion of club in the community')
        results[38] = st_star_rating("", maxValue=5, defaultValue=1, key="promotion",size=25)

        st.write('Varied and fun meetings')
        results[39] = st_star_rating("", maxValue=5, defaultValue=1, key="fun",size=25)

        st.write('Toastmasters sponsoring new members recognized')
        results[40] = st_star_rating("", maxValue=5, defaultValue=1, key="sponsoring",size=25)

        st.write('Member achievements formally recognized with ceremony')
        results[41] = st_star_rating("", maxValue=5, defaultValue=1, key="achievements",size=25)

        st.write('Club and member achievements publicized')
        results[42] = st_star_rating("", maxValue=5, defaultValue=1, key="publicized",size=25)                                                                                
        
        st.markdown('### Other interests')
        results[43] = st.text_input('What do you like most about your club?')
        results[44] = st.text_input('What do you like least about your club?')
        results[45] = st.text_input('What recommendations for improvement can you provide?')
        results[46] = st.text_input('Is there anything more specific you would like to learn about?')
        
        submit = st.form_submit_button('Submit')

    if submit:
        with st.spinner():
            time.sleep(2)
            current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if any((isinstance(value, str) and (value is None or not value.strip())) or 
        (isinstance(value, int) and value is None) for value in results.values()):
                
                st.error(f'Form submission on {current_datetime} failed! The form is not complete. Please fill in all the fields and try again.')            
            else:
                results = pd.DataFrame(results, index=[0])
                conn = st.connection("gsheets", type=GSheetsConnection)
                df = conn.read(worksheet="Sheet1")   
                
                df = df.append(results, ignore_index=True)
                conn.update(
                    worksheet="Sheet1",
                    data=df,)
                st.success(f'Thank you for your submission on {current_datetime}!')
                
                st.cache_data.clear()
                # reset_form()
                            
if __name__ == "__main__":
    run()
