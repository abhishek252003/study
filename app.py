from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/cisco')
def cisco():
    return render_template('cisco.html')

@app.route('/year/<int:year>')
def subjects(year):
    # Static subjects for demo
    subjects_by_year = {
        1: [
    'Mathematics-I',
    'Mathematics-II',
    'Engineering Physics',
     'Data Structures / Python Programming',
    'Engineering Chemistry',
    'Basic Electrical Engineering',
    'Basic Electronics Engineering',
    'Engineering Mechanics',
    'Engineering Graphics',
    'Programming for Problem Solving',
    'Environmental Science',
    'Workshop Practice',
    'Communication Skills'
],
        2:  [
    'Mathematics-III',
    'Data Structures',
    'Digital Electronics',
    'Computer Organization and Architecture',
    'Object-Oriented Programming (OOP)',
    'Discrete Mathematics',
    'Data Structures Lab',
    'Digital Electronics Lab',
    'Operating Systems',
    'Database Management Systems (DBMS)',
    'Design and Analysis of Algorithms (DAA)',
    'Software Engineering',
    'Microprocessors and Microcontrollers',
    'Environmental Engineering / Professional Ethics',
    'DBMS Lab',
    'Operating Systems Lab'
],
        3: [
    'Compiler Design',
    'Computer Networks',
    'Theory of Computation (Automata)',
    'Web Technologies',
    'Artificial Intelligence',
    'Software Project Management',
    'Computer Networks Lab',
    'Web Technologies Lab',
    'Machine Learning',
    'Cloud Computing',
    'Information Security / Cybersecurity',
    'Open Elective - I',
    'Open Elective - II',
    'Mini Project',
    'Industrial Training / Internship',
    'Machine Learning Lab'
],
        4:  [
    'Big Data Analytics',
    'Cloud Computing',
    'Information Security / Cybersecurity',
    'Blockchain Technology',
    'Mobile Application Development',
    'Data Mining',
    'Deep Learning',
    'Software Project Management',
    'Seminar / Technical Paper Presentation',
    'Project Phase I (Minor Project)',
    'Project Phase II (Major Project)',
    'Industrial Internship / Training',
    'Open Elective - III',
    'Professional Elective - I',
    'Professional Elective - II'
],
    }
    subjects = subjects_by_year.get(year, [])
    return render_template('subjects.html', year=year, subjects=subjects)

@app.route('/subject/<subject>')
def materials(subject):
    return render_template('materials.html', subject=subject)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use PORT env variable if available
    app.run(host='0.0.0.0', port=port, debug=True)
