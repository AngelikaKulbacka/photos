from flask import Flask
from endpoints.ping import ping_bp
from endpoints.gallery import gallery_bp

app = Flask(__name__)
app.register_blueprint(ping_bp)
app.register_blueprint(gallery_bp)

if __name__ == '__main__':
    app.run()
