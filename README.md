# Как запустить на ПК

Выбираем, куда будем кланировать (например на диск B в папку TEST_PROJECT)

```bash
cd /B/TEST_PROJECT
```

Клонируем проект:

```bash
git clone https://github.com/Vettel12/api_yamdb-master
```

Заходим в директорию проекта:

```bash
cd /api_yamdb-master
```

Устанавливаем виртуальное окружение:

```bash
python -m venv venv
```

Активируем виртуальное окружение:

```bash
source venv/Scripts/activate
```

> Для деактивации виртуального окружения выполним (после работы):
> ```bash
> deactivate
> ```

Устанавливаем зависимости:

```bash
python -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

Применяем миграции:

```bash
python yatube/manage.py makemigrations
python yatube/manage.py migrate
```

Для запуска тестов выполним:

```bash
pytest
```

Получим:

```bash
ollected 31 items

tests/test_01_users.py::Test01UserAPI::test_01_users_not_auth PASSED                                                                                                    [  3%]
tests/test_01_users.py::Test01UserAPI::test_02_users_username_not_auth PASSED                                                                                           [  6%]
tests/test_01_users.py::Test01UserAPI::test_03_users_me_not_auth PASSED                                                                                                 [  9%] 
tests/test_01_users.py::Test01UserAPI::test_04_users_get_auth PASSED                                                                                                    [ 12%]
tests/test_01_users.py::Test01UserAPI::test_05_users_post_auth PASSED                                                                                                   [ 16%]
tests/test_01_users.py::Test01UserAPI::test_06_users_username_get_auth PASSED                                                                                           [ 19%]
tests/test_01_users.py::Test01UserAPI::test_07_users_username_patch_auth PASSED                                                                                         [ 22%]
tests/test_01_users.py::Test01UserAPI::test_08_users_username_delete_auth PASSED                                                                                        [ 25%]
tests/test_01_users.py::Test01UserAPI::test_09_users_check_permissions PASSED                                                                                           [ 29%]
tests/test_01_users.py::Test01UserAPI::test_10_users_me_get PASSED                                                                                                      [ 32%]
tests/test_01_users.py::Test01UserAPI::test_11_users_me_patch PASSED                                                                                                    [ 35%]
tests/test_02_category.py::Test02CategoryAPI::test_01_category_not_auth PASSED                                                                                          [ 38%] 
tests/test_02_category.py::Test02CategoryAPI::test_02_category PASSED                                                                                                   [ 41%]
tests/test_02_category.py::Test02CategoryAPI::test_03_category_delete PASSED                                                                                            [ 45%]
tests/test_02_category.py::Test02CategoryAPI::test_04_category_check_permission PASSED                                                                                  [ 48%]
tests/test_03_genre.py::Test03GenreAPI::test_01_genre_not_auth PASSED                                                                                                   [ 51%]
tests/test_03_genre.py::Test03GenreAPI::test_02_genre PASSED                                                                                                            [ 54%]
tests/test_03_genre.py::Test03GenreAPI::test_03_genres_delete PASSED                                                                                                    [ 58%]
tests/test_03_genre.py::Test03GenreAPI::test_04_genres_check_permission PASSED                                                                                          [ 61%]
tests/test_04_title.py::Test04TitleAPI::test_01_title_not_auth PASSED                                                                                                   [ 64%] 
tests/test_04_title.py::Test04TitleAPI::test_02_title PASSED                                                                                                            [ 67%]
tests/test_04_title.py::Test04TitleAPI::test_03_titles_detail PASSED                                                                                                    [ 70%]
tests/test_04_title.py::Test04TitleAPI::test_04_titles_check_permission PASSED                                                                                          [ 74%]
tests/test_05_review.py::Test05ReviewAPI::test_01_review_not_auth PASSED                                                                                                [ 77%]
tests/test_05_review.py::Test05ReviewAPI::test_02_review PASSED                                                                                                         [ 80%]
tests/test_05_review.py::Test05ReviewAPI::test_03_review_detail PASSED                                                                                                  [ 83%]
tests/test_05_review.py::Test05ReviewAPI::test_04_reviews_check_permission PASSED                                                                                       [ 87%]
tests/test_06_comment.py::Test06CommentAPI::test_01_comment_not_auth PASSED                                                                                             [ 90%]
tests/test_06_comment.py::Test06CommentAPI::test_02_comment PASSED                                                                                                      [ 93%]
tests/test_06_comment.py::Test06CommentAPI::test_03_review_detail PASSED                                                                                                [ 96%]
tests/test_06_comment.py::Test06CommentAPI::test_04_comment_check_permission PASSED                                                                                     [100%]

