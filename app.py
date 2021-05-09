import streamlit as st
import pandas as pd
import json
import sys
import plotly.express as px
import plotly.graph_objects as go
import math


COLOR = "black"
BACKGROUND_COLOR = "#fff"


def main():
    load_pages()
    select_block_container_style()


def load_pages():

    sidebar_dropdownlist = ['Home Page','4-Spain GP','3-Portugal GP',"2-Imola GP","1-Bahrain GP"]
    page = st.sidebar.selectbox("Choose a page", sidebar_dropdownlist)

    if page == 'Home Page':
        st.title('Formula 1 2021 Season')
        st.write("")
        st.write("Here is the interactive timing charts for lap times clocked by drivers of respective team during the Formula 1 2021 season.")
        st.write('')
        st.write("")
        st.text('Select a page in the sidebar')
        st.write("")
        st.write("Note : These charts are best to view in bigger screens")
        st.write("The interactive charts are created using plotly and the devlopment of user interface is done with streamlit nd deployed in heroku")

    elif page == '1-Bahrain GP':
        # Race 1 Data
        df_r1M = load_data_session('r1M')
        df_r1P1 = load_data_session('r1P1')
        df_r1P2 = load_data_session('r1P2')
        df_r1P3 = load_data_session('r1P3')
        st.markdown("""# Formula 1 - Bahrain Grand Prix  2021 at Bahrain International Circuit, Sakhir""")
        # SelectBox
        testdayno = st.selectbox("Select Session",["Practice","Main Race"])
        st.write("On ", testdayno)
        if testdayno == "Practice":
            readme_text = st.markdown(read_markdown("1-Practice.md"))            
            sessionno = st.radio("Select Practice session",("Practice 1","Practice 2","Practice 3"))
            sectorno = get_sector()
            if sessionno =="Practice 1":
                if df_r1P1.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r1P1,True,sectorno)
            elif sessionno =="Practice 2":
                if df_r1P2.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r1P2,True,sectorno)
            elif sessionno =="Practice 3":
                if df_r1P3.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r1P3,True,sectorno)
        elif testdayno == "Main Race":
            sectorno = get_sector()
            if df_r1M.empty:
                st.write("Session Data is not available.")
            else:
                #st.write(df_r1M.describe())                
                load_toptennracefinsh(df_r1M,sectorno)
                load_plot2(df_r1M,0,60,85,170)
                load_plot3(df_r1M,90,105)
        else:
            st.write("Session Data is not available.")

    elif page == '2-Imola GP':
        # Race 2 Data
        df_r2M = load_data_session('r2M')
        df_r2P1 = load_data_session('r2P1')
        df_r2P2 = load_data_session('r2P2')
        df_r2P3 = load_data_session('r2P3')
        st.markdown("""# Formula 1 - Emilia Romagna Grand Prix at Autodromo Enzo e Dino Ferrari, Italy""")
        # SelectBox
        testdayno = st.selectbox("Select Session",["Practice","Main Race"])
        st.write("On ", testdayno)

        if testdayno == "Practice":
            readme_text = st.markdown(read_markdown("2-Practice.md"))            
            sessionno = st.radio("Select Practice session",("Practice 1","Practice 2","Practice 3"))
            sectorno = get_sector()
            if sessionno =="Practice 1":
                if df_r2P1.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r2P1,True,sectorno)
            elif sessionno =="Practice 2":
                if df_r2P2.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r2P2,True,sectorno)
            elif sessionno =="Practice 3":
                if df_r2P3.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r2P3,True,sectorno)
        elif testdayno == "Main Race":
            sectorno = get_sector()
            if df_r2M.empty:
                st.write("Session Data is not available.")
            else:
                #st.write(df_r2M.describe())                
                load_toptennracefinsh(df_r2M,sectorno)
                load_plot2(df_r2M,0,65,60,190)
                load_plot3(df_r2M,75,95)
        else:
            st.write("Session Data is not available.")

    elif page == '3-Portugal GP':
        # Race 3 Data
        df_r3M = load_data_session('r3M')
        df_r3P1 = load_data_session('r3P1')
        df_r3P2 = load_data_session('r3P2')
        df_r3P3 = load_data_session('r3P3')
        st.markdown("""# Formula 1 - Grande Prémio de Portugal at Algarve International Circuit, Portugal""")
        # SelectBox
        testdayno = st.selectbox("Select Session",["Practice","Main Race"])
        st.write("On ", testdayno)

        if testdayno == "Practice":
            readme_text = st.markdown(read_markdown("3-Practice.md"))            
            sessionno = st.radio("Select Practice session",("Practice 1","Practice 2","Practice 3"))
            sectorno = get_sector()
            if sessionno =="Practice 1":
                if df_r3P1.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r3P1,True,sectorno)
            elif sessionno =="Practice 2":
                if df_r3P2.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r3P2,True,sectorno)
            elif sessionno =="Practice 3":
                if df_r3P3.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r3P3,True,sectorno)
        elif testdayno == "Main Race":
            sectorno = get_sector()
            if df_r3M.empty:
                st.write("Session Data is not available.")
            else:
                #st.write(df_r3M.describe())                
                load_toptennracefinsh(df_r3M,sectorno)
                load_plot2(df_r3M,0,70,55,145)
                load_plot3(df_r3M,77,100)
        else:
            st.write("Session Data is not available.")

    elif page == '4-Spain GP':
        # Race 4 Data
        df_r4M = load_data_session('r4M')
        df_r4P1 = load_data_session('r4P1')
        df_r4P2 = load_data_session('r4P2')
        df_r4P3 = load_data_session('r4P3')
        st.markdown("""# Formula 1 - Spanish Grand Prix at Circuit de Barcelona-Catalunya, Spain""")
        # SelectBox
        testdayno = st.selectbox("Select Session",["Practice","Main Race"])
        st.write("On ", testdayno)

        if testdayno == "Practice":
            readme_text = st.markdown(read_markdown("4-Practice.md"))            
            sessionno = st.radio("Select Practice session",("Practice 1","Practice 2","Practice 3"))
            sectorno = get_sector()
            if sessionno =="Practice 1":
                if df_r4P1.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r4P1,True,sectorno)
            elif sessionno =="Practice 2":
                if df_r4P2.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r4P2,True,sectorno)
            elif sessionno =="Practice 3":
                if df_r4P3.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r4P3,True,sectorno)
        elif testdayno == "Main Race":
            sectorno = get_sector()
            if df_r4M.empty:
                st.write("Session Data is not available.")
            else:
                st.write(df_r4M.describe())                
                load_toptennracefinsh(df_r4M,sectorno)
                load_plot2(df_r4M,0,70,55,145)
                load_plot3(df_r4M,77,100)
        else:
            st.write("Session Data is not available.")


    else:
        st.text('Select a page in the sidebar')
        
