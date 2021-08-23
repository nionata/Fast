import os

def isProd():
    return os.getenv('ENIVORNMENT') == 'production'

def getVar(var):
    return os.getenv(var)