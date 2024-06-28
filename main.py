import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st
plt.style.use("seaborn-v0_8")
data=pd.read_csv("data.csv")

#data collection for country
def country(x):
    return st.write(data[data['Nationality']==x][['Name','Overall','Potential','Position']])
x=st.text_input("Enter the country for data",value='India')
country(x)

# data collection for club
def club(x):
    return st.write(data[data['Club']==x][['Name','Jersey Number','Position','Overall','Nationality','Age','Wage',
                                    'Value','Contract Valid Until']])
x=st.text_input("Enter club for data",value='Liverpool')
club(x)

# Data cleaning for missing Data
data['ShortPassing'].fillna(data['ShortPassing'].mean(), inplace = True)
data['Volleys'].fillna(data['Volleys'].mean(), inplace = True)
data['Dribbling'].fillna(data['Dribbling'].mean(), inplace = True)
data['Curve'].fillna(data['Curve'].mean(), inplace = True)
data['FKAccuracy'].fillna(data['FKAccuracy'], inplace = True)
data['LongPassing'].fillna(data['LongPassing'].mean(), inplace = True)
data['BallControl'].fillna(data['BallControl'].mean(), inplace = True)
data['HeadingAccuracy'].fillna(data['HeadingAccuracy'].mean(), inplace = True)
data['Finishing'].fillna(data['Finishing'].mean(), inplace = True)
data['Crossing'].fillna(data['Crossing'].mean(), inplace = True)
data['Weight'].fillna('200lbs', inplace = True)
data['Contract Valid Until'].fillna(2019, inplace = True)
data['Height'].fillna("5'11", inplace = True)
data['Loaned From'].fillna('None', inplace = True)
data['Joined'].fillna('Jul 1, 2018', inplace = True)
data['Jersey Number'].fillna(8, inplace = True)
data['Body Type'].fillna('Normal', inplace = True)
data['Position'].fillna('ST', inplace = True)
data['Club'].fillna('No Club', inplace = True)
data['Work Rate'].fillna('Medium/ Medium', inplace = True)
data['Skill Moves'].fillna(data['Skill Moves'].median(), inplace = True)
data['Weak Foot'].fillna(3, inplace = True)
data['Preferred Foot'].fillna('Right', inplace = True)
data['International Reputation'].fillna(1, inplace = True)
data['Wage'].fillna('€200K', inplace = True)
data.fillna(0, inplace = True)

def extract_value_froma(value):
  out = value.replace('lbs', '')
  return float(out)
data['Weight'] = data['Weight'].apply(lambda x : extract_value_froma(x))

def extract_value_fromb(Value):
    out = Value.replace('€', '')
    if 'M' in out:
        out = float(out.replace('M', ''))*1000000
    elif 'K' in Value:
        out = float(out.replace('K', ''))*1000
    return float(out)
data['Value'] = data['Value'].apply(lambda x: extract_value_fromb(x))
data['Wage'] = data['Wage'].apply(lambda x: extract_value_fromb(x))

def defending(data):
    return int(round((data[['Marking', 'StandingTackle', 
                               'SlidingTackle']].mean()).mean()))

def general(data):
    return int(round((data[['HeadingAccuracy', 'Dribbling', 'Curve', 
                               'BallControl']].mean()).mean()))

def mental(data):
    return int(round((data[['Aggression', 'Interceptions', 'Positioning', 
                               'Vision','Composure']].mean()).mean()))

def passing(data):
    return int(round((data[['Crossing', 'ShortPassing', 
                               'LongPassing']].mean()).mean()))

def mobility(data):
    return int(round((data[['Acceleration', 'SprintSpeed', 
                               'Agility','Reactions']].mean()).mean()))
def power(data):
    return int(round((data[['Balance', 'Jumping', 'Stamina', 
                               'Strength']].mean()).mean()))

def rating(data):
    return int(round((data[['Potential', 'Overall']].mean()).mean()))

def shooting(data):
    return int(round((data[['Finishing', 'Volleys', 'FKAccuracy', 
                               'ShotPower','LongShots', 'Penalties']].mean()).mean()))

data.rename(columns={'Club Logo':'Club_Logo'}, inplace=True)



