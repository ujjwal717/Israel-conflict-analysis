import psycopg2
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

db_link = psycopg2.connect("dbname = <database name> user = <database user name> password = <database password>")

def people_citienship():
    df_israeli = pd.read_sql('''SELECT COUNT(serial_id) AS died_people_count, citizenship FROM war_data WHERE citizenship = 'Israeli' GROUP BY citizenship''', db_link)

    df_american = pd.read_sql('''SELECT COUNT(serial_id) AS died_people_count, citizenship FROM war_data WHERE citizenship = 'American' GROUP BY citizenship''', db_link)

    df_palestinian = pd.read_sql('''SELECT COUNT(serial_id) AS died_people_count, citizenship FROM war_data WHERE citizenship = 'Palestinian' GROUP BY citizenship''', db_link)

    df_jordanian = pd.read_sql('''SELECT COUNT(serial_id) AS died_people_count, citizenship FROM war_data WHERE citizenship = 'Jordanian' GROUP BY citizenship''', db_link)

    df_all_data = pd.concat([df_israeli,df_american,df_palestinian,df_jordanian ])

    fig_1 = px.bar(df_all_data, x='citizenship', y='died_people_count', color='citizenship', height=600, width = 1000,text_auto='.1s' , title = 'FATALITIES DIVIDED ACCORDING TO THEIR CITIZENSHIP')

    fig_1.update_traces( textposition="outside")

    fig_1.update_traces(hovertemplate='<br>Citizenship: %{x}<br>Count of Fatalitites: %{y}')

    fig_1.show()


def event_location():
    df_region = pd.read_sql('''SELECT COUNT(serial_id) AS fatalities_count,event_location_region FROM war_data GROUP BY event_location_region ''', db_link)

    fig_2 = px.funnel(df_region, x='fatalities_count',y='event_location_region', title = 'FATALITITES DIVIDED ACCORDING TO THE REGIONS', hover_data=["fatalities_count", "event_location_region"])

    fig_2.update_traces(hovertemplate='<br>Count of Fatalities: %{x}<br>Region: %{y}')

    fig_2.show()


def fatalities_age():
    df_age_sum = pd.read_sql('''SELECT COUNT(serial_id) AS "Count of Fatalities", age FROM war_data GROUP BY age''', db_link)

    fig_3 = px.bar(df_age_sum, x='age', y='Count of Fatalities',color='Count of Fatalities', title = 'FATALITIES DIVIDED ACCORDING TO THE AGE')

    fig_3.update_xaxes(rangeslider_visible=True)

    fig_3.update_traces(hovertemplate='<br>Age: %{x}<br>Count of Fatalities of this Age: %{y}')

    fig_3.show()

def fatalities_gender():
    df_gender_sum = pd.read_sql('''SELECT COUNT(serial_id) AS "Count of Fatalities", gender FROM war_data GROUP BY gender''', db_link)

    fig_4 = px.bar(df_gender_sum, x='Count of Fatalities', y='gender', color = 'Count of Fatalities', title = 'FATALITIES DIVIDED ACCORDING TO GENDER')

    fig_4.show()


def fatalities_injury_type():
    df_injury_type = pd.read_sql('''SELECT DISTINCT type_of_injury,COUNT(serial_id) AS fatalities_count,event_location_region FROM war_data GROUP BY type_of_injury,event_location_region''', db_link)

    fig_5 = go.Figure(data=go.Heatmap(z = df_injury_type["fatalities_count"],x = df_injury_type["type_of_injury"],y = df_injury_type["event_location_region"],hoverongaps=False,zmin=0, zmax=10000))

    fig_5.update_layout(xaxis_showgrid=False, yaxis_showgrid=False,xaxis_zeroline=False, yaxis_zeroline=False, title = 'FATALITIES ACCORDING TO INJURY TYPE AND REGIONS' )

    fig_5.update_traces(hovertemplate='<br>Type of Injury: %{x}<br>Region: %{y} <br>Count of Fatalities: %{z}')

    fig_5.show()


def fatalities_killed_by():
    df_killed_by = pd.read_sql('''SELECT DISTINCT killed_by AS "Killed By", COUNT(serial_id) AS "Killing Count" FROM war_data GROUP BY killed_by''', db_link)

    fig_6 = go.Figure(data=[go.Pie(labels=df_killed_by['Killed By'] , values=df_killed_by['Killing Count'], hole=.3)])

    fig_6.update_layout(title = 'COUNT AND PERCENTAGE OF FATALITIES KILLED ACCORDING TO FORCES/CITIZENS')

    fig_6.show()


def fatalities_death_date():
    df_date_of_death = pd.read_sql('''SELECT DISTINCT EXTRACT (YEAR FROM date_of_death) AS "Year", COUNT(serial_id) OVER(PARTITION BY EXTRACT (YEAR FROM date_of_death)) AS "Count of Fatalities" FROM war_data''', db_link)

    print(df_date_of_death)

    fig_7 = px.histogram(df_date_of_death, x="Year", y="Count of Fatalities", title="FATALITIES DIVIDED ACCORDING TO YEARS")

    fig_7.update_traces(xbins_size="M1")

    fig_7.update_xaxes(showgrid=True, ticklabelmode="period", dtick="M1", tickformat="%b\n%Y")

    fig_7.update_layout(bargap=0.2,yaxis_title = "Count of Fatalities" )

    fig_7.add_trace(go.Scatter(mode="markers",x=df_date_of_death['Year'], y=df_date_of_death["Count of Fatalities"], name="FATALITIES PER YEAR"))

    fig_7.show()


def fatalities_district():

    df_districts = pd.read_sql('''SELECT DISTINCT event_location_district AS "District", event_location_region AS "Region", COUNT(serial_id) AS "Fatalities Count" FROM war_data GROUP BY event_location_district,event_location_region''', db_link)

    print(df_districts)

    fig_8 = px.strip(df_districts, x='District', y='Fatalities Count', color = 'Region', title = "FATALITIES DIVIDED ACROSS DISTRICTS AND REGIONS")

    fig_8.update_traces(marker={'size': 15})

    fig_8.show()


fatalities_district()
fatalities_death_date()
fatalities_killed_by()
fatalities_injury_type()
fatalities_gender()
fatalities_age()
event_location()
people_citienship()

db_link.close()
