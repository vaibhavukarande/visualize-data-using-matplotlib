# --------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

electors_2009 = pd.read_csv(path)
candidate_2009 = pd.read_csv(path1)

# Plot a bar chart to compare the number of male and female candidates in the election
candidate_2009['Candidate_Sex'].value_counts().plot(kind='bar')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Gender Comparision')
plt.xticks(rotation=45)
plt.show()



# Plot a histogram of the age of all the candidates as well as of the winner amongst them. Compare them and note an observation
#fig, ax_all = plt.subplots(1,2, figsize=(20,10),tight_layout=True)

#Plot a histogram of the age of all the candidates
#candidate_2009.hist(['Candidate_Age'],bins=4,ax=ax_all[1])
#ax_all[0].set_xlabel=("Age of Candidate")
#ax_all[0].set_ylabel=("Counts")
#ax_all[0].set_title=("All the Candidate")
#Plot a histogram of the winner amongst them
#candidate_2009[candidate_2009['Position']==1].hist(['Candidate_Age'],bins=4,ax=ax_all[1])
#ax_all[0].set_xlabel=("Age of Candidate")
#ax_all[0].set_ylabel=("Counts")
#ax_all[0].set_title=("Winner Candidate")
# Plot a bar graph to get the vote shares of different parties
#vote_share=candidate_2009.groupby(['Party_Abbreviation'])['Total_Votes_Polled'].sum()
#print(vote_share)
#plt_bar_chart=vote_share.sort_values(ascending=False)[:10].plot(kind="barv")

# Plot a barplot to compare the mean poll percentage of all the states
#Mean_Poll_Percentage=electors_2009.groupby(['STATE'])['POLL PERCENTAGE'].mean()
#Mean_Poll_Percentage=Mean_Poll_Percentage.sort_values(ascending=False).to_dict()
#print(Mean_Poll_Percentage)

#state=list(Mean_Poll_Percentage.keys())
#state_percentage=list(Mean_Poll_Percentage.values())
#State_DF=pd.DataFrame({})
# Plot a bar plot to compare the seats won by different parties in Uttar Pradesh

# Plot a stacked bar chart to compare the number of seats won by different `Alliances` in Gujarat,Madhya Pradesh and Maharashtra. 
#mask_1=(candidate_2009['Position']==1)
#mask_2=(candidate_2009)['State_name'].isin('Gujarat','Madhya Pradesh''Maharashtra')
#seats_req_states=candidate_2009[mask_1 & mask_2](['State_name','Alliance'])
#res=seats_req_states.groupby(['State_name','Alliance']).size().unstack()
#res.plot(kind="bar",stacked=True,figsize=(15,10))
# Plot a grouped bar chart to compare the number of winner candidates on the basis of their caste in the states of Andhra Pradesh, Kerala, Tamil Nadu and Karnataka

# Plot a horizontal bar graph of the Parliamentary constituency with total voters less than 100000
###plt.barh(val['PARLIAMENTARY CONSTITUENCY'],val['Total voters'])
#plt.xlabel("count")
#plt.ylabel("pc")
#plt.title("pc vs voters")
# Plot a pie chart with the top 10 parties with majority seats in the elections

# Plot a pie diagram for top 9 states with most number of seats


