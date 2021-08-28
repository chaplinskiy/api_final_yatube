### Описание:

Сие есть проект 9го (в недавнем прошлом 10го) спринта факультета бэкенд-разработки Яндекс.Практикума. Он решает нетривиальную задачу допуска автора на следующий спринт. Польза – вполне очевидна.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/chaplinskiy/api_final_yatube.git
```

```
cd api_final_yatube/
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
### Примеры:

Вывести список постов:

```
/api/v1/posts/
```

Вывести список комментариев к посту:

```
/api/v1/posts/{post_id}/comments/
```

Весь функционал API:

```
/redoc/
```