def get_sector():
    sector = st.selectbox("Select Sector",["Overall","Sector 1","Sector 2","Sector 3"])
    #sectorno = "S123"
    if sector == "Overall":
        sectorno = "S123"
    elif sector == "Sector 1":
        sectorno = "S1"
    elif sector == "Sector 2":
        sectorno = "S2"
    elif sector == "Sector 3":
        sectorno = "S3"
    else:
        sectorno = "S123"
    return sectorno


def load_plots(df,ispractice,sectorno):
    #st.write(df.describe())
    if ispractice:

        maxlapval = df["LAPS"].max()
        rounded_maxlapsval = int(math.ceil(maxlapval / 5.0)) * 5

        meansectorval = df[sectorno].mean()
        rounded_meansectorval = int(math.ceil(meansectorval / 5.0)) * 7.5

        minsectorval = df[sectorno].min()
        rounded_minsectorval = (int(math.floor(minsectorval / 5.0)) * 5) - 10

        maxectorval = df[sectorno].max()
        rounded_max123val = (int(math.floor(maxectorval / 5.0)) * 5) + 20

        excludeoutlap = st.radio("Exclude Out Laps?",("Yes","No"))
        if excludeoutlap == "Yes":
            newdf1 = df[df[sectorno] < meansectorval]
            topdf = newdf1.groupby(['NAME','N'])[sectorno].mean().reset_index(level='NAME').sort_values(by=sectorno,ascending=True)
            top10df = topdf.head(10)
            st.markdown("""#### Top 10 drivers based on average laptime in this session.""")
            st.text("Select the above dropdown to get performance by sector.")
            st.table(top10df[['NAME',sectorno]])
        else:
            newdf1 = df

        load_plot1(newdf1,0,rounded_maxlapsval,rounded_minsectorval,rounded_max123val,sectorno)

        newdf2 = df[df[sectorno] < rounded_meansectorval]
        load_plot4(newdf2,rounded_minsectorval,rounded_meansectorval,sectorno)

