from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about-css')
def about_css():
    return render_template('about-css.html')

@app.route('/favorite-course')
def favorite_course():
    print('Subject entered: ' + request.args.get('subject'))
    print('Course number entered: ' + request.args.get('course_number'))

    return render_template('favorite-course.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        print('First name entered: ' + request.form.get('first_name'))
        print('Last name entered: ' + request.form.get('last_name'))
        print('Email entered: ' + request.form.get('email'))
        print('Major entered: ' + request.form.get('major'))

        return render_template('contact.html', form_submitted=True)
    else:
        return render_template('contact.html')

if __name__ == '__main__':
    app.run()