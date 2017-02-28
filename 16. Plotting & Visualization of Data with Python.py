import pandas as pd
import matplotlib.pyplot as plt

# Plotting the data using bank-additional dataset
Bank_Details = pd.read_table('Files/bank-additional.csv', sep=';')
# print(Bank_Details)

# Plot the average campaign days by age
CampaignByAge = Bank_Details.groupby('age').campaign.mean().plot()

# Adding a title
CampaignByAge.set_title('Campaign days by age')
# X-Axis title
CampaignByAge.set_xlabel('age')
# Y-Axis title
CampaignByAge.set_ylabel('campaign')
# Add Legend
CampaignByAge.legend(['Avg campaign days'])

plt.show(CampaignByAge)



# Plot the average campaign days by maritial status / bar graph
CampaignByAge = Bank_Details.groupby('marital').campaign.mean().plot(kind='bar')

# Adding a title
CampaignByAge.set_title('Campaign days by Maritial status')
# X-Axis title
CampaignByAge.set_xlabel('Marital status')
# Y-Axis title
CampaignByAge.set_ylabel('campaign')
# Add Legend
CampaignByAge.legend(['Avg campaign days'])

plt.show(CampaignByAge)



# Plot the average campaign days by job status / horizontal bar graph
CampaignByAge = Bank_Details.groupby('job').campaign.mean().plot(kind='barh', color='red')

# Adding a title
CampaignByAge.set_title('Campaign days by Job status')
# X-Axis title
CampaignByAge.set_xlabel('campaign')
# Y-Axis title
CampaignByAge.set_ylabel('Job status')
# Add Legend
CampaignByAge.legend(['Avg campaign days'])

plt.show(CampaignByAge)



# Plot the average campaign days by  age /  histogram
CampaignByAge = Bank_Details.groupby('age').campaign.mean().plot(kind='hist')

# Adding a title
CampaignByAge.set_title('Campaign days by age')
# X-Axis title
CampaignByAge.set_xlabel('age')
# Y-Axis title
CampaignByAge.set_ylabel('campaign')
# Add Legend
CampaignByAge.legend(['Avg campaign days'])

plt.show(CampaignByAge)



# Plot the average campaign days by job status / Pie graph
CampaignByAge = Bank_Details.groupby('job').campaign.mean().plot(kind='pie')

# Adding a title
CampaignByAge.set_title('Campaign days by Job status')
# Adding legend
CampaignByAge.legend(['Avg campaign days'])

plt.show(CampaignByAge)
