
import sys
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")

# Requires 1 param - path to root directory
dir = sys.argv[1]

# Load in the dataframe
df = pd.read_csv(dir + "/wine/winemag-data-130k-v2.csv", index_col=0)

# Looking at first 5 rows of the dataset
print(df.head())

# Show some summary info
print("There are {} observations and {} features in this dataset. \n".format(df.shape[0],df.shape[1]))
print("There are {} types of wine in this dataset such as {}... \n".format(len(df.variety.unique()),
                                                                           ", ".join(df.variety.unique()[0:5])))
print("There are {} countries producing wine in this dataset such as {}... \n".format(len(df.country.unique()),
                                                                                      ", ".join(df.country.unique()[0:5])))
print(df[["country", "description","points"]].head())

# Groupby by country
country = df.groupby("country")

# Summary statistic of all countries
print(country.describe().head())

# Start with one review:
text = df.description[0]

# Create and generate a word cloud image:
wordcloud = WordCloud().generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

wordcloud.to_file("Experiment26.png")

# If this gives a "Only supported for TrueType fonts" error, do this:
# pip3 install --upgrade pip
# pip3 install --upgrade Pillow