@st.cache
def load_data_session(session):
    sessionfile = ''
    jsondata = '{}'
    if session == 'r1P1':
        sessionfile = '1-Final_Practice1Data.json'
    elif session == 'r1P2':
        sessionfile = '1-Final_Practice2Data.json'
    elif session == 'r1P3':
        sessionfile = '1-Final_Practice3Data.json'
    elif session == 'r1M':
        sessionfile = '1-Final_MainRaceData.json'

    elif session == 'r2P1':
        sessionfile = '2-Final_Practice1Data.json'
    elif session == 'r2P2':
        sessionfile = '2-Final_Practice2Data.json'
    elif session == 'r2P3':
        sessionfile = '2-Final_Practice3Data.json'
    elif session == 'r2M':
        sessionfile = '2-Final_MainRaceData.json'

    elif session == 'r3P1':
        sessionfile = '3-Final_Practice1Data.json'
    elif session == 'r3P2':
        sessionfile = '3-Final_Practice2Data.json'
    elif session == 'r3P3':
        sessionfile = '3-Final_Practice3Data.json'
    elif session == 'r3M':
        sessionfile = '3-Final_MainRaceData.json'

    elif session == 'r4P1':
        sessionfile = '4-Final_Practice1Data.json'
    elif session == 'r4P2':
        sessionfile = '4-Final_Practice2Data.json'
    elif session == 'r4P3':
        sessionfile = '4-Final_Practice3Data.json'
    elif session == 'r4M':
        sessionfile = '4-Final_MainRaceData.json'


    colorcodedf = get_colorcode()
    if sessionfile != '':     
        with open(sessionfile) as json_file:
            jsondata = json.load(json_file)
        data = pd.DataFrame(jsondata)
        if data.empty:
            data = data
        else:
            data = data.merge(colorcodedf,how="left",on="N")
    else:
        data = pd.DataFrame()
    return data

def load_plot1(df,startlap,endlap,mintime,maxtime,sectorno):
    st.markdown("""#### Lap time clocked and trendline during the session """)
    df = df.sort_values(['N'],ascending=[1])
    color_dict = dict(zip(df.NAME, df.COLORCODE))
    fig = px.scatter(df, x="LAPS", y=sectorno, color="NAME",template="ggplot2",width=1200,height=600, hover_name="TYRE",trendline="lowess",color_discrete_map=color_dict)
    fig.update_xaxes(range=[startlap,endlap],title_text='Lap Number')
    fig.update_yaxes(range=[mintime,maxtime],title_text='Total sector time')
    fig.update_layout(plot_bgcolor ='#eeeeee',legend_bgcolor='#eeeeee')
    st.plotly_chart(fig)

def load_plot2(df,startlap,endlap,mintime,maxtime):
    st.markdown("""#### Lap time clocked and trendline during the session """)
    df = df.sort_values(['N'],ascending=[1])
    color_dict = dict(zip(df.DRIVERCODE, df.COLORCODE))
    fig = px.scatter(df, x="LAPNO", y="S123", color="DRIVERCODE",template="ggplot2",width=1200,height=600, hover_name="TYRE",trendline="lowess",color_discrete_map=color_dict)
    fig.update_xaxes(range=[startlap,endlap],title_text='Lap Number')
    fig.update_yaxes(range=[mintime,maxtime],title_text='Total sector time')
    fig.update_layout(plot_bgcolor ='#eeeeee',legend_bgcolor='#eeeeee')
    st.plotly_chart(fig)

