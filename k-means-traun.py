
df_names = pd.read_csv('player_data.csv')
df_players = pd.read_csv('Players.csv')
df_seasons= pd.read_csv('Seasons_Stats.csv')

df_seasons[df_seasons['Year']>2016].sort_values(by=['PTS'],ascending=False)
print(df_seasons.head())
df_clustered = df_seasons[df_seasons['Year']>2016][['AST','BLK','TOV','PTS','ORB','DRB']]


df_clustered.count()



Error =[]
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i).fit(df_clustered)
    Error.append(kmeans.inertia_)
plt.plot(range(1, 11), Error)
plt.title('Elbow method')
plt.xlabel('No of clusters')
plt.ylabel('Error')
plt.show()

kmeans5 = KMeans(n_clusters = 5)
y_kmeans5 = kmeans5.fit_predict(df_clustered)
centers = kmeans5.cluster_centers_
plt.scatter(df_clustered.iloc[:, 1],df_clustered.iloc[:, 2],df_clustered.iloc[:, 3], c=y_kmeans5, cmap='rainbow')
