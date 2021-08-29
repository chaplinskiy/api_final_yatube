# chaplinskiy/api_final_yatube

## Описание:

Сие есть проект 9го (в недавнем прошлом 10го) спринта факультета бэкенд-разработки Яндекс.Практикума. Он решает нетривиальную задачу допуска автора на следующий спринт. 

Польза – вполне очевидна.

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone https://github.com/chaplinskiy/api_final_yatube.git
```

```bash
cd api_final_yatube/
```

Cоздать и активировать виртуальное окружение:

```bash
python3 -m venv env
```

```bash
source env/bin/activate
```

```bash
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```bash
pip install -r requirements.txt
```

Выполнить миграции:

```bash
python3 manage.py migrate
```

Запустить проект:

```bash
python3 manage.py runserver
```
## Примеры:

Вывести список постов:

```json
/api/v1/posts/
```

Вывести список комментариев к посту:

```json
/api/v1/posts/{post_id}/comments/
```

### Весь функционал API:

```json
/redoc/
```