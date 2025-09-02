from flask import Flask
from flask_cors import CORS
import os
from flask_sqlalchemy import SQLAlchemy
from backend.routes.recommend import recommend_bp
from backend.routes.submit import submit_bp
from backend.routes.history import history_bp
from backend.routes.pay import pay_bp
from backend.models import db
from backend.auth import auth_bp
from backend.feedback import feedback_bp

app = Flask(__name__)
CORS(app)

# MySQL config (update with your credentials or use .env)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('MYSQL_URI', 'mysql+pymysql://root:F21/2519/2020@localhost:3306/smart_crop')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'devsecret')

db.init_app(app)

# Register Blueprints for modular routing
app.register_blueprint(recommend_bp)
app.register_blueprint(submit_bp)
app.register_blueprint(history_bp)
app.register_blueprint(pay_bp)

app.register_blueprint(auth_bp)
app.register_blueprint(feedback_bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
