########################################################
#              Carregando bibliotecas
########################################################

import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go

st.set_page_config(page_title = 'Single Player Vision', layout='wide', page_icon = '👤')

########################################################
#              Carregando dados tratados
########################################################

data = pd.read_csv('df_selected.csv', low_memory=False)




########################################################
#              Definindo funcoes
########################################################








########################################################
#              Layout da barra lateral
########################################################
st.sidebar.image('./pages/NBA_logo_small.png', width=120)
st.sidebar.markdown('# NBA PlayersDex - Season 22/23')
st.sidebar.markdown("""---""")


# ------------------------------------------------------
# -------------- Widgets -------------------------------
# ------------------------------------------------------
# selected_teams = st.sidebar.multiselect(label='Select the team(s)', 
#                        options=data['Tm'].unique(),
#                        default = [])
# selected_positions = st.sidebar.multiselect(label='Select the position(s)', 
#                        options=data['Pos'].unique(),
#                        default = [])
# selected_player = st.sidebar.selectbox(label='Select the player', 
#                        options=data['Player'].unique())
#Vinculando os widgets aos dados
# selected_rows = data['Tm'].isin(selected_teams)
# data = data.loc[selected_rows, :]
# selected_rows = data['Pos'].isin(selected_positions)
# data = data.loc[selected_rows, :]
# selected_rows = data[data['Player'] == selected_player]
# # data = data.loc[selected_rows, :]




#---------------------- Player selection ------------------- #
selected_player_A = st.sidebar.text_input(label="Player's name", value='Joel Embiid')
selected_data_A = data[data['Player'] == selected_player_A]


selected_player_B = st.sidebar.text_input(label="Player's name", value='Jayson Tatum')
selected_data_B = data[data['Player'] == selected_player_B]



st.sidebar.markdown('##### Powered by Bruno Piato')


#-------------------------- METRICS ------------------------ #
team = selected_data_A['Tm'].iloc[0]
position = selected_data_A['Pos'].iloc[0]
age = selected_data_A['Age'].iloc[0]
vorp = selected_data_A['VORP'].iloc[0]
obpm = selected_data_A['OBPM'].iloc[0]
dbpm = selected_data_A['DBPM'].iloc[0]
bpm = selected_data_A['BPM'].iloc[0]



team = selected_data_B['Tm'].iloc[0]
position = selected_data_B['Pos'].iloc[0]
age = selected_data_B['Age'].iloc[0]
vorp = selected_data_B['VORP'].iloc[0]
obpm = selected_data_B['OBPM'].iloc[0]
dbpm = selected_data_B['DBPM'].iloc[0]
bpm = selected_data_B['BPM'].iloc[0]










########################################################
#              Layout do corpo da página
########################################################

st.markdown("# 👥 Player Comparison Vision")
    
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('### Building')

    with col2:
        st.markdown('### Building')
