import os
from werkzeug.security import (
    generate_password_hash, 
)
from werkzeug.utils import secure_filename
from flask import current_app as app
from delivery.ext.auth.models import User
from delivery.ext.db import db

ALG = "pbkdf2:sha256"

def create_user(email: str, passwd: str, admin: bool = False) -> User:
    user = User(
        email=email, 
        passwd=generate_password_hash(passwd, ALG),
        admin=admin
    )
    db.session.add(user)
    # TODO : Tratar user exists exception
    db.session.commit()
    return user

def save_user_foto(filename, filestorage):
    """
    Saves user foto in
    ./uploads/foo/asdasd.ext
    """
    filename = os.path.join(
        app.config["UPLOAD_FOLDER"], 
        secure_filename(filename)
    )
    # TODO
    # 1 - Verificar se o dir existe
    # 2 - criar o diretório
    filestorage.save(filename)