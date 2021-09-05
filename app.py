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

    sidebar_dropdownlist = ['Home Page','13-Dutch GP','12-Belgian GP','11-Hungarian GP','9-Austrian GP','8-Steiermark GP' ,'7-French GP','6-Baku GP','5-Monaco GP','4-Spain GP','3-Portugal GP',"2-Imola GP","1-Bahrain GP"]
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
        st.markdown("""# Formula 1 - Bahrain Grand Prix  2021""")
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
                driver_list = sorted(df_r1M['NAME'].unique())
                options = st.multiselect("Select driver",driver_list)
                if options:
                    mainrace1df =  df_r1M[df_r1M.NAME.isin(options)]
                else:
                    mainrace1df = df_r1M                 
                load_toptennracefinsh(df_r1M,sectorno)
                load_plot2(mainrace1df,0,60,85,170)
                load_plot3(mainrace1df,90,105)
        else:
            st.write("Session Data is not available.")

    elif page == '2-Imola GP':
        # Race 2 Data
        df_r2M = load_data_session('r2M')
        df_r2P1 = load_data_session('r2P1')
        df_r2P2 = load_data_session('r2P2')
        df_r2P3 = load_data_session('r2P3')
        st.markdown("""# Formula 1 - Emilia Romagna Grand Prix 2021""")
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
                driver_list = sorted(df_r2M['NAME'].unique())
                options = st.multiselect("Select driver",driver_list)
                if options:
                    mainrace2df =  df_r2M[df_r2M.NAME.isin(options)]
                else:
                    mainrace2df = df_r2M   
                load_toptennracefinsh(df_r2M,sectorno)
                load_plot2(mainrace2df,0,65,60,190)
                load_plot3(mainrace2df,75,95)
        else:
            st.write("Session Data is not available.")

    elif page == '3-Portugal GP':
        # Race 3 Data
        df_r3M = load_data_session('r3M')
        df_r3P1 = load_data_session('r3P1')
        df_r3P2 = load_data_session('r3P2')
        df_r3P3 = load_data_session('r3P3')
        st.markdown("""# Formula 1 - Grande Prémio de Portugal 2021""")
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
                driver_list = sorted(df_r3M['NAME'].unique())
                options = st.multiselect("Select driver",driver_list)
                if options:
                    mainrace3df =  df_r3M[df_r3M.NAME.isin(options)]
                else:
                    mainrace3df = df_r3M        
                load_toptennracefinsh(df_r3M,sectorno)
                load_plot2(mainrace3df,0,70,55,145)
                load_plot3(mainrace3df,77,100)
        else:
            st.write("Session Data is not available.")

    elif page == '4-Spain GP':
        # Race 4 Data
        df_r4M = load_data_session('r4M')
        df_r4P1 = load_data_session('r4P1')
        df_r4P2 = load_data_session('r4P2')
        df_r4P3 = load_data_session('r4P3')
        st.markdown("""# Formula 1 - Spanish Grand Prix 2021""")
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
                #st.write(df_r4M.describe())
                driver_list = sorted(df_r4M['NAME'].unique())
                options = st.multiselect("Select driver",driver_list)
                if options:
                    mainrace4df =  df_r4M[df_r4M.NAME.isin(options)]
                else:
                    mainrace4df = df_r4M
                load_toptennracefinsh(df_r4M,sectorno)
                load_plot2(mainrace4df,0,70,55,170)
                load_plot3(mainrace4df,77,100)
        else:
            st.write("Session Data is not available.")

    elif page == '5-Monaco GP':
        # Race 5 Data
        df_r5M = load_data_session('r5M')
        df_r5P1 = load_data_session('r5P1')
        df_r5P2 = load_data_session('r5P2')
        df_r5P3 = load_data_session('r5P3')
        st.markdown("""# Formula 1 Grand Prix De Monaco 2021""")
        # SelectBox
        testdayno = st.selectbox("Select Session",["Practice","Main Race"])
        st.write("On ", testdayno)

        if testdayno == "Practice":
            readme_text = st.markdown(read_markdown("5-Practice.md"))            
            sessionno = st.radio("Select Practice session",("Practice 1","Practice 2","Practice 3"))
            sectorno = get_sector()
            if sessionno =="Practice 1":
                if df_r5P1.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r5P1,True,sectorno)
            elif sessionno =="Practice 2":
                if df_r5P2.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r5P2,True,sectorno)
            elif sessionno =="Practice 3":
                if df_r5P3.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r5P3,True,sectorno)
        elif testdayno == "Main Race":
            sectorno = get_sector()
            if df_r5M.empty:
                st.write("Session Data is not available.")
            else:
                #st.write(df_r5M.describe())
                driver_list = sorted(df_r5M['NAME'].unique())
                options = st.multiselect("Select driver",driver_list)
                if options:
                    mainrace5df =  df_r5M[df_r5M.NAME.isin(options)]
                else:
                    mainrace5df = df_r5M
                load_toptennracefinsh(df_r5M,sectorno)
                load_plot2(mainrace5df,0,80,55,100)
                load_plot3(mainrace5df,75,80)
        else:
            st.write("Session Data is not available.")
            
    elif page == '6-Baku GP':
        # Race 6 Data
        df_r6M = load_data_session('r6M')
        df_r6P1 = load_data_session('r6P1')
        df_r6P2 = load_data_session('r6P2')
        df_r6P3 = load_data_session('r6P3')
        st.markdown("""# Formula 1 Azerbaijan Grand Prix 2021""")
        # SelectBox
        testdayno = st.selectbox("Select Session",["Practice","Main Race"])
        st.write("On ", testdayno)

        if testdayno == "Practice":
            readme_text = st.markdown(read_markdown("6-Practice.md"))            
            sessionno = st.radio("Select Practice session",("Practice 1","Practice 2","Practice 3"))
            sectorno = get_sector()
            if sessionno =="Practice 1":
                if df_r6P1.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r6P1,True,sectorno)
            elif sessionno =="Practice 2":
                if df_r6P2.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r6P2,True,sectorno)
            elif sessionno =="Practice 3":
                if df_r6P3.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r6P3,True,sectorno)
        elif testdayno == "Main Race":
            sectorno = get_sector()
            if df_r6M.empty:
                st.write("Session Data is not available.")
            else:
                #st.write(df_r6M.describe())
                driver_list = sorted(df_r6M['NAME'].unique())
                options = st.multiselect("Select driver",driver_list)
                if options:
                    mainrace6df =  df_r6M[df_r6M.NAME.isin(options)]
                else:
                    mainrace6df = df_r6M
                load_toptennracefinsh(df_r6M,sectorno)
                load_plot2(mainrace6df,0,55,70,200)
                load_plot3(mainrace6df,100,115)
        else:
            st.write("Session Data is not available.")

    elif page == '7-French GP':
        # Race 7 Data
        df_r7M = load_data_session('r7M')
        df_r7P1 = load_data_session('r7P1')
        df_r7P2 = load_data_session('r7P2')
        df_r7P3 = load_data_session('r7P3')
        st.markdown("""# Formula 1 French Grand Prix 2021""")
        # SelectBox
        testdayno = st.selectbox("Select Session",["Practice","Main Race"])
        st.write("On ", testdayno)

        if testdayno == "Practice":
            readme_text = st.markdown(read_markdown("7-Practice.md"))            
            sessionno = st.radio("Select Practice session",("Practice 1","Practice 2","Practice 3"))
            sectorno = get_sector()
            if sessionno =="Practice 1":
                if df_r7P1.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r7P1,True,sectorno)
            elif sessionno =="Practice 2":
                if df_r7P2.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r7P2,True,sectorno)
            elif sessionno =="Practice 3":
                if df_r7P3.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r7P3,True,sectorno)
        elif testdayno == "Main Race":
            sectorno = get_sector()
            if df_r7M.empty:
                st.write("Session Data is not available.")
            else:
                #st.write(df_r7M.describe())
                driver_list = sorted(df_r7M['NAME'].unique())
                options = st.multiselect("Select driver",driver_list)
                if options:
                    mainrace7df =  df_r7M[df_r7M.NAME.isin(options)]
                else:
                    mainrace7df = df_r7M
                load_toptennracefinsh(df_r7M,sectorno)
                load_plot2(mainrace7df,0,55,70,140)
                load_plot3(mainrace7df,95,105)
        else:
            st.write("Session Data is not available.")

    elif page == '8-Steiermark GP':
        # Race 48 Data
        df_r8M = load_data_session('r8M')
        df_r8P1 = load_data_session('r8P1')
        df_r8P2 = load_data_session('r8P2')
        df_r8P3 = load_data_session('r8P3')
        st.markdown("""# Formula 1 Steiermark Grand Prix 2021""")
        # SelectBox
        testdayno = st.selectbox("Select Session",["Practice","Main Race"])
        st.write("On ", testdayno)

        if testdayno == "Practice":
            readme_text = st.markdown(read_markdown("8-Practice.md"))            
            sessionno = st.radio("Select Practice session",("Practice 1","Practice 2","Practice 3"))
            sectorno = get_sector()
            if sessionno =="Practice 1":
                if df_r8P1.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r8P1,True,sectorno)
            elif sessionno =="Practice 2":
                if df_r8P2.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r8P2,True,sectorno)
            elif sessionno =="Practice 3":
                if df_r8P3.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r8P3,True,sectorno)
        elif testdayno == "Main Race":
            sectorno = get_sector()
            if df_r8M.empty:
                st.write("Session Data is not available.")
            else:
                #st.write(df_r8M.describe())
                driver_list = sorted(df_r8M['NAME'].unique())
                options = st.multiselect("Select driver",driver_list)
                if options:
                    mainrace8df =  df_r8M[df_r8M.NAME.isin(options)]
                else:
                    mainrace8df = df_r8M                  
                load_toptennracefinsh(df_r8M,sectorno)
                load_plot2(mainrace8df,0,75,50,150)
                load_plot3(mainrace8df,65,75)
        else:
            st.write("Session Data is not available.")

    elif page == '9-Austrian GP':
        # Race 9 Data
        df_r9M = load_data_session('r9M')
        df_r9P1 = load_data_session('r9P1')
        df_r9P2 = load_data_session('r9P2')
        df_r9P3 = load_data_session('r9P3')
        st.markdown("""# Formula 1 Austrian Grand Prix 2021""")
        # SelectBox
        testdayno = st.selectbox("Select Session",["Practice","Main Race"])
        st.write("On ", testdayno)

        if testdayno == "Practice":
            readme_text = st.markdown(read_markdown("9-Practice.md"))            
            sessionno = st.radio("Select Practice session",("Practice 1","Practice 2","Practice 3"))
            sectorno = get_sector()
            if sessionno =="Practice 1":
                if df_r9P1.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r9P1,True,sectorno)
            elif sessionno =="Practice 2":
                if df_r9P2.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r9P2,True,sectorno)
            elif sessionno =="Practice 3":
                if df_r9P3.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r9P3,True,sectorno)
        elif testdayno == "Main Race":
            sectorno = get_sector()
            if df_r9M.empty:
                st.write("Session Data is not available.")
            else:
                #st.write(df_r9M.describe())
                driver_list = sorted(df_r9M['NAME'].unique())
                options = st.multiselect("Select driver",driver_list)
                if options:
                    mainrace9df =  df_r9M[df_r9M.NAME.isin(options)]
                else:
                    mainrace9df = df_r9M               
                load_toptennracefinsh(df_r9M,sectorno)
                load_plot2(df_r9M,0,75,50,150)
                load_plot3(df_r9M,65,75)
        else:
            st.write("Session Data is not available.")

    elif page == '11-Hungarian GP':
        # Race 11 Data
        df_r11M = load_data_session('r11M')
        df_r11P1 = load_data_session('r11P1')
        df_r11P2 = load_data_session('r11P2')
        df_r11P3 = load_data_session('r11P3')
        st.markdown("""# Formula 1 Hungarian Grand Prix 2021""")
        # SelectBox
        testdayno = st.selectbox("Select Session",["Practice","Main Race"])
        st.write("On ", testdayno)

        if testdayno == "Practice":
            readme_text = st.markdown(read_markdown("11-Practice.md"))            
            sessionno = st.radio("Select Practice session",("Practice 1","Practice 2","Practice 3"))
            sectorno = get_sector()
            if sessionno =="Practice 1":
                if df_r11P1.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r11P1,True,sectorno)
            elif sessionno =="Practice 2":
                if df_r11P2.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r11P2,True,sectorno)
            elif sessionno =="Practice 3":
                if df_r11P3.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r11P3,True,sectorno)
        elif testdayno == "Main Race":
            sectorno = get_sector()
            if df_r11M.empty:
                st.write("Session Data is not available.")
            else:
                #st.write(df_r11M.describe())
                driver_list = sorted(df_r11M['NAME'].unique())
                options = st.multiselect("Select driver",driver_list)
                if options:
                    mainrace11df =  df_r11M[df_r11M.NAME.isin(options)]
                else:
                    mainrace11df = df_r11M                   
                load_toptennracefinsh(df_r11M,sectorno)
                load_plot2(mainrace11df,0,75,75,180)
                load_plot3(mainrace11df,75,90)

    elif page == '12-Belgian GP':
        # Race 12 Data
        df_r12M = load_data_session('r12M')
        df_r12P1 = load_data_session('r12P1')
        df_r12P2 = load_data_session('r12P2')
        df_r12P3 = load_data_session('r12P3')
        st.markdown("""# Formula 1 Belgian Grand Prix 2021""")
        # SelectBox
        testdayno = st.selectbox("Select Session",["Practice","Main Race"])
        st.write("On ", testdayno)

        if testdayno == "Practice":
            readme_text = st.markdown(read_markdown("12-Practice.md"))            
            sessionno = st.radio("Select Practice session",("Practice 1","Practice 2","Practice 3"))
            sectorno = get_sector()
            if sessionno =="Practice 1":
                if df_r12P1.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r12P1,True,sectorno)
            elif sessionno =="Practice 2":
                if df_r12P2.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r12P2,True,sectorno)
            elif sessionno =="Practice 3":
                if df_r12P3.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r12P3,True,sectorno)
        elif testdayno == "Main Race":
            sectorno = get_sector()
            if df_r12M.empty:
                st.write("Session Data is not available.")
            else:
                #st.write(df_r12M.describe())
                driver_list = sorted(df_r12M['NAME'].unique())
                options = st.multiselect("Select driver",driver_list)
                if options:
                    mainrace12df =  df_r12M[df_r12M.NAME.isin(options)]
                else:
                    mainrace12df = df_r12M         
                load_toptennracefinsh(df_r12M,sectorno)
                load_plot2(mainrace12df,0,45,75,250)
                load_plot3(mainrace12df,170,230)

        else:
            st.write("Session Data is not available.")

    elif page == '13-Dutch GP':
        # Race 12 Data
        df_r13M = load_data_session('r13M')
        df_r13P1 = load_data_session('r13P1')
        df_r13P2 = load_data_session('r13P2')
        df_r13P3 = load_data_session('r13P3')


        st.markdown("""# Formula 1 Belgian Grand Prix 2021""")
        # SelectBox
        testdayno = st.selectbox("Select Session",["Practice","Main Race"])
        st.write("On ", testdayno)

        if testdayno == "Practice":
            readme_text = st.markdown(read_markdown("13-Practice.md"))            
            sessionno = st.radio("Select Practice session",("Practice 1","Practice 2","Practice 3"))
            sectorno = get_sector()
            if sessionno =="Practice 1":
                if df_r13P1.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r13P1,True,sectorno)
            elif sessionno =="Practice 2":
                if df_r13P2.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r13P2,True,sectorno)
            elif sessionno =="Practice 3":
                if df_r13P3.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r13P3,True,sectorno)
        elif testdayno == "Main Race":
            sectorno = get_sector()
            if df_r13M.empty:
                st.write("Session Data is not available.")
            else:
                #st.write(df_r13M.describe())
                driver_list = sorted(df_r13M['NAME'].unique())
                options = st.multiselect("Select driver",driver_list)
                if options:
                    mainrace13df =  df_r13M[df_r13M.NAME.isin(options)]
                else:
                    mainrace13df = df_r13M
                load_toptennracefinsh(df_r13M,sectorno)
                load_plot2(mainrace13df,0,75,45,125)
                load_plot3(mainrace13df,70,85)

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

    elif session == 'r5P1':
        sessionfile = '5-Final_Practice1Data.json'
    elif session == 'r5P2':
        sessionfile = '5-Final_Practice2Data.json'
    elif session == 'r5P3':
        sessionfile = '5-Final_Practice3Data.json'
    elif session == 'r5M':
        sessionfile = '5-Final_MainRaceData.json'

    elif session == 'r6P1':
        sessionfile = '6-Final_Practice1Data.json'
    elif session == 'r6P2':
        sessionfile = '6-Final_Practice2Data.json'
    elif session == 'r6P3':
        sessionfile = '6-Final_Practice3Data.json'
    elif session == 'r6M':
        sessionfile = '6-Final_MainRaceData.json'

    elif session == 'r7P1':
        sessionfile = '7-Final_Practice1Data.json'
    elif session == 'r7P2':
        sessionfile = '7-Final_Practice2Data.json'
    elif session == 'r7P3':
        sessionfile = '7-Final_Practice3Data.json'
    elif session == 'r7M':
        sessionfile = '7-Final_MainRaceData.json'

    elif session == 'r8P1':
        sessionfile = '8-Final_Practice1Data.json'
    elif session == 'r8P2':
        sessionfile = '8-Final_Practice2Data.json'
    elif session == 'r8P3':
        sessionfile = '8-Final_Practice3Data.json'
    elif session == 'r8M':
        sessionfile = '8-Final_MainRaceData.json'

    elif session == 'r9P1':
        sessionfile = '9-Final_Practice1Data.json'
    elif session == 'r9P2':
        sessionfile = '9-Final_Practice2Data.json'
    elif session == 'r9P3':
        sessionfile = '9-Final_Practice3Data.json'
    elif session == 'r9M':
        sessionfile = '9-Final_MainRaceData.json'

    elif session == 'r11P1':
        sessionfile = '11-Final_Practice1Data.json'
    elif session == 'r11P2':
        sessionfile = '11-Final_Practice2Data.json'
    elif session == 'r11P3':
        sessionfile = '11-Final_Practice3Data.json'
    elif session == 'r11M':
        sessionfile = '11-Final_MainRaceData.json'

    elif session == 'r12P1':
        sessionfile = '12-Final_Practice1Data.json'
    elif session == 'r12P2':
        sessionfile = '12-Final_Practice2Data.json'
    elif session == 'r12P3':
        sessionfile = '12-Final_Practice3Data.json'
    elif session == 'r12M':
        sessionfile = '12-Final_MainRaceData.json'

    elif session == 'r13P1':
        sessionfile = '13-Final_Practice1Data.json'
    elif session == 'r13P2':
        sessionfile = '13-Final_Practice2Data.json'
    elif session == 'r13P3':
        sessionfile = '13-Final_Practice3Data.json'
    elif session == 'r13M':
        sessionfile = '13-Final_MainRaceData.json'

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