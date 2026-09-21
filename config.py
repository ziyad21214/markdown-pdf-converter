from flask import Flask
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-change-in-production'
    BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))
    TEMPLATE_FOLDER: str = os.path.join(BASE_DIR, 'templates')
    STATIC_FOLDER: str = os.path.join(BASE_DIR, 'static')
    UPLOAD_FOLDER: str = os.path.join(BASE_DIR, 'uploads')
    DOWNLOAD_FOLDER: str = os.path.join(BASE_DIR, 'downloads')

    @classmethod
    def init_app(cls, app: Flask) -> None:
        os.makedirs(cls.UPLOAD_FOLDER, exist_ok=True)
        os.makedirs(cls.DOWNLOAD_FOLDER, exist_ok=True)
        app.config['TEMPLATE_FOLDER'] = cls.TEMPLATE_FOLDER
        app.config['UPLOAD_FOLDER'] = cls.UPLOAD_FOLDER
        app.config['DOWNLOAD_FOLDER'] = cls.DOWNLOAD_FOLDER
