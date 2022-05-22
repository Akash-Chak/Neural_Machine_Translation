from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired,length


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)

class modelForm(FlaskForm):
    name = TextAreaField('Enter Hindi Text', validators=[DataRequired(),length(max=200)])
    submit = SubmitField('Submit')




@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

from model import translation_task
@app.route('/translation',methods=['GET', 'POST'])
def translation():
    text = ''
    form = modelForm()
    if form.validate_on_submit():
        text = form.name.data
        text = translation_task(text)
    return render_template('form.html',form=form,name=text)