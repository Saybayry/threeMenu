# tree menu
This is an application for creating a django tree menu without using third-party libraries

upload the application to the project folder
```
git clone https://github.com/Saybayry/threeMenu.git
```

add the app to INSTALLED_APPS
```python
INSTALLED_APPS = [
    ...
    'treeMenu',
    ...]
```
perform migrations
```python
python manage.py makemigrations 
python manage.py migrate
```
create a menu using the admin panel

insert the menu on the page
```python
 {% draw_menu 'main_menu' %}
```
![итоговый вид меню](https://i.imgur.com/PW1zBhn.png=10x20)
