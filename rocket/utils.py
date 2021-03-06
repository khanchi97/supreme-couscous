'''This file will contain utility functions which are required
in the project.'''

import random
from django.core.mail import send_mail
from .models import (
    user_activation_cache,
    password_forget_cache,
)

MAIL_ID = 'Rockets!'


def checkmail(mailid):
    '''It checks whether a mail ID is university's valid email ID
    or not. If not it returns False otherwise it will return the
    entry number parsed from that email ID.'''

    # TODO: Improve the following email Id parser
    if mailid.endswith('@smvdu.ac.in'):
        return mailid[:-12]
    return False


def send_forget_email(user):
    '''This handles everything related to confirmation
    email which is send to the users email ID.'''

    mailid = user.email
    unique_hash = random_hash()
    message = "Reset your password by going here someurl.com/resetpass/%s" % unique_hash
    subject = 'Reset your password | Rocket'
    #send_mail(subject, message, MAIL_ID, [mailid], False)
    password_forget_cache.objects.create(user=user, unique_hash=unique_hash)


def send_confirm_email(user_object):
    '''This handles everything related to confirmation
    email which is send to the users email ID.'''

    mailid = user_object.email
    fname = user_object.first_name
    lname = user_object.last_name
    message, unique_hash = prepare_message(fname, lname, mailid)
    subject = 'Confirm your email ID | Rocket'
    #send_mail(subject, message, MAIL_ID, [mailid], False)
    user_activation_cache.objects.create(user=user, unique_hash=unique_hash)


def prepare_message(fname, lname, mailid):
    '''This prepares the message which is sent to the user
    for confirming the email. This also includes preparing a
    random hash which will be given as an url.'''

    rhash = random_hash()
    message = "Hey " + fname + " " + lname + ",\nThanks for joining the rockets.\
				We here tend to change the world by starting with our own university.\
				You can confirm your email ID by visiting this link\
				someurl.com/activate/" + rhash + "\nFor any queries feel free to ping us\
				at someemail@someurl.com"
    return message, rhash


def random_hash():
    '''This prepares a random hash.'''
    return "%032x" % random.getrandbits(random.randint(120, 128))
