import streamlit as st
from datetime import date

st.set_page_config(
    page_title="CrateDB demo",
    page_icon=":package:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.header(":package:  CrateDB Demo  :package:")

if "sidebar_mode" not in st.session_state:
    st.session_state.sidebar_mode = None

with st.sidebar:
    if st.session_state.sidebar_mode == "map":
        st.title("🌎 Map 🌎")
        cities_list = [
            "Los Angeles", "New York", "Chicago", "Houston",
            "Phoenix", "Philadelphia", "San Antonio", "San Diego",
            "Dallas", "San Jose",
        ]
        selected_city = st.selectbox("Select a city", cities_list)
        st.write(f"You selected {selected_city}")
        start_time = st.slider(
            "Select Date:",
            value=date(2025, 1, 1),
            format="MM/DD/YY",
        )
        st.write("Date:", start_time)
        st.button("Apply")
    elif st.session_state.sidebar_mode == "incident":
        st.title("⚠️ Search Incident Type ⚠️")
        # st.write("\n\n\nEnter incident type:")
        st.text_input("Enter incident type:", placeholder="e.g., fire, accident, etc.")
        st.button("Search")

    elif st.session_state.sidebar_mode == "dashboards":
        st.title("📊 Dashboards 📊")
        st.button("Apply")
    else:
        st.title(":package: CrateDB demo :package:")
        st.write("Select an option to display sidebar content.")

left, middle, right = st.columns(3)

if left.button("Map", icon="🌎", use_container_width=True):
    st.session_state.sidebar_mode = "map" 
    st.rerun()

if middle.button("Search incident type", icon="⚠️", use_container_width=True):
    st.session_state.sidebar_mode = "incident"
    st.rerun()

if right.button("Dashboards", icon="📊", use_container_width=True):
    st.session_state.sidebar_mode = "dashboards"
    st.rerun()
