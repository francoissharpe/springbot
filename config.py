import os
import random
import string


# test that auto merge and branche deletion works
class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = os.environ.get("SECRET_KEY",
                                default=''.join(random.choice(string.ascii_letters + string.digits) for i in range(16)))
    TESTING = os.environ.get("TESTING", default=True)
    DEBUG = os.environ.get("DEBUG", default=True)
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI",
                                             default=f"sqlite:///{os.path.join(BASE_DIR, 'test.db')}")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS", default=False)