============================================================================ 31 passed in 10.23s ============================================================================= 
```

Создать суперпользователя:

```bash
python manage.py createsuperuser
```

Запустить проект:

```bash
python manage.py runserver
```

Запросы:

http://127.0.0.1:8000/redoc/ - вся информация

http://127.0.0.1:8000/api/v1/auth/email/ - для получения confirmation_code на переданный email
http://127.0.0.1:8000/api/v1/auth/token/ - для получения JWT-токена в обмен на email и confirmation_code

http://127.0.0.1:8000/api/v1/users/ - Получить список всех пользователей (GET). Права доступа: Администратор 
http://127.0.0.1:8000/api/v1/users/ - Создание пользователя (POST). Права доступа: Администратор
http://127.0.0.1:8000/api/v1/users/{username}/ - Получить пользователя по username (GET). Права доступа: Администратор
http://127.0.0.1:8000/api/v1/users/{username}/ - Изменить данные пользователя по username (PATCH). Права доступа: Администратор
http://127.0.0.1:8000/api/v1/users/{username}/ - Удалить пользователя по username (DELETE). Права доступа: Администратор.
http://127.0.0.1:8000/api/v1/users/me/ - Получить данные своей учетной записи (GET). Права доступа: Любой авторизованный пользователь
http://127.0.0.1:8000/api/v1/users/me/ - Изменить данные своей учетной записи (PATCH). Права доступа: Любой авторизованный пользователь

http://127.0.0.1:8000/api/v1/categories/ - Получить список всех категорий (GET). Права доступа: Доступно без токена
http://127.0.0.1:8000/api/v1/categories/ - Создать категорию (POST). Права доступа: Администратор
http://127.0.0.1:8000/api/v1/categories/{slug}/ - Удалить категорию (DELETE). Права доступа: Администратор

http://127.0.0.1:8000/api/v1/genres/ - Получить список всех жанров (GET). Права доступа: Доступно без токена
http://127.0.0.1:8000/api/v1/genres/ - Создать жанр (POST). Права доступа: Администратор
http://127.0.0.1:8000/api/v1/genres/{slug}/ - Удалить жанр (DELETE). Права доступа: Администратор

http://127.0.0.1:8000/api/v1/titles/ - Получить список всех объектов (GET). Права доступа: Доступно без токена
http://127.0.0.1:8000/api/v1/titles/ - Создать произведение для отзывов (POST). Права доступа: Администратор
http://127.0.0.1:8000/api/v1/titles/{titles_id}/ - Информация об объекте (GET). Права доступа: Доступно без токена
http://127.0.0.1:8000/api/v1/titles/{titles_id}/ - Обновить информацию об объекте (PATCH). Права доступа: Администратор
http://127.0.0.1:8000/api/v1/titles/{titles_id}/ - Удалить произведение (DELETE). Права доступа: Администратор

http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/ - Получить список всех отзывов (GET). Права доступа: Доступно без токена
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/ - Создать новый отзыв (POST). Права доступа: Аутентифицированные пользователи
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/ - Получить отзыв по id (GET). Права доступа: Доступно без токена
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/ - Частично обновить отзыв по id (PATCH). Права доступа: Автор отзыва, модератор или администратор
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/ - Удалить отзыв по id (DELETE). Права доступа: Автор отзыва, модератор или администратор

http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/ - Получить список всех комментариев к отзыву по id (GET). Права доступа: Доступно без токена
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/ - Создать новый комментарий для отзыва (POST). Права доступа: Аутентифицированные пользователи
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/ - Получить комментарий для отзыва по id (GET). Права доступа: Доступно без токена
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/ - Частично обновить комментарий к отзыву по id (PATCH). Права доступа: Автор комментария, модератор или администратор
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/ - Удалить комментарий к отзыву по id (DELETE). Права доступа: Автор комментария, модератор или администратор