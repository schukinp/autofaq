# Описание логики тестов
- Подключаемся к боту по WebSocket;
- Отправляем HTTP запросы боту с ключевыми словами (привет, запусти сценарий, Пельмени, Блины);
- Слушаем ответы бота по WebSocket;
- Делаем assert ответов бота на каждый HTTP запрос

# Описание структуры файлов
- файл helper.py содержит метод отправки запроса боту и получения ответа от него
- файл pytest.ini содержит настройки output результатов теста
- файл requirements.txt содержит список необходимых зависимостей
- файл test_bot_responses.py содержит тестовый сценарий

# Предусловие

* [Python 3.6+](https://www.python.org/)
* Для Windows требуется установка [cUrl](https://curl.haxx.se/windows/) 

# Установка

Install dependencies `pip install -r requirements.txt`

# Запуск тестов

Linux / Mac пример
```
$ pytest test_bot_responses.py
```

[Видео успешного прохождения теста](http://cloud.movavi.com/show/mZs0rKEBR1WV5bAYfoFnJHQ7LPp8hSUM)


