# Data

df_movies
df_tv

### Relevant groupings

data = df_movies.groupby('first_country')[['first_country', 'count']].sum().sort_values(by='count',
                                                                                        ascending=False).reset_index()[
       :10]
data = data['first_country']
df_loli = df_movies.loc[df_movies['first_country'].isin(data)]

loli = df_loli.groupby('first_country')['release_year', 'year_added'].mean().round()

# Reorder it following the values of the first value
ordered_df = loli.sort_values(by='release_year')

ordered_df_rev = loli.sort_values(by='release_year', ascending=False)

my_range = range(1, len(loli.index) + 1)

fig, ax = plt.subplots(1, 1, figsize=(7, 5))

fig.text(0.13, 0.9, 'How old are the movies? [Average]', fontsize=15, fontweight='bold', fontfamily='serif')
plt.hlines(y=my_range, xmin=ordered_df['release_year'], xmax=ordered_df['year_added'], color='grey', alpha=0.4)
plt.scatter(ordered_df['release_year'], my_range, color='#221f1f', s=100, alpha=0.9, label='Average release date')
plt.scatter(ordered_df['year_added'], my_range, color='#b20710', s=100, alpha=0.9, label='Average added date')
# plt.legend()

for s in ['top', 'left', 'right', 'bottom']:
    ax.spines[s].set_visible(False)

# Removes the tick marks but keeps the labels
ax.tick_params(axis=u'both', which=u'both', length=0)
# Move Y axis to the right side
ax.yaxis.tick_right()

plt.yticks(my_range, ordered_df.index)
plt.yticks(fontname="serif", fontsize=12)

# Custome legend
fig.text(0.19, 0.175, "Released", fontweight="bold", fontfamily='serif', fontsize=12, color='#221f1f')
fig.text(0.76, 0.175, "Added", fontweight="bold", fontfamily='serif', fontsize=12, color='#b20710')

fig.text(0.13, 0.46,
         '''The average gap between when 
         content is released, and when it
         is then added on Netflix varies
         by country. 
         
         In Spain, Netflix appears to be 
         dominated by newer movies 
         whereas Egypt & India have
         an older average movie.
         '''

         , fontsize=12, fontweight='light', fontfamily='serif')

# plt.xlabel('Year')
# plt.ylabel('Country')
plt.show()