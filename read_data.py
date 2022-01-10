# data analysis using seabourn
# author glen gardiner
# data set https://data.world/health/health-data-breaches/workspace/file?filename=breach_report.csv

# download link https://query.data.world/s/s342dw6qe7ox2gxxun3ngab4o4tuf6



import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

breaches = pd.read_csv('./breach_report.csv')


def catplot_bf():
    # types of breach and frequency barplot
    res = sns.catplot(x="Type of Breach",kind="count", data=breaches)
    plt.show()

def catplot_si():
    res = sns.catplot(x="State", y="Individuals Affected", data=breaches)
    plt.show()

def catplot_six():
    
    res = sns.catplot( data=breaches, kind="bar", x="Individuals Affected", y="Type of Breach", hue="Business Associate Present",
                      ci="sd", palette="dark", alpha=.6, height=6)
    res.despine(left=True)
    res.set_axis_labels("", "Type of Breach")
    res.legend.set_title("")
    plt.show()

def swarm_slb():
    res = sns.swarmplot(x="State", y="Location of Breached Information",hue="Covered Entity Type", data=breaches)
    plt.show()

def swarm_ti():
    #unpacking 
    res = sns.swarmplot(x=breaches["Type of Breach"], y=breaches["Individuals Affected"])
    plt.show()

def barplot_si():
    #
    res = sns.barplot(x="State", y="Individuals Affected", hue="Type of Breach", data=breaches)
    plt.show()

def relplot_tb():
    res = sns.relplot( x="Type of Breach", y="", col="Business Associate Present", hue="Type of Breach", data=breaches)
    res.set(xticks=[])
    plt.show()

def striplot_bi():
    sns.stripplot(x="Business Associate Present", y="Individuals Affected", hue="Type of Breach", data=breaches)
    plt.show()



def main():
    catplot_bf()
    # catplot_si()
    # atplot_six()
    # swarm_slb()
    # swarm_ti()
    # barplot_si()
    # relplot_tb()
    # striplot_bi()
   
            

if __name__ == '__main__':
    main()