ТЗ (с почином кста)

этот репозиторий создан с целью мотивации к созданию бекэндера)

так вот. если кратко, то этот проект - простейший бэкенд (если не будет 
лень - то и фронтенд) корпоративной сети компании, берущей деньги вкладчиков
и инвестирующей в крипту

если брать по функционалу - 4 (пока) бд
1. стэк:
на мой субъективный взгляд, под этот проект чудесно ложится django -бэй, drf 
(django rest framework) - API, bs4 (beautiful soup 4) для парсинга цен и 
requests для получения страниц для последующего парсинга, smtplib.

2. Таблицы в бд
запросы будут как при помоще ORM django так и на sql
итого 4 таблицы в бд
3. Функционал
    3.1 Просмотр активных заказов, персонала, клиентов
    будет реализован на одтельно странице при помощи запроса в бд с возмож-
    ностью фильтрации по имени, id

    3.2 страница с отправкой сообщений на email с корпоративной почты (рассылка)
    для конкретного человека или по фильтрации

    3.3 возможность удалять\добавлять\изменять рабочий состав

