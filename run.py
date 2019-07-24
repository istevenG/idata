import os
from app import create_app
from setting import DevConfig, ProdConfig

CONFIG = ProdConfig if os.environ.get('FLASK_DEBUG') == 0 else DevConfig
app = create_app(CONFIG)

if __name__ == '__main__':
    app.run()
