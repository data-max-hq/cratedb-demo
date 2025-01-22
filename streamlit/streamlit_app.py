import streamlit as st
import pandas as pd
import numpy as np
from datetime import date
from fetch_data import *
import plotly.express as px

st.set_page_config(
    page_title="CrateDB demo",
    page_icon=":package:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.header(":package:  CrateDB Demo  :package:")

# Initialize session states
if "sidebar_mode" not in st.session_state:
    st.session_state.sidebar_mode = None
if "map_data" not in st.session_state:
    st.session_state.map_data = None
if "selected_state" not in st.session_state:
    st.session_state.selected_state = None
if "incident_search" not in st.session_state:
    st.session_state.incident_search = None

# if "cratedb_client" not in st.session_state:
#     st.session_state.cratedb_client = fetch_data.cratedb_client

# Only show sidebar if not in dashboard mode
if st.session_state.sidebar_mode != "dashboards":
    with st.sidebar:
        if st.session_state.sidebar_mode == "map":
            st.title("🌎 Map 🌎")
            state_codes = [
                "US-AL", "US-AK", "US-AZ", "US-AR", "US-CA", "US-CO", "US-CT", "US-DE",
                "US-FL", "US-GA", "US-HI", "US-ID", "US-IL", "US-IN", "US-IA", "US-KS",
                "US-KY", "US-LA", "US-ME", "US-MD", "US-MA", "US-MI", "US-MN", "US-MS",
                "US-MO", "US-MT", "US-NE", "US-NV", "US-NH", "US-NJ", "US-NM", "US-NY",
                "US-NC", "US-ND", "US-OH", "US-OK", "US-OR", "US-PA", "US-RI", "US-SC",
                "US-SD", "US-TN", "US-TX", "US-UT", "US-VT", "US-VA", "US-WA", "US-WV",
                "US-WI", "US-WY"
            ]
            selected_state = st.selectbox("Select a state:", state_codes)
            col1, col2 = st.columns(2)
            
            if col1.button("Apply"):
                st.session_state.selected_state = selected_state
                st.rerun()
            
            if col2.button("Reset"):
                st.session_state.selected_state = None
                st.session_state.map_data = None
                st.rerun()

        elif st.session_state.sidebar_mode == "incident":
            st.title("⚠️ Search Incident Type ⚠️")
            search_input = st.text_input("Enter incident type:", placeholder="e.g., fire, accident, etc.")
            
            col1, col2 = st.columns(2)
            
            if col1.button("Search"):
                if search_input:
                    st.session_state.incident_search = search_input
                    st.rerun()
            
            if col2.button("Reset"):
                st.session_state.incident_search = None
                st.rerun()


# Button row
left, middle, right = st.columns(3)

if left.button("Map", icon="🌎", use_container_width=True):
    st.session_state.sidebar_mode = "map"
    st.session_state.incident_search = None
    st.rerun()

if middle.button("Search incident type", icon="⚠️", use_container_width=True):
    st.session_state.sidebar_mode = "incident"
    st.session_state.map_data = None
    st.session_state.selected_state = None
    st.rerun()

if right.button("Dashboards", icon="📊", use_container_width=True):
    st.session_state.sidebar_mode = "dashboards"
    st.session_state.map_data = None
    st.session_state.selected_state = None
    st.session_state.incident_search = None
    st.rerun()

# Main content area
if st.session_state.sidebar_mode == "dashboards":
    st.markdown("""
        <h1 style='text-align: center;'>📊 Dashboards 📊</h1>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <style>
        .horizontal-line {
            border-top: 1px solid #ccc;
            width: 100%;
            margin: 20px 0;
        }
        .vertical-divider {
            border-left: 1px solid #ccc;
            min-height: 600px;  /* Match the height of our charts */
            margin: auto;
            width: 1px;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Row 1
    row1_col1, divider1, row1_col2 = st.columns([0.495, 0.01, 0.495])
    with row1_col1:
        st.header("1. Daily Fires")
        columns, results = fetch_daily_fires()
        df = pd.DataFrame(results, columns=columns)
        df['discovery_date'] = pd.to_datetime(df['discovery_date'], unit='ms').dt.strftime('%B %d')
        df = df.sort_values('discovery_date')
        
        fig = px.line(
            df,
            x='discovery_date',
            y='number_of_fires',
            title='Number of Fire Incidents Over Time',
            labels={
                'discovery_date': '',
                'number_of_fires': 'Number of Fires'
            }
        )
    
        fig.update_layout(
            height=500,
            width=800,
            yaxis_title="Number of Fires",
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)

    with divider1:
        st.markdown('<div class="vertical-divider"></div>', unsafe_allow_html=True)
    
    with row1_col2:
        st.header("2. Emergency Call Distribution")
        
        columns, results = fetch_calls_by_topic()
        df = pd.DataFrame(results, columns=columns)
        
        import plotly.express as px
        
        fig = px.pie(
            df,
            values='call_count',
            names='emergency_type',
            title='Distribution of emergency calls by type',
            hover_data=['percentage'],
            labels={'percentage': 'Percentage (%)'}
        )
        
        fig.update_layout(
            height=500,
            width=800,
            showlegend=True,
            legend=dict(
                yanchor="top",
                y=0.99,
                xanchor="left",
                x=0.01
            )
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown('<div class="horizontal-line"></div>', unsafe_allow_html=True)
    
    # Row 2
    row2_col1, divider2, row2_col2 = st.columns([0.495, 0.01, 0.495])
    with row2_col1:
        st.header("3. Fire Size Distribution")
        
        columns, results = fetch_size_distribution()
        df = pd.DataFrame(results, columns=columns)
        
        fig = px.bar(
            df,
            x='size_category',
            y='number_of_fires',
            title='Distribution of Fires by Size',
            text='number_of_fires',
            labels={
                'size_category': 'Fire Size Category',
                'number_of_fires': 'Number of Fires'
            }
        )
        
        # Update layout
        fig.update_layout(
            height=500,
            width=800,
            yaxis_title="Number of Fires",
            showlegend=False,
            uniformtext_minsize=8,
            uniformtext_mode='hide'
        )
        
        fig.update_traces(
            texttemplate='%{text}',
            textposition='outside'
        )
        
        st.plotly_chart(fig, use_container_width=True)

    with divider2:
        st.markdown('<div class="vertical-divider"></div>', unsafe_allow_html=True)
    
    with row2_col2:
        st.header("4. Fires in LA County Area")
        st.write("Wildfires within the specified area (Long Beach to Angeles National Forest)")
        
        columns, results = fetch_fires_in_area()
        df = pd.DataFrame(results, columns=columns)
        
        df['lat'] = df['geometry'].apply(lambda x: x[1])
        df['lon'] = df['geometry'].apply(lambda x: x[0])
        
        st.write(f"Number of fires in area: {len(df)}")
        st.code('POLYGON((-118.6 33.9, -118.6 34.7, -117.8 34.7, -117.8 33.9, -118.6 33.9))')
        
        st.map(
            df[['lat', 'lon']],
            use_container_width=True,
            height=400  
        )


elif st.session_state.sidebar_mode == "map":
    st.markdown("""
        <h2 style='text-align: center;'>Wildfire Map</h2>
    """, unsafe_allow_html=True)
    
    if st.session_state.map_data is None:
        columns, results = fetch_all_fire()
        df = pd.DataFrame(results, columns=columns)

        # st.map expects lon and lat columns
        if 'location' in df.columns:
            df['lon'] = df['location'].apply(lambda x: x[0])
            df['lat'] = df['location'].apply(lambda x: x[1])
            df = df.drop('location', axis=1)

        st.session_state.map_data = df

    if st.session_state.selected_state:
        filtered_df = st.session_state.map_data[
            st.session_state.map_data['poo_state'] == st.session_state.selected_state
        ]
        st.map(filtered_df)
    else:
        st.map(st.session_state.map_data)

elif st.session_state.sidebar_mode == "incident":
    st.subheader("Emergency Calls Records:  Jan-Feb 2025")
    columns, results = fetch_all_emergency_calls()
    df = pd.DataFrame(results, columns=columns)
    df['created_at'] = pd.to_datetime(df['created_at'], unit='ms').dt.strftime('%B %d %Y')
    
    # If there's a search, filter the dataframe
    if st.session_state.incident_search:
        columns, results = fetch_emergency_calls_search(st.session_state.incident_search)
        df = pd.DataFrame(results, columns=columns)
        df['created_at'] = pd.to_datetime(df['created_at'], unit='ms').dt.strftime('%B %d %Y')
    
    st.dataframe(df)