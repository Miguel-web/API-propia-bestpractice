from flask import Flask 

from config import config

app = Flask(__name__)


def page_not_found(error):
    return "<hi>Not found page</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Error Handlers
    app.register_error_handler(404, page_not_found)
    app.run()

# activar el servidor:  . env/bin/activate
# desactivar el servidor: deactivate

# debug mode on: python ./src/database/models/routes/utils/app.py
# Si hay un error de sintaxys , hay que repetir en la terminal el comando: debug mode on