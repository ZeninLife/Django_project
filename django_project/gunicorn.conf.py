
bind = 'unix:/run/gunicorn.sock'  # Socket binding
workers = 4                        # Number of Gunicorn worker processes
accesslog = 'django_project/gunicorn/access.log'
errorlog = 'django_project/gunicorn/error.log'
