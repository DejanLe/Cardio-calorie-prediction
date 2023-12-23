import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

column_names= ['user_id', 'item_id', 'rating', 'timestamp']
df = pd.read_csv('file.tsv', sep='\t', names=column_names)
movies_titles = pd.read_csv('Movie_Id_Titles.csv')

data = pd.merge(df, movies_titles, on='item_id')
data.groupby('title')['rating'].mean().sort_values(ascending=False).head()
#print(data.groupby('title')['rating'].mean().sort_values(ascending=False).head())
#print(data.groupby('title')['rating'].count().sort_values(ascending=False).head())
ratings = pd.DataFrame(data.groupby('title')['rating'].mean())
ratings['num of ratings'] = pd.DataFrame(data.groupby('title')['rating'].count())

#print(ratings.head())
#rating movie 
# plot graph of 'num of ratings column'
plt.figure(figsize =(10, 4))
  
ratings['num of ratings'].hist(bins = 70)
# plot graph of 'ratings' column
plt.figure(figsize =(10, 4))
  
ratings['rating'].hist(bins = 70)
moviemat = data.pivot_table(index ='user_id',
              columns ='title', values ='rating')
ratings.sort_values('num of ratings', ascending = False).head(10)

starwars_user_ratings = moviemat['Star Wars (1977)']
liarliar_user_ratings = moviemat['Liar Liar (1997)']
#print(starwars_user_ratings.head())
# analysing correlation with similar movies
similar_to_starwars = moviemat.corrwith(starwars_user_ratings)
similar_to_liarliar = moviemat.corrwith(liarliar_user_ratings)

corr_starwars = pd.DataFrame(similar_to_starwars, columns =['Correlation'])
corr_starwars.dropna(inplace = True)

corr_starwars.head()

# Similar movies like starwars
corr_starwars.sort_values('Correlation', ascending = False).head(10)
corr_starwars = corr_starwars.join(ratings['num of ratings'])

corr_starwars.head()

corr_starwars[corr_starwars['num of ratings']>100].sort_values('Correlation', ascending = False).head()

# Similar movies as of liarliar
corr_liarliar = pd.DataFrame(similar_to_liarliar, columns =['Correlation'])
corr_liarliar.dropna(inplace = True)

corr_liarliar = corr_liarliar.join(ratings['num of ratings'])
corr_liarliar[corr_liarliar['num of ratings']>100].sort_values('Correlation', ascending = False).head()












