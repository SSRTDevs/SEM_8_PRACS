import pandas as pd
import nltk
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("tweets.csv", nrows=200)
# col = "content"

# def get_sentiment_label(sentiment):
#     if sentiment > 0.0:
#         return 'positive'
#     elif sentiment < 0.0:
#         return 'negative'
#     else:
#         return 'neutral'

# # Apply the sentiment analysis and label function to the DataFrame's text column
# df['polarity'] = df['content'].apply(lambda x: TextBlob(x).sentiment.polarity)
# df['sentiment_label'] = df['polarity'].apply(get_sentiment_label)

# positive_count = df['sentiment_label'].value_counts()['positive']
# negative_count = df['sentiment_label'].value_counts()['negative']
# neutral_count = df['sentiment_label'].value_counts()['neutral']

# sns.countplot(x='sentiment_label', data = df)
# plt.show()

# sns.barplot(x='author',y='number_of_likes',data=df)
# plt.show()

# # Try to use hue for categorical columns
# sns.scatterplot(x='number_of_shares',y='number_of_likes',hue="author",data=df)
# plt.show()

# # Pie chart
# count = df['author'].value_counts()
# plt.pie(count, labels = count.index, data = df, autopct = '%1.1f%%')
# plt.show()

# from wordcloud import WordCloud
# wc = WordCloud(background_color = "white", height = 800, width = 800)
# text = "".join(df['content'])
# cloud = wc.generate(text)
# plt.imshow(cloud)
# plt.axis('off')
# plt.show()

# df['formatted_date'] = pd.to_datetime(df['date_time'])
# df['year'] = df['formatted_date'].dt.year
# group = df.groupby('year')['number_of_likes'].sum()

# plt.plot(group.index, group.values)
# plt.xlabel('year')
# plt.ylabel('No. of likes')
# plt.show()

country = df.groupby('language')['number_of_likes'].sum()
print(country)
sns.barplot(x=country.index,y=country.values,capsize=100)
plt.show()



