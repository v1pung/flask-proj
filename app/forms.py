from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.fields.choices import SelectField
from wtforms.fields.simple import BooleanField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError

from .models.user import User


class RegForm(FlaskForm):
    name = StringField('ФИО', validators=[DataRequired(),
                                          Length(min=2, max=50)],
                       render_kw={
                           'class': 'form-control',
                           'placeholder': 'ФИО'
                       })
    login = StringField('Логин', validators=[DataRequired(),
                                             Length(min=2, max=16)])
    password = PasswordField('Пароль', validators=[DataRequired()])
    confirm_password = PasswordField('Подтвердите пароль', validators=[DataRequired(),
                                                                       EqualTo('password')])
    avatar = FileField('Загрузите свое фото', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField('Зарегистрироваться')

    def validate_login(self, login):
        user = User.query.filter_by(login=login.data).first()
        if user:
            raise ValidationError('Имя пользователя уже занято.')


class LoginForm(FlaskForm):
    login = StringField('Логин', validators=[DataRequired(),
                                             Length(min=2, max=16)])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class StudentForm(FlaskForm):
    student = SelectField('student', choices=[], render_kw={
        'class': 'form-control'
    })

class TeacherForm(FlaskForm):
    teacher = SelectField('teacher', choices=[], render_kw={
        'class': 'form-control'
    })
