# Лабораторная 1 по дисциплине "Технологии программирования"

---

## Цель работы
1. Освоить основы работы с системой контроля версий **Git**.  
2. Научиться использовать **GitHub** для хранения проектов.  
3. Освоить механизм автоматического тестирования и проверки стиля кода через **GitHub Actions (CI/CD)**.  
4. Реализовать задание с использованием языка **Python** и модульного тестирования (**pytest**).  

---

## Постановка задачи
Проект: система классификации на основе кластеризации данных мониторинга оборудования.
Выполняется передача параметров и доступ к данным на основе API.

---

## Структура проекта
```
assistant/
 ├── .github/workflows/github-actions-testing.yml   # CI/CD
 ├── main_scripts/
 │    ├── rules/
 │    │    ├── classification_rules.json
 │    │    └── clusterization_rules.json
 │    └── main.py
 ├── src/
 │    ├── rules/
 │    │    ├── classification_methods.py
 │    │    ├── clusterization_methods.py
 │    │    ├── connector.py
 │    │    └── two_methods_included.py
 ├── test/
 │    ├── test_API.py
 │    └── test_database.py
 ├── requirements.txt
 ├── .gitignore
 └── README.md
```

---

## Используемые технологии
1. Язык программирования: **Python 3.10+**  
2. Управление зависимостями: **requirements.txt**  
3. Модульное тестирование: **pytest**   
4. CI/CD: **GitHub Actions**  
5. Проверка стиля кода: **pycodestyle (PEP8)**

---

## Инструкция по запуску

### Установка зависимостей
```bash
pip install -r requirements.txt
```

### Запуск тестов
```bash
pytest test
```

### Проверка стиля кода (PEP8)
```bash
pycodestyle src tests main_scripts
```

### Запуск программы
```bash
python main_scripts/main.py
```

---

## UML-диаграмма функций
```mermaid
  sequenceDiagram
    participant Client
    participant API as FastAPI
    participant TP as task_processing
    participant Agent as DB_Agent
    participant Prep as DataPrep_two_methods
    participant Clust as Clusterization_methods
    participant Classif as Classification_methods

    %% DELETE
    Note over Client,API: DELETE
    Client->>API: DELETE /task/delete
    API->>TP: delete_task_processing
    TP->>Agent: delete_table_agent [data_classif, data_claster]
    Agent-->>TP: ok
    TP-->>Client: processing_result_by_task (status=ok, message="data deleted")

    %% LEARN
    Note over Client,API: LEARN
    Client->>API: GET /task/train
    API->>TP: task_processing (task=LEARN)
    TP->>Agent: connect (db_uri, creds)
    Agent-->>TP: connection
    TP->>Agent: check_table_exists
    Agent-->>TP: exists
    TP->>Agent: create_model_table (if missing)
    TP->>Agent: get_data_table (learn)
    Agent-->>TP: df_raw
    TP->>Prep: data_learn_claster_classif_distribution (df_raw)
    Prep-->>TP: df_learn
    TP->>Prep: data_formater_clusterization (df_learn)
    Prep-->>TP: X_cluster
    TP->>Clust: data_clusterization (X_cluster)
    Clust-->>TP: labels, cluster_model, acc_cluster
    TP->>Prep: data_formater_classification (df_learn + labels)
    Prep-->>TP: X_clf, y_clf
    TP->>Classif: data_classification (X_clf, y_clf)
    Classif-->>TP: y_pred, clf_model, acc_clf
    TP->>Agent: insert_data (data_claster, cluster_model, acc_cluster)
    Agent-->>TP: ok
    TP->>Agent: insert_data (data_classif, clf_model, acc_clf)
    Agent-->>TP: ok
    TP-->>Client: processing_result_by_task (data="model trained")

    %% PREDICT
    Note over Client,API: PREDICT
    Client->>API: POST /task/prediction
    API->>TP: task_processing (task=PREDICT)
    TP->>Agent: connect
    Agent-->>TP: connection
    TP->>Agent: get_data_table (predict)
    Agent-->>TP: df_predict_raw
    TP->>Agent: check_exists_in_table (data_classif)
    Agent-->>TP: exists?

    alt model not found
        TP-->>Client: error ("no trained model")
    else model found
        TP->>Agent: get_data_table_in_coloumn (data_claster)
        Agent-->>TP: cluster_model_best
        TP->>Prep: data_predict_claster_classif_distribution (df_predict_raw)
        Prep-->>TP: df_predict
        TP->>Prep: data_formater_clusterization (df_predict)
        Prep-->>TP: Xp_cluster
        TP->>Clust: predict (cluster_model_best, Xp_cluster)
        Clust-->>TP: cluster_labels
        TP->>Agent: get_data_table_in_coloumn (data_classif)
        Agent-->>TP: clf_model_best
        TP->>Prep: data_formater_classification (df_predict + cluster_labels)
        Prep-->>TP: Xp_clf
        TP->>Classif: predict (clf_model_best, Xp_clf)
        Classif-->>TP: class_labels
        TP-->>Client: processing_result_by_task (equipment, data=[time,id,cluster_labels,class_labels])
    end
```

---

## Выводы
В ходе выполнения лабораторной работы были освоены:  
1. Базовые команды **Git** и принципы работы с репозиторием на GitHub.  
2. Настройка CI/CD через **GitHub Actions**.
3. Применение **pytest** для тестирования.
4. Контроль качества кода с помощью **pycodestyle**.

Проект успешно протестирован и соответствует требованиям.  