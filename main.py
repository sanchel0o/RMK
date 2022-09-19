from flask import (
    Flask,
    render_template,
    request
)
from res.work_with_file import (
    read_csv,
    sorting,
    merge
)
from res.work_with_db import (
    conn_to_db,
    extract_data
)

first_file = read_csv('files//volume.csv')
second_file = read_csv('files//machine.csv')

volumes = sorting(first_file)
machines = sorting(second_file)
merged = merge(volumes, machines)

connection, cursor = conn_to_db()
data = extract_data()


app = Flask(__name__)


@app.route('/')
def index():
    # l = len(data['Дата'])
    # first_date = data['Дата'][0]
    # last_date = data['Дата'][-1]
    return render_template('forms.html')


@app.route('/', methods=['POST'])
def index_form():
    length = len(data['Дата'])

    start_date = request.form['trip-start']
    end_date = request.form['trip-end']
    print(data['Дата'][0])
    print(type(data['Дата'][0]))
    print(start_date)
    ind = 0

    return render_template('index.html',
                           d=data,
                           start=start_date,
                           end=end_date,
                           len=length)


if __name__ == '__main__':
    app.run()
