# -*- coding=UTF-8 -*-
import smtplib
from email.headers import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from config.conf import get_email_args


email_args = get_email_args()
smtp_server = email_args['server']
smtp_port = email_args['port']
from_addr = email_args['from']
from_password = email_args['password']
to_addr = email_args['to']
email_subject = email_args['subject']
warning_info = email_args['warning_info']


def __format_addr(nick_addr):
    name, addr = parseaddr(nick_addr)
    return formataddr((Header(name, 'UTF-8').encoder(), addr))


def gen_msg(cont, subject, from_nick=None, to_nick=None):
    if from_nick is None:
        from_nick = from_addr
    if to_nick is None:
        to_nick = to_addr
    msg = MIMEText(cont, 'plain', 'UTF-8')
    msg['From'] = __format_addr('{} <{}>'.format(from_nick, from_addr))
    msg['to'] = __format_addr('{} <{}>'.format(to_nick, to_addr))
    msg['subject'] = Header(subject).encode()
    return msg


def send_email(from_nick='weibospider', to_nick='SpiderUser'):
    msg = gen_msg(warning_info, email_subject, from_nick, to_nick)
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(from_addr, from_password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
