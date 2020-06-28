from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index(): return redirect(url_for('insert_info_method', page_type='default'))


@app.route('/method', methods=['GET'])
def insert_info_method():
    METHOD = request.args.get('page_type')
    if METHOD == 'excel': return render_template('method_excel.html')
    elif METHOD == 'self': return render_template('method_self.html')
    else: return render_template('index.html')  # METHOD : default


@app.route('/excel_processing', methods=['POST'])
def excel_processing():
    EXCEL_FILE = request.form['excel_file']


@app.route('/self_processing', methods=['POST'])
def self_processing():
    pass


if __name__ == '__main__':
    app.run()

