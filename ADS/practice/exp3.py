import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../travel-times.csv")

DayOfWeek_counts = df["DayOfWeek"].value_counts()
plt.pie(DayOfWeek_counts.values, labels=DayOfWeek_counts.index, autopct='%1.1f%%')
plt.title("Day of Week - Pie chart")
plt.show()

df['TotalTime'].plot.density(color='green')
plt.title('Density of Total Time')
plt.show()

df = df.head(20)
plt.plot(df['Date'], df['MovingTime'], label='Moving Time')
plt.xlabel('Date')
plt.ylabel('MovingTime')
plt.legend()
plt.show()

df["AvgSpeed"].hist()

sns.histplot(df["AvgSpeed"], kde=True, color="m")
plt.show()

sns.pairplot(df)
plt.show()