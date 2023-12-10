# Installing the project

1. Install Django: pip3 install -r requirements.txt
2. Copy .env.example to .env
3. Adjust DATABASE_URL in the .env file to match local Postgres user
4. Create an empty database in Postgres called finance_test (`psql -d postgres` then `CREATE DATABASE finance_test;`)
5. Run migrations via `python3 manage.py migrate`

# Running the developer's environment

1. `python3 manage.py createsuperuser`
2. `python3 manage.py runserver`

# Running tests

1. `python3 manage.py test`


The query for the test task can be found in operations/views/ 

# Задание
в системе имеются сущности: 
- кредитная заявка 
- контракт  
- товар 
- производитель 
 
Задания:  
1) создать модели в Django для вышеупомянутых сущностей, учитывая, что у  кредитной 
заявки может быть: 
 - только один контракт 
 -  несколько товаров  
каждый отдельно взятый товар связан только с одной заявкой 
  
у товара - только один производитель 
у каждой модели есть поле "дата создания",  проставляется в момент создания обьекта 
при создании связей с другими моделями  можно указать related_name 
  
  
2) Дано:  id   контракта (например 32812) 
 получить из обьектов модели кредитной заявки (!!!) уникальные id производителей всех 
товаров, которые связаны с этим контрактом 
  
при выполнении постараться минимизировать обращение к базе данных 
использовать git, результат залить на любой репозиторий, например github 
