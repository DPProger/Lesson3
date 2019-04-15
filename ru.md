Скрипт обрезает ссылки с помощью сервиса Битли и возвращает статистику переходов по ним.

Как установить

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
pip install -r requirements.txt

Запуск

    python main.py -h
    usage: main.py [-h] link
    
    Скрипт обрезает ссылки с помощью сервиса Битли и возвращает статистику
    переходов по ним.
    
    positional arguments:
      link        Введите ссылку
    
    optional arguments:
      -h, --help  show this help message and exit



    python main.py http://ya.ru вернет короткую ссылку bit.ly/2WgWYZL
    python main.py bit.ly/2WgWYZL вернет количество переходов по ссылке number of links = 3


Цель проекта
    Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.