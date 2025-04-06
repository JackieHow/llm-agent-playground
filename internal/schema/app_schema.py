from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired,Length

class CompletionReq(FlaskForm):
    query = StringField("query",validators=[
        DataRequired(message="用户的提问是必填的"),
        Length(max=2000,message="用户的提问不能超过2000个字符"),
    ])

