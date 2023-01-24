from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import PasswordField, StringField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length

from fengweb.models import Category


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
    title = StringField("文章标题", validators=[DataRequired(), Length(1, 128)])
    # author = StringField("文章作者", validators=[DataRequired(), Length(1, 20)], default="回到古代见李白")
    category = SelectField("文章分类", coerce=int, default=1)
    body = TextAreaField("文章内容", validators=[DataRequired()])
    submit = SubmitField("确认")

    def __init__(self, *args, **kwargs):
        super(PassageSubmit, self).__init__(*args, **kwargs)
        self.category.choices = [(category.id, category.name)
                                 for category in Category.query.order_by(Category.name).all()]


class PassageEdit(PassageSubmit):
    pass


class MessageEdit(FlaskForm):
    name = StringField("名字", validators=[DataRequired(), Length(1, 20)])
    about = TextAreaField("留言", validators=[DataRequired()])
    submit = SubmitField("确认")
