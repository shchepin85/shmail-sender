# ======================== ABOUT ============================= #

#   This utility can send email, formed from the selected HTML-template.
#   Preliminarily, you can prepare template and download it in the
#   '/template' folder.


# ======================== PREREQUISITES ====================== #

#   Python 3.5 or later
#   pip install Jinja2


# ======================== LICENSE =========================== #

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#   
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#   
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.


# ======================== LIBRARIES ========================= #
 
import os
import smtplib
from   email.mime.multipart import MIMEMultipart
from   email.mime.text      import MIMEText
# from email.mime.image     import MIMEImage
from   jinja2               import Template, Environment, meta 
 
 
# ======================== FUNCTIONS ========================= #
 
# Select template from the list of template files
def shmailer_template_select():
 
    template_files_directory      = os.path.join(os.getcwd(),'templates')
    template_files_list           = os.listdir  (template_files_directory)
    print(                          'List of templates:')
    for template_file_name in template_files_list:
        print(                      template_files_list.index(template_file_name), ':', 
                                    template_file_name)
    template_selected_file_id     = int(input   ('Input number of selected template: '))
    template_selected_file_path   = os.path.join(template_files_directory,
                                                 template_files_list[template_selected_file_id])
    template_selected_file_object = open        (template_selected_file_path, encoding='utf-8').read()
    return                          template_selected_file_object
 
# Parse keys (variables) from the selected template
def shmailer_template_parse(file_object):
 
    template_enviroment = Environment()
    template_ast        = template_enviroment.parse(file_object)
    template_variables  = dict.fromkeys            (meta.find_undeclared_variables(template_ast), None)
    return                template_variables
 
# Modify selected template
def shmailer_template_modify        (file_object, template_variables):

    for    key in                    template_variables.keys():
           template_variables[key] = input("Введите значение для '" + key + "': ")
           template_file_modified  = Template(file_object).render(template_variables.items())
    return template_file_modified

# Send email
def shmailer_email_send(email_body):

    print              ('Input additional information to send email!')
    email_from        = input('From         : ')
    email_to          = input('To           : ')
    email_subject     = input('Email subject: ')

    msg               = MIMEMultipart()
    msg['From']       = email_from
    msg['To']         = email_to
    msg['Subject']    = email_subject
    msg.attach(         MIMEText(email_body, 'html'))
  
    server_smtp       = ''
    server_port       = 0
    server_login      = ''
    server_password   = ''

    server            = smtplib.SMTP(server_smtp, server_port)
    server.starttls    ()
    server.login       (server_login, server_password)
    server.send_message(msg)
    server.quit        ()

    print              ('Email отправлен!')
    return              True


# ======================== MAIN CYCLE ======================== #

while(True):

    shmailer_template_selected  = shmailer_template_select()
    shmailer_template_variables = shmailer_template_parse (shmailer_template_selected)
    shmailer_template_modified  = shmailer_template_modify(shmailer_template_selected, 
                                                           shmailer_template_variables)
    shmailer_send_result        = shmailer_email_send     (shmailer_template_modified)
    shmailer_exit               = input                   ('press Enter')


# ======================== END =============================== #