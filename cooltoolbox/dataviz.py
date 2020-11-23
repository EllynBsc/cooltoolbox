import seaborn as sns
import matplotlib.pyplot as plt

def showme(df):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 6))
    sns.boxplot(df, ax=ax1)
    sns.distplot(df, ax=ax2)



