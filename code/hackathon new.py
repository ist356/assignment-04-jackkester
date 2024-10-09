import pandas as pd
import streamlit as st
import numpy as np
import folium
import math 
from streamlit_folium import st_folium


st.title("Local SDG Tracker")



def add_deed():
    deed_date = st.date_input('Date of Good Deed')
    sdg_type = st.selectbox('Sustainable Development Goal', ['1. No Poverty', '2. Zero Hunger', '3. Good Health and Well-being', '4. Quality Education', '5. Gender Equality', '6. Clean Water and Sanitation', '7. Affordable and Clean Energy', '8. Decent Work and Economic Growth', '9. Industry, Innovation, and Infrastructure', '10. Reduced Inequality', '11. Sustainable Cities and Communities', '12. Responsible Consumption and Production', '13. Climate Action', '14. Life Below Water', '15. Life on Land', '16. Peace and Justice Strong Institutions', '17. Partnerships to achieve the Goal'])
    deed_description = st.text_input('Description of Good Deed')
    deed_lat = st.number_input('Latitude of Good Deed')
    deed_long = st.number_input('Longitude of Good Deed')
    add_deed_button = st.button('Add Deed')

    if deed_lat not in st.session_state:
        st.session_state.deed_lat = False
    if deed_long not in st.session_state:
        st.session_state.deed_long = False

    deed_lats.append(deed_lat)
    deed_longs.append(deed_long)

         


def add_event():
    event_name = st.text_input('Name of Event')
    event_date = st.date_input('Date of Event')
    event_description = st.text_input('Description of Event')
    event_lat = st.number_input('Latitude of Event')
    event_long = st.number_input('Longitude of Event')
    add_event_button = st.button('Add Event')

    if event_lat not in st.session_state:
        st.session_state.event_lat = False
    if event_long not in st.session_state:
        st.session_state.event_long = False

    

    
    event_lats.append(event_lat)
    event_longs.append(event_long)
    

start_button = st.toggle('Start')
deed_lats = []
deed_longs = []
event_lats =[]
event_longs = []
if start_button:
    deed_dict = ({'Deed Date': [], 'Deed Type': [], 'Deed Description': [], 'Deed Lat': [], 'Deed Long': []})
    event_dict = ({'Event Name': [], 'Event Date': [], 'Event Description': [], 'Event Lat': [], 'Event Long': []})
    main_map = folium.Map(location=[0, 0], zoom_start=0)
                          
    if st.toggle("Add a Deed"):
        add_deed()
        
        
    if st.toggle("Add an Event"):
        add_event()  
    

    if st.toggle("Show Map"):
        for i in range(len(deed_lats)):
            folium.Marker([deed_lats[i], deed_longs[i]], popup='Good Deed').add_to(main_map)
        for i in range(len(event_lats)):
            folium.Marker([event_lats[i], event_longs[i]], popup='Event').add_to(main_map)
        map = st_folium(main_map)
