# coding:utf-8
import random
import string

from users.models import EmailVerifyRecord

from django.core.mail import send_mail
from MxOnline.settings import EMAIL_FROM


def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    random_str = generate_random_str(16)

    email_record.code = random_str
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ''
    email_body = ''

    if send_type == 'register':
        email_title = '注册激活链接'
        email_body = '请点击链接以激活账户: http://127.0.0.1/active/{0}'.format(random_str)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass


def generate_random_str(length=8):
    salt = ''.join(random.sample(string.ascii_letters + string.digits, length))
    return salt