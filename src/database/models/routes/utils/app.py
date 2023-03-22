from flask import Flask 

from config import config

app = Flask(__name__)

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()

# activar el servidor:  . env/bin/activate
# desactivar el servidor: deactivate

# debug mode on: python ./src/database/models/routes/utils/app.py