data = df_tv.groupby('first_country')[['first_country', 'count']].sum().sort_values(by='count',
                                                                                    ascending=False).reset_index()[:10]
data = data['first_country']
df_loli = df_tv.loc[df_tv['first_country'].isin(data)]

loli = df_loli.groupby('first_country')['release_year', 'year_added'].mean().round()

# Reorder it following the values of the first value:
ordered_df = loli.sort_values(by='release_year')

ordered_df_rev = loli.sort_values(by='release_year', ascending=False)

my_range = range(1, len(loli.index) + 1)

fig, ax = plt.subplots(1, 1, figsize=(7, 5))

fig.text(0.13, 0.9, 'How old are the TV shows? [Average]', fontsize=15, fontweight='bold', fontfamily='serif')
plt.hlines(y=my_range, xmin=ordered_df['release_year'], xmax=ordered_df['year_added'], color='grey', alpha=0.4)
plt.scatter(ordered_df['release_year'], my_range, color='#221f1f', s=100, alpha=0.9, label='Average release date')
plt.scatter(ordered_df['year_added'], my_range, color='#b20710', s=100, alpha=0.9, label='Average added date')
# plt.legend()

for s in ['top', 'left', 'right', 'bottom']:
    ax.spines[s].set_visible(False)

ax.yaxis.tick_right()
plt.yticks(my_range, ordered_df.index)
plt.yticks(fontname="serif", fontsize=12)

fig.text(0.19, 0.175, "Released", fontweight="bold", fontfamily='serif', fontsize=12, color='#221f1f')

fig.text(0.47, 0.175, "Added", fontweight="bold", fontfamily='serif', fontsize=12, color='#b20710')

fig.text(0.13, 0.42,
         '''The gap for TV shows seems
         more regular than for movies.
         
         This is likely due to subsequent
         series being released
         year-on-year.
         
         Spain seems to have
         the newest content
         overall.
         '''

         , fontsize=12, fontweight='light', fontfamily='serif')

ax.tick_params(axis=u'both', which=u'both', length=0)
# plt.xlabel('Value of the variables')
# plt.ylabel('Group')
plt.show()