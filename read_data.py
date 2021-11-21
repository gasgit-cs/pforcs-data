# data analysis using seabourn
# author glen gardiner
# data set https://data.world/health/health-data-breaches/workspace/file?filename=breach_report.csv



import pandas as pd


import seaborn as sns
import matplotlib.pyplot as plt



breaches = pd.read_csv('./breach_report.csv')


# res = sns.swarmplot(x="State", y="Location of Breached Information", data=breaches)
# plt.show()

res = sns.barplot(x="State", y="Individuals Affected", hue="Type of Breach", data=breaches)

plt.show()