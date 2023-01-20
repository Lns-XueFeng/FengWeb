from flask_wtf import FlaskForm, CSRFProtect
from wtforms import PasswordField, StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField("账号", validators=[DataRequired(), Length(1, 20)])
    password = PasswordField("密码", validators=[DataRequired(), Length(1, 128)])
    remember = BooleanField("记住")
    submit = SubmitField("确认")


class NotesSubmit(FlaskForm):
    pass


class PassageSubmit(FlaskForm):
    pass


class PassageEdit(FlaskForm):
    pass


class MessageEdit(FlaskForm):
    pass


class MessageDelete(FlaskForm):
    pass
