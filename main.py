import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Template

# ============================================================================================== #

# Формируем текст письма по шаблону
def template_modify(c_name, c_email):
    
    fileread = open("templates/test.txt", encoding="utf-8").read()
    filemodify = Template(fileread).render(client_name=c_name, client_email=c_email)
    return filemodify

# Отправляем письмо
def send_email_to_client(addr_from, password, addr_to, email_subject, email_body):

    msg            = MIMEMultipart()                        # Создаем сообщение
    msg['From']    = addr_from                              # Адресат
    msg['To']      = addr_to                                # Получатель
    msg['Subject'] = email_subject                          # Тема сообщения
    msg.attach(MIMEText(email_body, 'plain'))               # Добавляем в сообщение текст

    server = smtplib.SMTP('smtp.gmail.com', 587)            # Создаем объект SMTP
    server.starttls()                                       # Начинаем шифрованный обмен по TLS
    server.login(addr_from, password)                       # Получаем доступ
    server.send_message(msg)                                # Отправляем сообщение
    server.quit()                                           # Логаут

# ============================================================================================== #

send_email_to_client('Адресат',                             # Адресат
                     'Пароль',                              # Пароль
                     'Получатель',                          # Получатель
                     'Тема письма',                         # Тема письма
                     template_modify('Имя клиента',         #
                                     'Емайл клиента'))      # Текст письма
