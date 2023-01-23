from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import PasswordField, StringField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField("账号", validators=[DataRequired(), Length(1, 20)])
    password = PasswordField("密码", validators=[DataRequired(), Length(1, 128)])
    remember = BooleanField("记住")
    submit = SubmitField("确认")


class LeftWords(FlaskForm):
    name = StringField("名字", validators=[DataRequired(), Length(1, 20)])
    words = TextAreaField("话语", validators=[DataRequired()])
    submit = SubmitField("提交")


class UploadMarkdown(FlaskForm):
    file = FileField("Markdown", validators=[FileRequired(), FileAllowed(["md"])])
    submit = SubmitField("上传")


class PassageSubmit(FlaskForm):
    pass


class PassageEdit(FlaskForm):
    pass


class MessageEdit(FlaskForm):
    pass


class MessageDelete(FlaskForm):
    pass
