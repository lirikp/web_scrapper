# web_scrapper

Технические требования для WEB_SCRAPPER:

1. Машина с операционной системой UBUNTU с версией не ниже 18.04
2. Права SUDO
3. Установленный DOCKER и DOCKER-COMPOUSE https://docs.docker.com/compose/install/
А так же зависимые библиотеки для него.
4. Подключенный INTERNET

Инструкция по установке.
1. Клонировать репозиторий в удобную для вас папку
# git clone git@github.com:lirikp/web_scrapper.git

2. Зайти в каталог репозитория cd web_scrapper
3. Запустить сборку и создание машины коммандой:
# sudo docker-compose up --build -d
4. После отработки комманды, (около 1-2мин на 1 процессорной машине и 8GB) проверить запущена ли она коммандой:
# sudo docker ps
5. Если в списке присутствует одна запись запущенной машины с названием scrapper, запустить консоль на этот полученный хост
#sudo docker exec -it bash scrapper
6. Ручной запуск загрузчика новостей или установка работы по CRONTAB
6.1 В ручную загрузчик новостей можно запустить коммандой
# /usr/bin/python3 /home/scrapper/main.py
По окончании работы скрипта появится сообщение о количестве отгруженных сообщений в базу
6.2 Для установки работы по CRONTAB в консоли хоста наберите комманду > crontab -e
откроется редактор VIM, далее поместите строку указанную ниже в конец файла.
*/5 * * * *     d=`date`; echo $d >> /tmp/scrapper.log; /usr/bin/python3 /home/scrapper/main.py >> /tmp/scrapper.log

6.2.1 Перезапустите CRON коммандой из консоли # service restart cron
6.2.2 После успешного перезапуска наберите комманду # cat /tmp/scrapper.log. Если в логе появляются свежие записи, загрузка заработала успешно.


WEB_SCRAPPER technical requirements:

1. OS: UBUNTU version 18.04 or higher
2. SUDO rights
3. Installed DOCKER and DOCKER-COMPOUND https://docs.docker.com/compose/install/
As well as dependent libraries for it.
4. Connected INTERNET

Installation instruction.
1. Clone the Git repository into a convenient folder
# git clone git@github.com:lirikp/web_scrapper.git
2. Move to the cd web_scrapper repository directory
3. Run the build of machine using the command:
# sudo docker-compose up --build -d
4. After working out the command, (about 1-2min on 1 processor machine and 8GB) check whether it is started by the command:
# sudo docker ps
5. If the list contains one string of the running machine named scrapper, re-launch the console to this received host
#sudo docker exec -it bash scrapper
6. Manually starting the news loader or the CRONTAB software instalation
6.1 You can manually  run the news loader using the command
# /usr/bin/python3 /home/scrapper/main.py
At the end of the script, you will see a message about the number of messages sent to the database
6.2 To install crontab in the host console, type the command  
> crontab -e
The VIM editor opens, then place the line specified below at the end of the file.
*/5 * * * * d=`date`; echo $d >> /tmp/scrapper.log; /usr/bin/python3 /home/scrapper/main.py >> /tmp/scrapper.log

6.2.1 Restart CRON using the command
# service restart cron console
6.2.2 After a successful restart, type the command 
# cat /tmp/scrapper.log.
 If there are new entries in the log, the download was successful.
