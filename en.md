The script cuts links with the help of the Bitly service and returns the statistics of navigation on them.

How to install

Python3 should already be installed. Then use pip (or pip3, there is a conflict with Python2) to install dependencies:
pip install -r requirements.txt

Launch

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


Project Goals
The code is written for educational purposes on online-course for web-developers dvmn.org.