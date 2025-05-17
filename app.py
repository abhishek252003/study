from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/year/<int:year>')
def subjects(year):
    # Static subjects for demo
    subjects_by_year = {
        1: ['Maths', 'Physics', 'Chemistry'],
        2: ['Data Structures', 'DBMS', 'OOP'],
        3: ['CN', 'OS', 'DAA'],
        4: ['AI', 'ML', 'IoT']
    }
    subjects = subjects_by_year.get(year, [])
    return render_template('subjects.html', year=year, subjects=subjects)

@app.route('/subject/<subject>')
def materials(subject):
    return render_template('materials.html', subject=subject)

if __name__ == '__main__':
    app.run(debug=True)
