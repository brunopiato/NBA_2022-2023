import streamlit as st

st.set_page_config(
    page_title = "Home",
    page_icon = "🏀")

st.sidebar.image('/home/bruno/repos/NBA_2022-2023/streamlit/pages/NBA_logo.png', width = 160)

st.sidebar.markdown('# NBA PlayersDex - Season 22/23')
st.sidebar.markdown('## Visualizing your favorite players')
st.sidebar.markdown("""---""")

st.write('# NBA PlayersDex - Season 22/23')

st.markdown("""
            This app is intended to give you a visual analysis of your favorite players along with a comparison of a player-to-player rank for players during season 2022 and 2023
            
            ### How to use the NBA PlayersDex
            - First tab:
                - A single player vision
            - Second tab: 
                - A player-to-player comparison
            ### Ask for help
                - Via Discord
                    - @piatobruno#0143
                - Via e-mail:
                    - piatobio@gmail.com
            """)