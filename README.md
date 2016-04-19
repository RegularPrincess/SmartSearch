# StackOverFlow Crawler.

<b>19.04.2016</b>

Появился скелет MVC и заглушенный функционал.

В Контроллере можно найти запуск основного цикла программы: run_mvc(). Сделан топором WHILE TRUE. (смотрю в сторону PyQT5 и asyncio, но не уверен, что они предназначены именно для этого. PyQT5 может предоставить систему сигнал-слотов, а asyncio предназначен для проектирования сервера через сокеты, или нет...)

Выделен модуль бизнес-логики: Model <- <b>WebMinersBarracks.py</b>. Для реализации, скорее всего, понадобится подключение библиотек HTML-запросов (requests) и обработки JSON (запросы к stackoverflow возвращают json)

Реализация View: <b>MasterMiner.py</b>

Описание "запроса" как типа данных выделен в отдельную задачу. Проектирование класса: <b>Query</b>.

<b>~09.04.2016</b>

Разработчик: "Команда Ракета"

Команда ракета: Фёдоров Юрий, Нигматуллин Рамис, Габбасов Даниил.

Разработка ПО, которое предоставляет функционал «умного» поиска. Специализированный поисковик (в нашем случае, ориентированный на программный код).

Нас интересуют не алгоритмы поиска информации в сети Интернет, а алгоритмы анализа данных, полученных в результате запроса, и формулировка самих запросов.

Чем сильнее сузится область поиска, тем меньше факторов придётся учитывать при разработке необходимых алгоритмов. Первое тематическое ограничение уже наложено: нас интересует та часть публичного интернета, в которой можно найти фрагменты кода и информацию, связанную с программированием.

Выбран конкретный ресурс: http://stackoverflow.com/

Развития, путём расширения области поиска (т.е. добавления поиска по новым ресурсам) не предполагается. Цель — написать максимально эффективное и изящное клиентское приложение для поиска по stackoverflow.

Диалог, который приложение ведёт с пользователем, основан на функциях API сайта: https://api.stackexchange.com/docs

Как это работает? MVC: Представление -> Диалог -> Формирование запроса -> Передача запроса в Модель -> Обработка запроса Моделью -> Обновление Представления -> Конец -> Представление -> Диалог -> Формирование запроса -> ...

Инструменты и технологии: Python.
