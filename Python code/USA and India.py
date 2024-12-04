fig, ax = plt.subplots(1, 1, figsize=(14, 6))
color = ['#b20710', '#221f1f'][::-1]
hs_list = data_sub.columns
hs_built = data_sub[hs]

for i, hs in enumerate(hs_list):
    if i == 0: continue
    ax.fill_between(hs_built.index, data_sub.iloc[:, i - 1], data_sub.iloc[:, i], color=color[i - 1])

for s in ['top', 'right', 'bottom', 'left']:
    ax.spines[s].set_visible(False)
ax.set_axisbelow(True)
ax.set_yticks([])
# ax.legend(loc='upper left')
ax.grid(False)

fig.text(0.16, 0.76, 'USA vs. India: Stream graph of new content added', fontsize=15, fontweight='bold',
         fontfamily='serif')
fig.text(0.16, 0.575,
         '''
         Seeing the data displayed like this helps 
         us to realise just how much content is added in the USA.
         Remember, India has the second largest amount of
         content yet is dwarfed by the USA.'''

         , fontsize=12, fontweight='light', fontfamily='serif')

fig.text(0.16, 0.41, "India", fontweight="bold", fontfamily='serif', fontsize=15, color='#b20710')
fig.text(0.208, 0.41, "|", fontweight="bold", fontfamily='serif', fontsize=15, color='black')
fig.text(0.218, 0.41, "USA", fontweight="bold", fontfamily='serif', fontsize=15, color='#221f1f')

ax.tick_params(axis=u'y', which=u'both', length=0)

plt.show()