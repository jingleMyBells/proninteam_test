# Тестовое задание proninteam

## Запуск

###### Для запуска необходимы docker и docker-compose
###### [Инструкции по установке докера](https://docs.docker.com/engine/install/)

#### Шаги:

Склонировать репозиторий
```bash
git clone git@github.com:jingleMyBells/proninteam_test.git
```

Перейти в каталог с проектом
```bash
cd proninteam_test
```

Создать файл с переменными окружения по образу и подобию env-example.txt
```bash
  cat env-example.txt > .env
```

Запустить проект 
```bash
  docker-compose up
```

API будет отвечать по адресу http://localhost:8000
```http
  GET /api/consumers/
```
```http
  POST /api/deals/
```

###### Заметки:

`Формулировка в ТЗ "2.Ранее загруженные версии файла deals.csv  
не должны влиять на результат обработки новых."  
неясна. Сделал так, что пользователи и итемы - уникальны, а сделки - нет.  
Можно наверное зауникалить сделку (например по времени), но недостаточно вводных  
а без них у сделок нет ни одного по-настоящему подходящего параметра.  
Уповаю на пользователя, который не будет загружать дубликаты файлов.`

`Формулировку в ТЗ "5.Проект не использует глобальных зависимостей  
за исключением:  python, docker, docker-compose;" трактую как отсутствие других контейнеров.`