import os

PROJECT_ENV = os.environ.setdefault('PROJECT_ENV', 'development')

if PROJECT_ENV in ('development', 'staging', 'production'):
    exec(f'from .{PROJECT_ENV} import *')
