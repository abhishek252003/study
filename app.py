from flask import Flask, render_template
import os

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

    port = int(os.environ.get('PORT', 5000))  # Use PORT env variable if available
    app.run(host='0.0.0.0', port=port)
