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
flowchart TD
  sequenceDiagram
  autonumber
  participant Client
  participant API as FastAPI
  participant TP as task_processing
  participant Agent as DB_Agent
  participant Prep as DataPrep(two_methods)
  participant Clust as Clusterization(methods)
  participant Classif as Classification(methods)

  rect rgb(240,240,240)
  Note over Client,API: DELETE
  Client->>API: DELETE /task/delete
  API->>TP: delete_task_processing task=DELETE
  TP->>Agent: delete_table_agent tables=[data_classif,data_claster]
  Agent-->>TP: result=ok
  TP-->>Client: processing_result_by_task status=ok message="data deleted"
  end

  rect rgb(240,240,255)
  Note over Client,API: LEARN
  Client->>API: GET /task/train
  API->>TP: task_processing task=LEARN
  TP->>Agent: connect db_uri creds
  Agent-->>TP: conn
  TP->>Agent: check_table_exists names=[data_classif,data_claster]
  Agent-->>TP: exists=bool
  TP->>Agent: create_model_table names=[missing only]
  TP->>Agent: get_data_table name=name_table_for_learn
  Agent-->>TP: df_raw
  TP->>Prep: data_learn_claster_classif_distribution df_raw id_col time_col
  Prep-->>TP: df_learn
  TP->>Prep: data_formater_clusterization df_learn features
  Prep-->>TP: X_cluster
  TP->>Clust: data_clusterization X_cluster params/search
  Clust-->>TP: labels cluster_model acc_cluster
  TP->>Prep: data_formater_classification df_learn+labels target/features
  Prep-->>TP: X_clf y_clf
  TP->>Classif: data_classification X_clf y_clf params/search
  Classif-->>TP: y_pred clf_model acc_clf
  TP->>Agent: insert_data table=data_claster model=cluster_model accuracy=acc_cluster
  Agent-->>TP: ok
  TP->>Agent: insert_data table=data_classif model=clf_model accuracy=acc_clf
  Agent-->>TP: ok
  TP-->>Client: processing_result_by_task data="model trained"
  end

  rect rgb(240,255,240)
  Note over Client,API: PREDICT
  Client->>API: POST /task/prediction
  API->>TP: task_processing task=PREDICT payload
  TP->>Agent: connect
  Agent-->>TP: conn
  TP->>Agent: get_data_table name=predict_table
  Agent-->>TP: df_predict_raw
  TP->>Agent: check_exists_in_table table=data_classif equipment
  Agent-->>TP: exists?
  alt model not found
    TP-->>Client: error message="no trained model"
  else model found
    TP->>Agent: get_data_table_in_coloumn table=data_claster column=machine
    Agent-->>TP: cluster_model(best_accuracy)
    TP->>Prep: data_predict_claster_classif_distribution df_predict_raw id_col time_col
    Prep-->>TP: df_predict
    TP->>Prep: data_formater_clusterization df_predict features
    Prep-->>TP: Xp_cluster
    TP->>Clust: predict model=cluster_model X=Xp_cluster
    Clust-->>TP: cluster_labels
    TP->>Agent: get_data_table_in_coloumn table=data_classif column=machine
    Agent-->>TP: clf_model(best_accuracy)
    TP->>Prep: data_formater_classification df_predict+cluster_labels features
    Prep-->>TP: Xp_clf
    TP->>Classif: predict model=clf_model X=Xp_clf
    Classif-->>TP: class_labels
    TP-->>Client: processing_result_by_task equipment data=[time,id,cluster_labels,class_labels,...]
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