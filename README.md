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

## Диаграмма функций
```mermaid
flowchart TD
  A[FastAPI_app] -->|POST /task/train_and_prediction| TP[task_processing]
  A -->|POST /task/prediction| TP
  A -->|GET /task/train| TP
  A -->|DELETE /task/delete| TP

  %% DELETE
  TP -->|DELETE| DEL[delete_task_processing]
  DEL --> AGDEL[delete_table_agent]
  AGDEL --> RESDEL[processing_result_by_task]

  %% LEARN
  TP -->|LEARN| CONN[connect]
  CONN --> CHK[check_table_exists]
  CHK --> CREATE[create_model_table]
  CREATE --> GETL[get_data_table]
  GETL --> DIST1[data_learn_claster_classif_distribution]
  DIST1 --> FORM1[data_formater_clusterization]
  FORM1 --> CL[data_clusterization]
  CL --> FORM2[data_formater_classification]
  FORM2 --> CLASS[data_classification]
  CLASS --> INSERT1[insert_data]
  INSERT1 --> RESL[processing_result_by_task]

  %% PREDICT
  TP -->|PREDICT| CONN2[connect]
  CONN2 --> GETP[get_data_table]
  GETP --> CHKEX[check_exists_in_table]
  CHKEX --> LOADM[get_data_table_in_coloumn]
  LOADM --> DIST2[data_predict_claster_classif_distribution]
  DIST2 --> FORM3[data_formater_clusterization]
  FORM3 --> CONCAT[concatenate_data_with_labels]
  CONCAT --> FORM4[data_formater_classification]
  FORM4 --> RESP[processing_result_by_task]
```

---

## Выводы
В ходе выполнения лабораторной работы были освоены:  
1. Базовые команды **Git** и принципы работы с репозиторием на GitHub.  
2. Настройка CI/CD через **GitHub Actions**.
3. Применение **pytest** для тестирования.
4. Контроль качества кода с помощью **pycodestyle**.

Проект успешно протестирован и соответствует требованиям.  