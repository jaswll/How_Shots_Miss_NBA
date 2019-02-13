
import matplotlib.pyplot as plt, numpy as np

def plot_dbscan(dbscan, X, features=[0, 3]):

    core_samples  =  dbscan.core_sample_indices_
    labels        =  dbscan.labels_

    core_samples_mask = np.zeros_like(labels, dtype=bool)
    core_samples_mask[core_samples] = True

    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

    # Black removed and is used for noise instead.
    unique_labels = set(labels)
    colors = [plt.cm.Spectral(each)
              for each in np.linspace(0, 1, len(unique_labels))]
    for k, col in zip(unique_labels, colors):
        if k == -1:
            # Black used for noise.
            col = [0, 0, 0, 1]

        class_member_mask = (labels == k)

        xy = X[class_member_mask & core_samples_mask]
        plt.plot(xy[:, features[0]], xy[:, features[1]], '.', markersize=4)

        xy = X[class_member_mask & ~core_samples_mask]
        plt.plot(xy[:, features[0]], xy[:, features[1]], '.', markersize=2)

    plt.title('Estimated number of clusters: %d' % n_clusters_)
    plt.show()
