fig, ax = plt.subplots(1, 1, figsize=(12, 6))
color = ["#b20710", "#221f1f"]

for i, mtv in enumerate(df['type'].value_counts().index):
    mtv_rel = df[df['type'] == mtv]['year_added'].value_counts().sort_index()
    ax.plot(mtv_rel.index, mtv_rel, color=color[i], label=mtv)
    ax.fill_between(mtv_rel.index, 0, mtv_rel, color=color[i], alpha=0.9)

ax.yaxis.tick_right()

ax.axhline(y=0, color='black', linewidth=1.3, alpha=.7)

# ax.set_ylim(0, 50)
# ax.legend(loc='upper left')
for s in ['top', 'right', 'bottom', 'left']:
    ax.spines[s].set_visible(False)

ax.grid(False)

ax.set_xlim(2008, 2020)
plt.xticks(np.arange(2008, 2021, 1))

fig.text(0.13, 0.85, 'Movies & TV Shows added over time', fontsize=15, fontweight='bold', fontfamily='serif')
fig.text(0.13, 0.59,
         '''We see a slow start for Netflix over several years. 
         Things begin to pick up in 2015 and then there is a 
         rapid increase from 2016.
         
         It looks like content additions have slowed down in 2020, 
         likely due to the COVID-19 pandemic.
         '''

         , fontsize=12, fontweight='light', fontfamily='serif')

fig.text(0.13, 0.2, "Movie", fontweight="bold", fontfamily='serif', fontsize=15, color='#b20710')
fig.text(0.19, 0.2, "|", fontweight="bold", fontfamily='serif', fontsize=15, color='black')
fig.text(0.2, 0.2, "TV Show", fontweight="bold", fontfamily='serif', fontsize=15, color='#221f1f')

ax.tick_params(axis=u'both', which=u'both', length=0)

plt.show()