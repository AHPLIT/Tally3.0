from app import app
from flask import render_template
from app.forms import TallyForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/youth', methods=['GET', 'POST'])
def youth_info_queries():
    form = TallyForm()
    return render_template('youth_services.html', title="youth", form=form)
