
import smtplib                                      # Библиотека для SMTP
from email.mime.multipart import MIMEMultipart      # Многокомпонентный объект
from email.mime.text import MIMEText                # Текст/HTML
from email.mime.image import MIMEImage              # Изображения
from jinja2 import Template                         # Объект Template из шаблонизатора jinja2


# ФУНКЦИЯ - Прочитать шаблон из файла и модифицировать его

def template_modify(c_name, c_email):
    fileread = open("templates/test.txt", encoding="utf-8").read()
    filemodify = Template(fileread).render(client_name=c_name, client_email=c_email)
    return filemodify

# ФУНКЦИЯ - Отправить письмо

def send_email_to_client(addr_from, password, addr_to, email_subject, email_body):

    msg            = MIMEMultipart()                        # Создаем сообщение
    msg['From']    = addr_from                              # Адресат
    msg['To']      = addr_to                                # Получатель
    msg['Subject'] = email_subject                          # Тема сообщения
    msg.attach(MIMEText(email_body, 'plain'))               # Добавляем в сообщение текст

    server = smtplib.SMTP('smtp.gmail.com', 587)            # Создаем объект SMTP
    ####server.set_debuglevel(True)                         # Включаем режим отладки
    server.starttls()                                       # Начинаем шифрованный обмен по TLS
    server.login(addr_from, password)                       # Получаем доступ
    server.send_message(msg)                                # Отправляем сообщение
    server.quit()                                           # Выходим

    return print("Email отправлен!")

# От винта!

send_email_to_client('shchepin85@gmail.com',                # Адресат
                     'J#QQ$h7h2v2hch4',                     # Пароль
                     'shchepin85@gmail.com',                # Получатель
                     'Тема письма',                         # Тема письма
                     template_modify('Имя клиента',         #
                                     'Емайл клиента'))      # Текст письма