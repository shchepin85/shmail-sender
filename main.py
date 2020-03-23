# ======================== БИБЛИОТЕКИ ======================== #
 
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from jinja2 import Template, Environment, meta
 
 
# ======================== ФУНКЦИИ =========================== #
 
# Выбор шаблона из списка файлов
def shmailer_template_select():
 
    template_files_directory = os.path.join (os.getcwd(),'templates')
    template_files_list      = os.listdir   (template_files_directory)
    print('\nСписок шаблонов для писем:')
    for template_file_name in template_files_list:
        print (template_files_list.index(template_file_name), ': ', template_file_name)
    template_selected_file_id     = int(input('Введите номер шаблона: '))
    template_selected_file_path   = os.path.join (template_files_directory,
                                                  template_files_list[template_selected_file_id])
    template_selected_file_object = open(template_selected_file_path, encoding='utf-8').read()
    return template_selected_file_object
 
# Извлечение из шаблона списка переменных
def shmailer_template_parse(file_object):
 
    template_enviroment = Environment()
    template_ast        = template_enviroment.parse(file_object)
    template_variables  = dict.fromkeys(meta.find_undeclared_variables(template_ast), None)
    return template_variables
 
# Модификация шаблона
def shmailer_template_modify(file_object, template_variables):

    for key in template_variables.keys():
        template_variables[key] = input("Введите значение для '" + key + "': ")
        template_file_modified  = Template(file_object).render(template_variables.items())
    return template_file_modified

# Отправка письма
def shmailer_email_send(email_body):

    print('\nВведите данные для отправки письма!')
    email_from    = input('От кого     : ')
    email_to      = input('Кому (email): ')
    email_subject = input('Тема письма : ')

    msg            = MIMEMultipart()
    msg['From']    = email_from
    msg['To']      = email_to
    msg['Subject'] = email_subject
    msg.attach(MIMEText(email_body, 'html'))
  
    server_smtp     = ''
    server_port     = 0
    server_login    = ''
    server_password = ''

    server = smtplib.SMTP(server_smtp, server_port)
    server.starttls()
    server.login(server_login, server_password)
    server.send_message(msg)
    server.quit()

    print('\nEmail отправлен!')
    return True


# ======================== ОСНОВНОЙ ЦИКЛ ===================== #

# Добавить цикл
shmailer_template_selected  = shmailer_template_select ()
shmailer_template_variables = shmailer_template_parse  (shmailer_template_selected)
shmailer_template_modified  = shmailer_template_modify (shmailer_template_selected, 
                                                        shmailer_template_variables)
shmailer_send_result        = shmailer_email_send      (shmailer_template_modified)
shmailer_exit               = input('\nНажмите Enter, что бы завершить программу')
