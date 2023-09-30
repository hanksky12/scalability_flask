from flask_cors import CORS

from .extension import Extension, FlaskApp
from commons.utils.config import ConfigUtil

extension = Extension()
extension.log_init()
extension.sql_init()
docs = extension.generate_flaskapispec()


def create_app():
    FlaskApp().create()
    app = FlaskApp().app

    config_obj = ConfigUtil.get()
    app.config.from_object(config_obj)

    from .controller.main import main_bp
    app.register_blueprint(main_bp)

    from .controller.api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    # print(app.url_map)
    docs.init_app(app)

    if ConfigUtil.get_env_config() == "development":
        CORS(app, supports_credentials=True)

    return app
