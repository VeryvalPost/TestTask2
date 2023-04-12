#	Python, Docker проект
___

### Создать git проект, в котором должно быть 2 docker контейнера: 
+	скрипт python;
+	БД (postgreSQL).

Алгоритм взаимодействия.

Скрипт каждую минуту отправляет данные в БД cо сгенерированными данными.

### Пример данных:

+	*"id"*: id записи (инкремент);
+	*"data"*: сгенерированная строка данных;
+	*"date"*: текущая дата и время.

Скрипт логирует свои действия.

При достижении в таблице БД 30 строк, таблица должна очищаться и вновь пришедшие данные должны быть записаны 1й строчкой.(Реализовано на уровне скрипта)

Проект разворачивается с помощью docker compose.