# adding these categories to the data

data['Defending'] = data.apply(defending, axis = 1)
data['General'] = data.apply(general, axis = 1)
data['Mental'] = data.apply(mental, axis = 1)
data['Passing'] = data.apply(passing, axis = 1)
data['Mobility'] = data.apply(mobility, axis = 1)
data['Power'] = data.apply(power, axis = 1)
data['Rating'] = data.apply(rating, axis = 1)
data['Shooting'] = data.apply(shooting, axis = 1)


players = data[['Name','Defending','General','Mental','Passing',
                'Mobility','Power','Rating','Shooting','Flag','Age',
                'Nationality', 'Photo', 'Club_Logo', 'Club']]

def foot():
    axa=px.histogram(data,x='Preferred Foot',title="Preferred Foot")
    axa.update_layout(title_font_size=20, width=1000, height=500)
    st.plotly_chart(axa)
def Position():
    plt.figure(figsize = (18, 8))
    plt.style.use('fivethirtyeight')
    ax = px.histogram(data, x='Preferred Foot', color='Preferred Foot', title='Most Preferred Foot of the Players')
    st.plotly_chart(ax)
def wages():
    fig = px.histogram(data, x='Wage', nbins=30, color_discrete_sequence=['blue'], title='Distribution of Wages of Players')
    fig.update_layout(
    xaxis_title='Wage Range for Players',
    yaxis_title='Count of the Players',
    title_font_size=20,
    xaxis_tickangle=90,
    width=1500,
    height=500)
    st.plotly_chart(fig)
def moves():
    fig = px.histogram(data, x='Skill Moves', color_discrete_sequence=px.colors.qualitative.Pastel, title='Count of players on Basis of their skill moves')

    fig.update_layout(
    xaxis_title='Number of Skill Moves',
    yaxis_title='Count',
    title_font_size=20,
    xaxis_tickangle=0,
    width=1000,
    height=800
)
    st.plotly_chart(fig)
def Height():
    fig = px.histogram(data, x='Height', color_discrete_sequence=px.colors.qualitative.Dark24, title='Count of players on Basis of Height')

    fig.update_layout(
    xaxis_title='Height in Foot per inch',
    yaxis_title='Count',
    title_font_size=20,
    xaxis_tickangle=0,
    width=1300,
    height=800
)
    st.plotly_chart(fig)
def Weight():
    fig = px.histogram(data, x='Weight', nbins=30, color_discrete_sequence=['pink'], title='Different Weights of the Players Participating in FIFA 2019')

    fig.update_layout(
    xaxis_title='Weights associated with the players',
    yaxis_title='Count of Players',
    title_font_size=20,
    xaxis_tickangle=0,
    width=2000,
    height=500)
    st.plotly_chart(fig)
def Parti():
    fig = px.histogram(data, x='Work Rate', color_discrete_sequence=px.colors.qualitative.Set3, title='Different work rates of the Players Participating in the FIFA 2019')

    fig.update_layout(
    xaxis_title='Work rates associated with the players',
    yaxis_title='Count of Players',
    title_font_size=20,
    xaxis_tickangle=0,
    width=1500,
    height=700
)
    st.plotly_chart(fig)
def sepsc():
    fig = px.histogram(data, x='Special', nbins=58, color_discrete_sequence=['magenta'], title='Histogram for the Speciality Scores of the Players')
    fig.update_layout(
    xaxis_title='Special score range',
    yaxis_title='Count of the Players',
    title_font_size=20,
    width=1200,
    height=800
)
    st.plotly_chart(fig)
def Psc():
    fig = px.histogram(data, x='Potential', nbins=58, color_discrete_sequence=['yellow'], title="Histogram of players' Potential Scores")
    fig.update_layout(
    xaxis_title="Player's Potential Scores",
    yaxis_title='Number of players',
    title_font_size=20,
    width=1200,
    height=800
)
    st.plotly_chart(fig)
def Npat():
    top_nationalities = data['Nationality'].value_counts().head(80).reset_index()
    top_nationalities.columns = ['Nationality', 'Count']

    fig = px.bar(top_nationalities, x='Nationality', y='Count', color_discrete_sequence=['orange'], title='Different Nations Participating in FIFA 2019')

    fig.update_layout(
    xaxis_title='Name of The Country',
    yaxis_title='Count',
    title_font_size=30,
    title_font=dict(weight='bold'),
    width=2000,
    height=700
)
    st.plotly_chart(fig)
