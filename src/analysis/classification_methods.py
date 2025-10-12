import pickle
from typing import Any, Optional
import numpy as np

from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier


def determine_linearity(
        X: np.ndarray,
        y: np.ndarray,
        threshold: float = 0.85
) -> str:
    """Определяет, являются ли данные линейно разделимыми.

    Используются логистическая регрессия и SVM с линейным ядром.

    Args:
        X: numpy.ndarray. Массив признаков.
        y: numpy.ndarray. Массив меток классов.
        threshold: float. Порог точности, выше которого
            данные считаются линейно разделимыми (по умолчанию 0.85).

    Returns:
        str. "Linearly separable" или "Linearly inseparable".
    """
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )

    # Логистическая регрессия
    log_reg = LogisticRegression()
    log_reg.fit(X_train, y_train)
    y_pred_log_reg = log_reg.predict(X_test)
    accuracy_log_reg = accuracy_score(y_test, y_pred_log_reg)

    # SVM с линейным ядром
    svm_linear = SVC(kernel='linear')
    svm_linear.fit(X_train, y_train)
    y_pred_svm = svm_linear.predict(X_test)
    accuracy_svm = accuracy_score(y_test, y_pred_svm)

    if accuracy_log_reg > threshold and accuracy_svm > threshold:
        return "Linearly separable"
    return "Linearly inseparable"


def data_naiveb_classif(
        loaded_model: Optional[Any] = None,
        data: Optional[Any] = None,
        X: Optional[Any] = None,
        y: Optional[Any] = None,
        best_params: Optional[Any] = None
) -> Any:
    """Классификация с использованием GaussianNB."""
    if loaded_model is None:
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        model_classif_naiveb = GaussianNB(**best_params)
        model_classif_naiveb.fit(X_train, y_train)
        y_pred = model_classif_naiveb.predict(X_test)
        return y_pred, model_classif_naiveb, y_test

    loaded_model = pickle.loads(loaded_model)
    return loaded_model.predict(data)


def data_knn_classif(
        loaded_model: Optional[Any] = None,
        data: Optional[Any] = None,
        X: Optional[Any] = None,
        y: Optional[Any] = None,
        best_params: Optional[Any] = None
) -> Any:
    """Классификация с использованием KNeighborsClassifier."""
    if loaded_model is None:
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        model_classif_knn = KNeighborsClassifier(**best_params)
        model_classif_knn.fit(X_train, y_train)
        y_pred = model_classif_knn.predict(X_test)
        return y_pred, model_classif_knn, y_test

    loaded_model = pickle.loads(loaded_model)
    return loaded_model.predict(data)


def data_svm_classif(
        loaded_model: Optional[Any] = None,
        data: Optional[Any] = None,
        X: Optional[Any] = None,
        y: Optional[Any] = None,
        best_params: Optional[Any] = None
) -> Any:
    """Классификация с использованием SVC."""
    if loaded_model is None:
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        model_classif_svm = SVC(**best_params)
        model_classif_svm.fit(X_train, y_train)
        y_pred = model_classif_svm.predict(X_test)
        return y_pred, model_classif_svm, y_test

    loaded_model = pickle.loads(loaded_model)
    return loaded_model.predict(data)


def data_logregress_classif(
        loaded_model: Optional[Any] = None,
        data: Optional[Any] = None,
        X: Optional[Any] = None,
        y: Optional[Any] = None,
        best_params: Optional[Any] = None
) -> Any:
    """Классификация с использованием LogisticRegression."""
    if loaded_model is None:
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        model_classif_loggr = LogisticRegression(**best_params)
        model_classif_loggr.fit(X_train, y_train)
        y_pred = model_classif_loggr.predict(X_test)
        return y_pred, model_classif_loggr, y_test

    loaded_model = pickle.loads(loaded_model)
    return loaded_model.predict(data)


def data_dectree_classif(
        loaded_model: Optional[Any] = None,
        data: Optional[Any] = None,
        X: Optional[Any] = None,
        y: Optional[Any] = None,
        best_params: Optional[Any] = None
) -> Any:
    """Классификация с использованием DecisionTreeClassifier."""
    if loaded_model is None:
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        model_classif_tree = DecisionTreeClassifier(**best_params)
        model_classif_tree.fit(X_train, y_train)
        y_pred = model_classif_tree.predict(X_test)
        return y_pred, model_classif_tree, y_test

    loaded_model = pickle.loads(loaded_model)
    return loaded_model.predict(data)


def data_randforest_classif(
        loaded_model: Optional[Any] = None,
        data: Optional[Any] = None,
        X: Optional[Any] = None,
        y: Optional[Any] = None,
        best_params: Optional[Any] = None
) -> Any:
    """Классификация с использованием RandomForestClassifier."""
    if loaded_model is None:
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        model_classif_forest = RandomForestClassifier(**best_params)
        model_classif_forest.fit(X_train, y_train)
        y_pred = model_classif_forest.predict(X_test)
        return y_pred, model_classif_forest, y_test

    loaded_model = pickle.loads(loaded_model)
    return loaded_model.predict(data)


def data_gradboost_classif(
        loaded_model: Optional[Any] = None,
        data: Optional[Any] = None,
        X: Optional[Any] = None,
        y: Optional[Any] = None,
        best_params: Optional[Any] = None
) -> Any:
    """Классификация с использованием GradientBoostingClassifier."""
    if loaded_model is None:
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        model_classif_grand = GradientBoostingClassifier(**best_params)
        model_classif_grand.fit(X_train, y_train)
        y_pred = model_classif_grand.predict(X_test)
        return y_pred, model_classif_grand, y_test

    loaded_model = pickle.loads(loaded_model)
    return loaded_model.predict(data)