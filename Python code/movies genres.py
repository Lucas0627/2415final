# Genres
from sklearn.preprocessing import MultiLabelBinarizer

import matplotlib.colors

# Custom colour map based on Netflix palette
cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", ['#221f1f', '#b20710', '#f5f5f1'])


def genre_heatmap(df, title):
    df['genre'] = df['listed_in'].apply(lambda x: x.replace(' ,', ',').replace(', ', ',').split(','))
    Types = []
    for i in df['genre']: Types += i
    Types = set(Types)
    print("There are {} types in the Netflix {} Dataset".format(len(Types), title))
    test = df['genre']
    mlb = MultiLabelBinarizer()
    res = pd.DataFrame(mlb.fit_transform(test), columns=mlb.classes_, index=test.index)
    corr = res.corr()
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True
    fig, ax = plt.subplots(figsize=(10, 7))
    fig.text(.54, .88, 'Genre correlation', fontfamily='serif', fontweight='bold', fontsize=15)
    fig.text(.75, .665,
             '''
              It is interesting that Independant Movies
              tend to be Dramas. 
 
              Another observation is that 
              Internatinal Movies are rarely
              in the Children's genre.
              ''', fontfamily='serif', fontsize=12, ha='right')
    pl = sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, vmin=-.3, center=0, square=True, linewidths=2.5)

    plt.show()

    df_tv = df[df["type"] == "TV Show"]
    df_movies = df[df["type"] == "Movie"]

    genre_heatmap(df_movies, 'Movie')
    plt.show()