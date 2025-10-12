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

### Запуск программы
```bash
python main_scripts/main.py
```

---

## UML-диаграмма классов
```mermaid
classDiagram
    class DatabaseConnector {
      +connect() asyncpg.Connection
      +check_table_exists(table_name: str, schema: str = "public") bool
      +check_exists_in_table(table_name: str, machine_name: str, schema: str = "public") bool
      +create_model_table(table_name: str, table_column_name: str, schema: str = "public") void
      +insert_data(table_name: str, data: Dict[str, Any], schema: str = "public") void
      +get_data_table(table_name: str, schema: str = "public") List[Dict[str, Any]]
      +get_data_table_in_coloumn(table_name: str, column_name: str, machine_name: str, schema: str = "public") List[Dict[str, Any]]
      +delete_table_agent(table_name: str, schema: str = "public") void
      +close() void
    }

    DatabaseConnector : -server
    DatabaseConnector : -port
    DatabaseConnector : -database
    DatabaseConnector : -user
    DatabaseConnector : -password
    DatabaseConnector : -equipment
    DatabaseConnector : -equipment_predict
    DatabaseConnector : -conn

```

---

## Выводы
В ходе выполнения лабораторной работы были освоены:  
1. Базовые команды **Git** и принципы работы с репозиторием на GitHub.  
2. Настройка CI/CD через **GitHub Actions**.
3. Применение **pytest** для тестирования.

Проект успешно протестирован и соответствует требованиям.  