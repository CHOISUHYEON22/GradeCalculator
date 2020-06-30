from flask import Flask, render_template, request, redirect, url_for
from calc import grade_calc, average_grade

app = Flask(__name__)
#google colab

@app.route('/')
def index(): return redirect(url_for('insert_info_method', page_type='default'))


@app.route('/method', methods=['GET'])
def insert_info_method():
    METHOD = request.args.get('page_type')

    if METHOD == 'self': return redirect(url_for('method_self', num_of_subjects='1'))
    elif METHOD == 'excel': return redirect(url_for('method_excel'))
    else: return render_template('index.html')  # METHOD : default


@app.route('/method_excel')
def method_excel(): return render_template('method_excel.html')


@app.route('/excel_processing', methods=['POST'])
def excel_processing():
    EXCEL_FILE = request.files['excel_file']
    print(EXCEL_FILE)
    print(type(EXCEL_FILE))


@app.route('/self_set_num_of_subjects', methods=['POST'])
def self_set_num_of_subjects():
    return redirect(url_for('method_self', num_of_subjects=request.form['num_of_subjects']))


@app.route('/method_self', methods=['GET'])
def method_self():
    num_of_subjects = request.args.get('num_of_subjects')
    name = ('과목_', 'subject_name', 'ranking', 'same_ranking_num', 'student_num', 'semester_hour')
    name_of_ques_with_index = (tuple(f'{j}{i}' for j in name) for i in range(int(num_of_subjects)))
    return render_template('method_self.html', name_of_ques_with_index=name_of_ques_with_index, num_of_subjects=num_of_subjects)


@app.route('/self_processing', methods=['POST'])
def self_processing():
    num_of_subjects = request.form['num_of_subjects']
    name = ('subject_name', 'ranking', 'same_ranking_num', 'student_num', 'semester_hour')
    input_data = tuple(tuple(request.form[f'{j}{i}'] for j in name) for i in range(int(num_of_subjects)))
    grade = {i[0]: grade_calc(int(i[1]), int(i[2]), int(i[3])) for i in input_data}
    average = average_grade(tuple(int(j[0]) for j in grade.values()), tuple(int(i[4]) for i in input_data))
    return render_template('result.html', grade=grade, average=average)


if __name__ == '__main__':
    app.run()


