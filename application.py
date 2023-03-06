import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import preprocessor, helper
# import scipy
import plotly.express as px
import plotly.figure_factory as ff


df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')


df = preprocessor.preprocess(df, region_df)

st.sidebar.title('Olympics Analysis')
st.sidebar.image('data:image/png;base64,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')
user_menu = st.sidebar.radio(
    'Select an option',
    ('Medal Tally','Overall Analysis', 'Country-wise Analysis', 'Athlete-wise Analysis')
)

if user_menu == 'Medal Tally':
    st.sidebar.header("Medal Tally")
    years,country = helper.country_year_list(df)
    selected_year = st.sidebar.selectbox("Select Year", years)
    selected_country = st.sidebar.selectbox("Select Country", country)
    
    medal_tally = helper. fetch_medal_tally(df, selected_year, selected_country)
    
    if selected_year == 'Overall' and selected_country == 'Overall':
        st.title("Overall Tally")
    if selected_year != 'Overall' and selected_country == 'Overall':
        st.title('Medal Tally in ' + str(selected_year) + " Olympics")
    if selected_year == 'Overall' and selected_country != 'Overall':
        st.title(selected_country + " overall performance")
    if selected_year != 'Overall' and selected_country != 'Overall':
        st.title(selected_country + " performance in " + str(selected_year) + " Olympics")
    
    st.table(medal_tally)
    
if user_menu == 'Overall Analysis':
    editions = df['Year'].unique().shape[0] -1
    cities = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athletes = df['Name'].unique().shape[0]
    nations = df['region'].unique().shape[0]
    
    st.title("Top Statistics")
    col1,col2,col3 = st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)
    with col2:
        st.header("Hosts")
        st.title(cities)
    with col3:
        st.header("Sports")
        st.title(sports)
    
    col1,col2,col3 = st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)
    with col2:
        st.header("Nations")
        st.title(nations)
    with col3:
        st.header("Athletes")
        st.title(athletes)
        
    nations_over_time =  helper.data_over_time(df, 'region')
    fig = px.line(nations_over_time, x = 'Edition', y = 'region')
    st.header('Participating Nations Over Years')
    st.plotly_chart(fig)
    
    events_over_time =  helper.data_over_time(df, 'Event')
    fig = px.line(events_over_time, x = 'Edition', y = 'Event')
    st.header('Events Over the Years')
    st.plotly_chart(fig)
    
    athlete_over_time =  helper.data_over_time(df, 'Name')
    fig = px.line(athlete_over_time, x = 'Edition', y = 'Name')
    st.header('Events Over the Years')
    st.plotly_chart(fig)
    
    st.title('No. of events over time(every sport)')
    fig, ax = plt.subplots(figsize=(20,20))
    x = df.drop_duplicates(['Year', 'Sport', 'Event'])
    ax = sns.heatmap(x.pivot_table(index='Sport', columns = 'Year', values = 'Event', aggfunc ='count').fillna(0).astype('int'),annot = True)
    
    st.pyplot(fig)
    
    st.title("Most Successful Athletes")
    #add drop down
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')
    selected_sport = st.selectbox('Select a Sport', sport_list)
    
    x = helper.most_successful(df, selected_sport)
    st.table(x)
    
if user_menu == 'Country-wise Analysis':
    st.sidebar.title('Country-wise Analysis')
    #dropdown
    country_list = df['region'].dropna().unique().tolist()
    country_list.sort()
    
    selected_country = st.sidebar.selectbox('Select Country', country_list)
    
    
    country_df = helper.yearwise_medal_tally(df, selected_country)
    fig = px.line(country_df, x = 'Year', y = 'Medal')
    st.title('Medal Tally over the years')
    st.plotly_chart(fig)
    
    st.title(selected_country +' excels in the following sports')
    pt = helper.country_event_heatmap(df, selected_country)
    fig, ax = plt.subplots(figsize=(20,20))
    ax = sns.heatmap(pt, annot=True)
    st.pyplot(fig)
    
    st.title('Top 10 athletes of '+ selected_country)
    top10_df = helper.most_successful_countrywise(df, selected_country)
    st.table(top10_df)
    
if user_menu == 'Athlete-wise Analysis':
    athlete_df = df.drop_duplicates(subset = ['Name', 'region'])
        
    x1 = athlete_df['Age'].dropna()
    x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
    x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
    x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()

    st.title('Distribution of Age')
    fig = ff.create_distplot([x1, x2, x3, x4],['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'],show_hist=False,show_rug = False)
    fig.update_layout(autosize= False,width =1000,height = 600)
    st.plotly_chart(fig)
    
    # x = []
    # name = []
    # famous_sports = ['Basketball', 'Judo', 'Football', 'Tug of War', 'Athletics','Swimming','Badminton','Sailing','Gymnastics',
    #                  'Art Competions', 'Handball', 'Weightlifting','Wrestling',
    #                  'Water Polo', 'Hockey','Rowing','Fencing',
    #                  'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
    #                  'Tennis', 'Golf', 'Softball', 'Archery',
    #                  'Volleyball', 'Synchronised Swimming', 'Table Tennis', 'Baseball',
    #                  'Rhythmic Gymnastics', 'Rugby Sevens',
    #                  'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']
    # for sport in famous_sports:
    #         temp_df = athlete_df[athlete_df['Sport'] == sport]
    #         x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
    #         name.append(sport)
    
    # # fig = ff.create_distplot(x, name, show_hist = False, show_rug = False)
    # # fig.update_layout(autosize= False,width =1000,height = 600)
    # # st.title('Distribution of Age with respect to Sports (Gold Medalist)')
    # # st.plotly_chart(fig)
    
   
    # sport_list = df['Sport'].unique().tolist()
    # sport_list.sort()
    # sport_list.insert(0, 'Overall')
    # selected_sport = st.selectbox('Select a Sport', sport_list)
    
    # st.title('Height Vs Weight')
    # temp_df = helper.weight_v_height(df,selected_sport)
    # fig,ax = plt.subplots()
    # ax = sns.scatterplot(temp_df['Weight'],athlete_df['Height'], hue=temp_df['Medal'], style = temp_df['Sex'], s =60)
    # st.pyplot(fig)
    
    # st.title('Men Vs Women Participation Over the Years')
    # final = helper.men_vs_women(df)
    # fig = px.line(final, x = 'Year', y =['Male', 'Female'])
    # fig.update_layout(autosize=False, width =1000, height = 600)
    # st.plotly_chart(fig)