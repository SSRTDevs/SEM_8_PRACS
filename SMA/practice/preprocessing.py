import pandas as pd
import nltk

df = pd.read_csv("tweets.csv", nrows=100)
col = "content"

# Remove links
links_regex = "https?://\S+"
df[col] = df[col].str.replace(links_regex, ' ', regex = True)

# remove numbers
df[col] = df[col].str.replace('\d+','',regex = True)

#remove special characters 
special_character_regex = "[^A-Za-z\s]+"
df[col] = df[col].str.replace(special_character_regex,'',regex = True)

#remove extra white spaces 
df[col] = df[col].str.replace('\s+',' ',regex = True)




nltk.download('punkt')
from nltk.tokenize import word_tokenize
df[col] = df[col].astype(str)
df[col] = df[col].apply(word_tokenize)

nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
df[col] = df[col].apply(lambda x : ' '.join([word for word in x.split() if word.lower() not in stop_words]))

nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
lemmatizer = WordNetLemmatizer()
df[col] = df[col].apply(lambda x : ' '.join([lemmatizer.lemmatize(word) for word in word_tokenize(x)]))


# Typecasting df[col] = df[col].astype(str)











# print(df[col].head(10))