def NatWp():
    some_countries = ('England', 'Germany', 'Spain', 'Argentina', 'France', 'Brazil', 'Italy')
    data_countries = data[data['Nationality'].isin(some_countries)]
    plt.figure(figsize=(15, 7))
    sns.violinplot(x='Nationality', y='Weight', data=data_countries, palette='Reds')
    plt.xlabel('Countries', fontsize=12)
    plt.ylabel('Weight in lbs', fontsize=12)
    plt.title('Distribution of Weight of players from different countries', fontsize=20)

    fig = px.violin(data_countries, x='Nationality', y='Weight', color='Nationality',
                    title='Distribution of Weight of players from different countries',
                    labels={'Nationality': 'Countries', 'Weight': 'Weight in lbs'})

    fig.update_layout(
        xaxis_tickangle=0,
        width=1200,
        height=600
    )

    st.plotly_chart(fig)
def Pclub():
    some_clubs = ('CD Leganés', 'Southampton', 'RC Celta', 'Empoli', 'Fortuna Düsseldorf', 'Manchester City',
              'Tottenham Hotspur', 'FC Barcelona', 'Valencia CF', 'Chelsea', 'Real Madrid')
    data_clubs = data[data['Club'].isin(some_clubs)]

    plt.figure(figsize=(15, 8))
    sns.boxplot(x='Club', y='Overall', data=data_clubs, palette='inferno')
    plt.xlabel('Some Popular Clubs', fontsize=12)
    plt.ylabel('Overall Score', fontsize=12)
    plt.title('Distribution of Overall Score in Different popular Clubs', fontsize=20)
    plt.xticks(rotation=90)

    fig = px.box(data_clubs, x='Club', y='Overall', color='Club',
                title='Distribution of Overall Score in Different popular Clubs',
                labels={'Club': 'Some Popular Clubs', 'Overall': 'Overall Score'})

    fig.update_layout(
        xaxis_tickangle=0,
        width=1200,
        height=600
    )
    st.plotly_chart(fig)
def Wclub():
    some_clubs = ('CD Leganés', 'Southampton', 'RC Celta', 'Empoli', 'Fortuna Düsseldorf', 
              'Manchester City', 'Tottenham Hotspur', 'FC Barcelona', 'Valencia CF', 
              'Chelsea', 'Real Madrid')

    data_club = data[data['Club'].isin(some_clubs)]  
    fig = px.box(data_club, x='Club', y='Wage', color='Club', title='Distribution of Wages in some Popular Clubs',
                 labels={'Club': 'Names of some popular Clubs', 'Wage': 'Distribution'})

    fig.update_layout(xaxis={'categoryorder':'total descending'})
    st.plotly_chart(fig)
def B_d():
    fig = px.scatter(data, x='BallControl', y='Dribbling', color='Preferred Foot', trendline='ols',
                 title='Ball Control vs Dribbling by Preferred Foot')
    fig.update_layout(xaxis_title='Ball Control', yaxis_title='Dribbling')
    st.plotly_chart(fig)



vis= st.selectbox("Type of Data visual: ",
                     ["Foot", 'Position and player', 'Wages',"Moves","Height","Weight","Participant","Special score","P scores","Nation Part","Nation Player Weight","Pclub","Wclub","Ballcontrol vs dribble"])

st.write("Your Visualization is: ",vis)

if vis=="Foot":
    foot()
elif vis=="Position and player":
    Position()
elif vis=="Wages":
    wages()
elif vis=="Moves":
    moves()
elif vis=="Height":
    Height()
elif vis=="weight":
    Weight()
elif vis=="Participant":
    Parti()
elif vis=="Special score":
    sepsc()
elif vis=="P scores":
    Psc()
elif vis=="Nation part":
    Npat()
elif vis=="Nation Player Weight":
    NatWp()
elif vis=="Pclub":
    Pclub()
elif vis=="Wclub":
    Wclub()
else:
    B_d()







