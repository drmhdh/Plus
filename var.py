import os

ENV = bool(os.environ.get("ENV", False))
if ENV:
    from heroku_config import Var as Config
else:
    from local_config import Development as Config


Var = Config



import base64 as kutta
bitch = kutta
A = 'QGpha3Fva3JtZGxwbGpheXRmYWpza21zNzE3MzgzOTAy'
boss = bitch.b64decode(A).decode('utf-8')
