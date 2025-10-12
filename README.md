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

## UML-диаграмма классов
```mermaid
flowchart TD
  A[FastAPI app] --> B[API Endpoints]
  B -->|POST /task/train_and_prediction| TP[task_processing result predict]
  B -->|POST /task/prediction| TP
  B -->|GET /task/train| TP
  B -->|DELETE /task/delete| TP

  TP -->|DELETE| DEL[delete_task_processing]
  DEL --> AGDEL[agent delete table data_classif and data_claster]
  AGDEL --> R1[return data deleted]

  TP -->|LEARN or PREDICT| DB[DatabaseConnector connect]
  DB --> CHK[check_table_exists and create_model_table]

  %% LEARN
  CHK -->|LEARN| GETL[get_data_table learn]
  GETL --> DLC[data_learn_claster_classif_distribution]

  subgraph Learn
    direction LR
    DLC --> F1[data_formater clusterization]
    F1 --> CL[data_clusterization]
    CL --> ANA1[method_selector_by_analysis rules]
    ANA1 --> OPT1[optimize_hyperparameters_claster]
    OPT1 --> CM[clusterization_methods labels model]
    CM --> F2[data_formater classification]
    F2 --> CLSF[data_classification]
    CLSF --> ANA2[method_selector_by_analysis rules]
    ANA2 --> OPT2[optimize_hyperparameters_classif]
    OPT2 --> SKC[classification_methods y_pred model]
    SKC --> SAVE1[insert_data data_claster]
    SKC --> SAVE2[insert_data data_classif]
    SAVE2 --> OUT1[processing_result_by_task LEARN]
  end

  %% PREDICT
  CHK -->|PREDICT| GETP[get_data_table predict]
  GETP --> CHKM[check_exists_in_table data_classif]
  CHKM -->|нет| ERR[return false]
  CHKM -->|да| DPP[data_predict_claster_classif_distribution]

  subgraph Predict
    direction LR
    DPP --> LOADC[load best cluster model]
    LOADC --> F3[data_formater clusterization]
    F3 --> APPLYC[clusterization_methods predict cluster labels]
    APPLYC --> LOADM[load best classification model]
    LOADM --> F4[data_formater classification]
    F4 --> APPLYM[classification_methods predict class labels]
    APPLYM --> CJ1[concatenate front time column]
    CJ1 --> CJ2[concatenate front id column]
    CJ2 --> OUT2[processing_result_by_task PREDICT]
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