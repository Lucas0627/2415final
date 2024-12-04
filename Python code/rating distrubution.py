order = pd.DataFrame(df.groupby('rating')['count'].sum().sort_values(ascending=False).reset_index())
rating_order = list(order['rating'])

mf = df.groupby('type')['rating'].value_counts().unstack().sort_index().fillna(0).astype(int)[rating_order]

movie = mf.loc['Movie']
tv = - mf.loc['TV Show']

fig, ax = plt.subplots(1, 1, figsize=(12, 6))
ax.bar(movie.index, movie, width=0.5, color='#b20710', alpha=0.8, label='Movie')
ax.bar(tv.index, tv, width=0.5, color='#221f1f', alpha=0.8, label='TV Show')
# ax.set_ylim(-35, 50)

# Annotations
for i in tv.index:
    ax.annotate(f"{-tv[i]}",
                xy=(i, tv[i] - 60),
                va='center', ha='center', fontweight='light', fontfamily='serif',
                color='#4a4a4a')

for i in movie.index:
    ax.annotate(f"{movie[i]}",
                xy=(i, movie[i] + 60),
                va='center', ha='center', fontweight='light', fontfamily='serif',
                color='#4a4a4a')

for s in ['top', 'left', 'right', 'bottom']:
    ax.spines[s].set_visible(False)

ax.set_xticklabels(mf.columns, fontfamily='serif')
ax.set_yticks([])

ax.legend().set_visible(False)
fig.text(0.16, 1, 'Rating distribution by Film & TV Show', fontsize=15, fontweight='bold', fontfamily='serif')
fig.text(0.16, 0.89,
         '''We observe that some ratings are only applicable to Movies. 
         The most common for both Movies & TV Shows are TV-MA and TV-14.
         '''

         , fontsize=12, fontweight='light', fontfamily='serif')

fig.text(0.755, 0.924, "Movie", fontweight="bold", fontfamily='serif', fontsize=15, color='#b20710')
fig.text(0.815, 0.924, "|", fontweight="bold", fontfamily='serif', fontsize=15, color='black')
fig.text(0.825, 0.924, "TV Show", fontweight="bold", fontfamily='serif', fontsize=15, color='#221f1f')

plt.show()