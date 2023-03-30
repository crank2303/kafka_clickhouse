# Проектная работа 8 спринта
Kafka

Clickhouse

ETL from Kafka to CLickhouse

# Как развернуть проект

Склонируйте репозиторий
```
git clone git@github.com:crank2303/ugc_sprint_1.git
```

Перейдите в каталог с проектом
```
cd ugc_sprint_1
```

Перейдите в каталог ugc_api
```
cd ugc_api
```

Скопируйте файл настроек окружения проекта
```
cp .env.example .env
```

Вернитесь в корневую папку проекта
```
cd -
```

Запустите сборку контейнера
```
docker compose up -d --build
```
<br>
<hr>

# Документация сваггер

Доступна по адресу: <a href="http://localhost:8000/api/docs">http://localhost:8000/api/docs