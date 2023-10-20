# Israel-conflict-analysis
It is the conflict analysis between Israel and Palestine from 2000 to 2023(before war of 2023). I have analysed the tension between Israel and Palestine during the years 2000 to 2023 before the war started as people are getting updates regarding the current situation but I wanted to analyse whatever happened between them during these 20 to 23 years and how many fatalities were there and various other details regarding the same.

Technologies/tools used are :-

1) Python
2) SQL
3) plotly
4) pandas
   
The dataset is taken from kaggle and under description, it was written by the author that they have collected the data from the government released data of the Israel Government.

I have done data cleaning, data preprocessing and initial analysing using SQL and then used SQL and pandas with python for further data manipulation and analyzing the data. I used psycopg2 to link the database with python so that I can link both of them together and use SQL queries in python for further data manipulation and analyzing.

I have used Python and visualization library i.e 'plotly' for the visualization of the data.

**Note :- All the Visuals support for Hover Tool, so you can hover and see the exact data/insight that the visual represents to have an exact understanding about the data.**

Now let's underastand about the different visualization to have a better understanding about the conflict


1) **Fatalities Divided across Districts and Regions**


   ![Fatalities divided across districts and regions](https://github.com/ujjwal717/Israel-conflict-analysis/assets/93403224/a22b4426-1014-41ed-a261-ae22e50ebe3c)

   **Explanation** :- Here, we have divided the fatalities according to the various districts present across the regions such as "Israel", "West Bank" and "Gaza Strip". So you can see that the districts are divided according to the regions by using 'legends' and the amount of fatalities are represented using scatterplots.

   **Insight :-** I found that the districts of "Gaza Strip" has maximum number of fatalities across these years and those districts include - "Gaza", "Deir al-Balah", "North Gaza" , "Khan Yunis" , "Rafah". Also the districts of "West Bank" also include the fatalities but they are less in amount if we compare them with "Gaza Strip".

   


 
**Fatalities Divided According to Years**


 
 ![fatalities divided according to years](https://github.com/ujjwal717/Israel-conflict-analysis/assets/93403224/0251c1a7-597f-4072-a4ed-699483f11b56)



   **Explanation** :- In this visual, we have divided the fatalities according to the different years, It has various years across the X-Axis while the count or amount of fatalities across the Y-Axis.

   

   **Insight :-** I found that the maximum amount of fatalities were recorded in 2014 and the reason for that was the "2014 Gaza Conflict" and in a nuthsell, there was fight between the regions which led a lot of fatalities which can be seen from the visual that 2014 recorded maximum amount of fatalities. Also, 2002 also recorded great amount of fatalities which was also due to the battle between the regions which has a detailed explanation of the battle on wikipedia (https://en.wikipedia.org/wiki/Timeline_of_the_Israeli%E2%80%93Palestinian_conflict_in_2002).





3) **Count and Percentage of Fatalities killed according to Forces/Civilians**


![count and percentage of fatalities killed according to forces](https://github.com/ujjwal717/Israel-conflict-analysis/assets/93403224/03224ab3-4b60-4adc-a911-cb0812f049be)



**Explanation** :- Here we have used a donut chart that shows us the count as well as the percentage of the fatalities that were killed either by israeli/palestinian civilians or Israel Security Forces.



**Insight :-** I found that around 90 Percent (10,000) fatalities were killed by the Israel Security Forces while 9.2 Percent(1028) fatalities were killed by Palestinian Civilians and 0.86 Percent(96) fatalities were killed by Israeli Civilians.

    



   