def load_plot3(df,mintime,maxtime):
    st.markdown("""#### Heatmap which provides an overview of the push laps during the race""")
    df = df.sort_values(['N'],ascending=[1])
    dataset = df.pivot("LAPNO", "DRIVERCODE", "S123")
    fig = go.Figure(data=go.Heatmap(df_to_plotly(dataset),colorscale='speed',hovertemplate='Driver Code: %{x}<br>Lap No.: %{y}<br>Lap Time: %{z}<extra></extra>'))
    fig.update_layout(
    xaxis=dict(title = "Driver Code"),
    yaxis=dict(tickmode = 'linear',tick0 = 0,dtick = 1,title = "Lap No."),showlegend = True,width = 1200, height = 1000,autosize = True,yaxis_autorange='reversed'
    )
    fig.data[0].update(zmin=mintime, zmax=maxtime)
    st.plotly_chart(fig)

def load_plot4(df,mintime,maxtime,sectorno):
    df = df.sort_values(['N'],ascending=[1])
    color_dict = dict(zip(df.NAME, df.COLORCODE))
    optiontyres = st.radio("By Tyre Compound or Overall?",("Overall","Tyre Compound"))
    if optiontyres == "Overall":
        fig = px.box(df, x="NAME", y=sectorno,color ="NAME",width=1200,height=600,color_discrete_map=color_dict)
        fig.update_xaxes(title_text='Name')
    if optiontyres =="Tyre Compound":
        fig = px.box(df, x="TYRECOMPOUND", y=sectorno,color="NAME",width=1200,height=600,color_discrete_map=color_dict)
        fig.update_xaxes(title_text='Tyre Compounds')
    fig.update_layout(plot_bgcolor ='#eeeeee',legend_bgcolor='#eeeeee')
    fig.update_yaxes(range=[mintime,maxtime],title_text='Total sector time')
   
    st.plotly_chart(fig)

def load_toptennracefinsh(df,sectorno):
    df = df[df['LAPNO'] != 1]
    meansectorval = df[sectorno].mean()
    newdf1 = df[df[sectorno] < meansectorval]
    topdf = newdf1.groupby(['NAME','N'])[sectorno].mean().reset_index(level='NAME').sort_values(by=sectorno,ascending=True)
    top10df = topdf.head(10)
    st.markdown("""#### Top 10 drivers based on average laptime.""")
    st.text("Select the above dropdown to get performance by sector.")
    st.table(top10df[['NAME',sectorno]])

def read_markdown(markdownfile):
    markdowncontentstr =""
    if markdownfile != "":
        markdowncontentstr = """{}""".format(open(markdownfile).read())
    return markdowncontentstr

def select_block_container_style():
    """Add selection section for setting setting the max-width and padding
    of the main block container"""

    max_width_100_percent = st.sidebar.checkbox("Set max width to 100%", False)
    if not max_width_100_percent:
        max_width = 1400
    else:
        max_width = 2000
    padding_top = 5
    padding_right = 1
    padding_left = 1
    padding_bottom = 10


    _set_block_container_style(
        max_width,
        max_width_100_percent,
        padding_top,
        padding_right,
        padding_left,
        padding_bottom,
    )

def get_colorcode():
    colorcodedf = pd.read_csv('ColorCodes.csv',index_col=False,header=0)
    return colorcodedf

def df_to_plotly(df):
    return {'z': df.values.tolist(),
            'x': df.columns.tolist(),
            'y': df.index.tolist()}

def _set_block_container_style(max_width: int = 1200,max_width_100_percent: bool = False,padding_top: int = 5,padding_right: int = 1,padding_left: int = 1,padding_bottom: int = 10):
    if max_width_100_percent:
        max_width_str = f"max-width: 100%;"
    else:
        max_width_str = f"max-width: {max_width}px;"
    st.markdown(
        f"""
<style>
    .reportview-container .main .block-container{{
        {max_width_str}
        padding-top: {padding_top}rem;
        padding-right: {padding_right}rem;
        padding-left: {padding_left}rem;
        padding-bottom: {padding_bottom}rem;
    }}
    .reportview-container .main {{
        color: {COLOR};
        background-color: {BACKGROUND_COLOR};
    }}
</style>
""",
        unsafe_allow_html=True,
    )



if __name__ == '__main__':
    main()