from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename

class UploadForm(FlaskForm):
    upload = FileField(
            'image', 
            validators = [
                FileRequired(),
                FileAllowed(['jpg', 'png'], 'Images only!')
            ]
    )