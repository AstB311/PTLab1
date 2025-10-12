import pickle
from typing import Any, Optional
import numpy as np

from sklearn.cluster import (
    AffinityPropagation,
    AgglomerativeClustering,
    DBSCAN,
    KMeans,
    SpectralClustering,
)


def data_kmean_cluster(
    data: np.ndarray,
    params: Optional[dict] = None,
    loaded_model: Optional[bytes] = None,
) -> Any:
    """Выполняет кластеризацию данных с использованием алгоритма K-средних (KMeans)."""
    if loaded_model is None and params is not None:
        model_cluster_kmeans = KMeans(
            n_clusters=params["n_clusters"],
            init=params["init"],
            max_iter=params["max_iter"],
            random_state=42,
        )
        labels = model_cluster_kmeans.fit_predict(data)
        return labels, model_cluster_kmeans
    loaded_model = pickle.loads(loaded_model)
    loaded_model_cluster_kmeans = loaded_model.fit_predict(data)
    return loaded_model_cluster_kmeans


def data_agglclust_cluster(
    data: np.ndarray,
    params: Optional[dict] = None,
    loaded_model: Optional[bytes] = None,
) -> Any:
    """Выполняет кластеризацию данных с использованием агломеративной кластеризации."""
    if loaded_model is None and params is not None:
        model_cluster_agg = AgglomerativeClustering(
            n_clusters=params["n_clusters"],
            linkage=params["linkage"],
        )
        labels = model_cluster_agg.fit_predict(data)
        return labels, model_cluster_agg
    loaded_model = pickle.loads(loaded_model)
    loaded_model_cluster_agg = loaded_model.fit_predict(data)
    return loaded_model_cluster_agg


def data_specclust_clust(
    data: np.ndarray,
    params: Optional[dict] = None,
    loaded_model: Optional[bytes] = None,
) -> Any:
    """Выполняет кластеризацию данных с использованием спектральной кластеризации."""
    if loaded_model is None and params is not None:
        model_cluster_spectral = SpectralClustering(
            n_clusters=params["n_clusters"],
            affinity=params["affinity"],
            gamma=params["gamma"],
            random_state=42,
        )
        labels = model_cluster_spectral.fit_predict(data)
        return labels, model_cluster_spectral
    loaded_model = pickle.loads(loaded_model)
    loaded_model_cluster_spectral = loaded_model.fit_predict(data)
    return loaded_model_cluster_spectral


def data_dbscan_cluster(
    data: np.ndarray,
    params: Optional[dict] = None,
    loaded_model: Optional[bytes] = None,
) -> Any:
    """Выполняет кластеризацию данных с использованием DBSCAN."""
    if loaded_model is None and params is not None:
        model_cluster_dbscan = DBSCAN(
            eps=params["eps"],
            min_samples=params["min_samples"],
        )
        labels = model_cluster_dbscan.fit_predict(data)
        return labels, model_cluster_dbscan
    loaded_model = pickle.loads(loaded_model)
    loaded_model_cluster_dbscan = loaded_model.fit_predict(data)
    return loaded_model_cluster_dbscan


def data_affprop_cluster(
    data: np.ndarray,
    params: Optional[dict] = None,
    loaded_model: Optional[bytes] = None,
) -> Any:
    """Выполняет кластеризацию данных с использованием Affinity Propagation."""
    if loaded_model is None and params is not None:
        model_cluster_affinity = AffinityPropagation(
            damping=params["damping"],
            preference=params["preference"],
            random_state=42,
        )
        labels = model_cluster_affinity.fit_predict(data)
        return labels, model_cluster_affinity
    loaded_model = pickle.loads(loaded_model)
    loaded_model_cluster_affinity = loaded_model.fit_predict(data)
    return loaded_model_cluster_affinity
