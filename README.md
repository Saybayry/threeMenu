# tree menu
Create django the menu  without using libraries

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
