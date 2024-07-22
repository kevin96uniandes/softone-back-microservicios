import logging
from flask_cors import CORS
from configuracion.configuracion import Config
from blueprints.actions import actions_blueprint


app = Config.init()

cors = CORS(app)

logging.basicConfig(level=logging.DEBUG)

app.register_blueprint(actions_blueprint, url_prefix='/api/clave_maestra')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3003, debug=True)