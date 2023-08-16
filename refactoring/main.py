# Мы устроились на новую работу. Бывший сотрудник начал разрабатывать модуль для работы с почтой,
# но не успел доделать его. Код рабочий. Нужно только провести рефакторинг кода.
#
# Создать класс для работы с почтой;
# Создать методы для отправки и получения писем;
# Убрать "захардкоженный" код. Все значения должны определяться как аттрибуты класса, либо аргументы методов;
# Переменные должны быть названы по стандарту PEP8;
# Весь остальной код должен соответствовать стандарту PEP8;
# Класс должен инициализироваться в конструкции.
# if __name__ == '__main__'
# Скрипт для работы с почтой.

import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart


class SendPostMail:

    def __init__(self):
        self.login = 'login@gmail.com'
        self.password = 'passwORD'
        self.GMAIL_SMTP = "smtp.gmail.com"
        self.GMAIL_IMAP = "imap.gmail.com"
        self.port = 587
        self.rfc = '(RFC822)'
        self.inbox_folder = "inbox"
        self.criterion = '(HEADER Subject "%s")' % header if header else 'ALL'

    def get_message(self, subject, recipients, message, header='None'):
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))
        return msg

    def send_message(self, msg):
        ms = smtplib.SMTP(self.GMAIL_SMTP, self.port)
        # identify ourselves to smtp gmail client
        ms.ehlo()
        # secure our email with tls encryption
        ms.starttls()
        # re-identify ourselves as an encrypted connection
        ms.ehlo()
        ms.login(self.login, self.password)
        ms.sendmail(self.login, ms, msg.as_string())
        ms.quit()

    def receive_message(self):
        mail = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
        mail.login(self.login, self.password)
        mail.list()
        mail.select(self.inbox_folder)
        result, data = mail.uid('search', None, self.criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, self.rfc)
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()


if __name__ == '__main__':

    email_login = SendPostMail()
    my_message = email_login.get_message('Subject', ['vasya@email.com', 'petya@email.com'], 'Message')
    email_login.send_message(my_message)
    email_login.receive_message()




# OLD CODE BEFORE REFACTOR
#
# GMAIL_SMTP = "smtp.gmail.com"
# GMAIL_IMAP = "imap.gmail.com"
#
# l = 'login@gmail.com'
# passwORD = 'qwerty'
# subject = 'Subject'
# recipients = ['vasya@email.com', 'petya@email.com']
# message = 'Message'
# header = None
#
#
# #send message
# msg = MIMEMultipart()
# msg['From'] = l
# msg['To'] = ', '.join(recipients)
# msg['Subject'] = subject
# msg.attach(MIMEText(message))
#
# ms = smtplib.SMTP(GMAIL_SMTP, 587)
# # identify ourselves to smtp gmail client
# ms.ehlo()
# # secure our email with tls encryption
# ms.starttls()
# # re-identify ourselves as an encrypted connection
# ms.ehlo()
#
# ms.login(l, passwORD)
# ms.sendmail(l,
# ms, msg.as_string())
#
# ms.quit()
# #send end
#
#
# #recieve
# mail = imaplib.IMAP4_SSL(GMAIL_IMAP)
# mail.login(l, passwORD)
# mail.list()
# mail.select("inbox")
# criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
# result, data = mail.uid('search', None, criterion)
# assert data[0], 'There are no letters with current header'
# latest_email_uid = data[0].split()[-1]
# result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
# raw_email = data[0][1]
# email_message = email.message_from_string(raw_email)
# mail.logout()
# #end recieve
#
#
#
