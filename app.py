import pandas as pd 
import plotly.express as px
import streamlit as st


st.set_page_config(page_title="App  Dashboard",
 		page_icon=":bar_chart:", 
 		layout="wide")


@st.cache
def get_data_from_excel():
	df=pd.read_excel(
	io='findingsv2.xlsx',
	engine='openpyxl',
	sheet_name='findingsv2',
	skiprows=0,
	usecols='A:K',
	nrows=1000,
	)
	return df
df = get_data_from_excel()


dfdef = df.loc[df.category == 'browser']

st.sidebar.header("Please Filter Here:")
category = st.sidebar.selectbox(
    "Select app Category",
    options=df["category"].unique(),
    #default=dfdef["category"].unique()
)



df_selection = df.query(
    "category == @category"
)


st.title(":bar_chart: App Recommendation Dashboard")
st.markdown("##")


fig_app_rank = px.bar(
	df_selection,
    x='score',
    y='appId',	
    orientation="h",
    title="<b>App ranking</b>",
    template="plotly_white",
)

fig_app_rank.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
    
)
st.plotly_chart(fig_app_rank)


		



# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)