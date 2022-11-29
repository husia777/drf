# DRF Project 2

<h3>Backup БД файл postgres_localhost-2022_11_21_16_05_34-dump.sql</h3>

<h3>Команды создания и заполнения таблиц </h3>
./manage.py makemigrations ads
<br>
./manage.py migrate
<br>
./manage.py load_data
<br>

<h3>шаг 1</h3>
URL для создания пользователя
http://127.0.0.1:8000/user/create/

{   
"first_name":"Хусейн",
"last_name":"Хусейн",
"username":"husia777",
"password":"sasa222",
"location":["Tobolsk"],
"role":"moderator",
"age":"22"
}</h3>
<h4> проверка обновления и создания юзера</h4>

<h3>шаг 2</h3>
URL для проверки 2 шага
http://127.0.0.1:8000/location/

<h3>шаг 3</h3>  
1 http://127.0.0.1:8000/ad?cat=1
<br>
2 http://127.0.0.1:8000/ad?text=принципы
<br>
3 http://127.0.0.1:8000/ad?location=Москва
<br>

<h3>шаг 4</h3>

http://127.0.0.1:8000/ad?price_from=100&price_to=100

