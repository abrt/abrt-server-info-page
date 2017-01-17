import os

class Config(object):
    DEBUG = False
    TESTING = False
    ADMINS = "mail.admins"
    MAIL_SERVER = "localhost"
    MAIL_PORT = "25"
    MAIL_USERNAME = None
    MAIL_PASSWORD = None
    BRAND_TITLE = "ABRT"
    BRAND_SUBTITLE = "Server"
    URL_FOR_FAF = "https://retrace.fedoraproject.org/faf/summary/"
    URL_FOR_RS = None
    MORE_FAF = None
    MORE_RS = None
    MORE_ABRT = None
    MORE_GABRT = None
    MORE_LR = None
    MORE_SATYR = None

