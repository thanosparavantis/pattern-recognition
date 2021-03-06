# Pattern Recognition 2018-2019  #
#================================#
# p16036 - Ioannidis Panagiotis  #
# p16112 - Paravantis Athanasios #
#================================#

from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import pandas as pd
from movielens_data import MovieLensData

# Access data
dataObj = MovieLensData()

# Load normalized data
data = dataObj.get_normalized_data()

hierarchical = linkage(data, method = 'median', metric = 'euclidean')

# Create plot
plt.figure(figsize = (19, 9))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('sample index')
plt.ylabel('distance')
dendrogram(
    hierarchical,
    leaf_rotation = 90,
    leaf_font_size = 10,
    truncate_mode = 'lastp',
    p = 100
)

plt.show()
