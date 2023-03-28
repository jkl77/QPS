from flask import Flask, session, render_template, Response, request, url_for, flash, redirect

app = Flask(__name__)
appName = "QTMA Product Series"
pageName = ""

app.config['SECRET_KEY'] = 'AF92AF84692AE0661B1CE20B'

queensResMessages = [{'title': 'Brant House', 
                      'content': 'Single plus rooms are awesome!', 
                      'rating': '11111'}
            ]

queensCourseMessages = [{'title': 'COMM 151',
             'content': 'Not a fun class', 
                      'rating': '11'}
            ]

queensFoodMessages = [{'title': 'Leonard Dining Hall',
             'content': "Don't eat the eggs!!", 
                      'rating': '1'}
            ]

queensSocialMessages = [{'title': 'Homecoming (HOCO)',
             'content': "Best HOCO is Canada by far", 
                      'rating': '11111'}
            ]

westernMessages = [{'title': 'Party Life',
             'content': 'Queens wannabe 2/10'},
            {'title': 'Message Two',
             'content': 'Message Two Content'},
            {'title': 'Message Three',
             'content': 'Message Three Content'},
            ]

@app.route('/', methods=('GET', 'POST'))
def index():
     if request.method == 'POST':
         if request.form.get('btn-fs') == 'QUEENS_U':
             pageName = "Queens University"
         elif request.form.get('btn-do') == 'WESTERN_U':
             pageName = "Western University"
         else:
             pass
     elif request.method == 'GET':
         return render_template('index.html', appName=appName)
     return render_template('index.html')

@app.route('/queensHP', methods=('GET', 'POST'))
def queensHP():
     if request.method == 'POST':
         if request.form.get('btn-fs') == 'QUEENS_U':
             pageName = "Queens University"
         elif request.form.get('btn-do') == 'WESTERN_U':
             pageName = "Western University"
         else:
             pass
     elif request.method == 'GET':
         return render_template('queensHP.html', appName=appName)
     return render_template('queensHP.html')

@app.route('/queensRes', methods=('GET', 'POST'))
def queensRes():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        rating = request.form['rating']

        if not title:
            flash('Residence name is empty!')
        elif not content and rating == "":
            flash('Content and rating are empty!')
        elif not content:
            flash('Content is empty!')
        elif not title and not content:
            flash('Residence name and content are empty!')
        elif rating == "":
            flash('Rating is empty!')
        elif not title  and rating == "":
            flash('Residence name and rating are empty!')
        elif not title and not content and rating == "":
            flash('Residence name, content, and rating are empty!')
        else:
            queensResMessages.append({'title': title, 'content': content, 'rating': rating})
            return redirect(url_for('queensRes'))
    return render_template('queensRes.html', appName=appName, queensResMessages=queensResMessages)

@app.route('/queensCourse', methods=('GET', 'POST'))
def queensCourse():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        rating = request.form['rating']

        if not title and not content:
            flash('Course code and content are empty!')
        elif not title:
            flash('Course code is empty!')
        elif not content and rating == "":
            flash('Content and rating are empty!')
        elif not content:
            flash('Content is empty!')
        elif rating == "":
            flash('Rating is empty!')
        elif not title  and rating == "":
            flash('Residence name and rating are empty!')
        elif not title and not content and rating == "":
            flash('Residence name, content, and rating are empty!')
        else:
            queensCourseMessages.append({'title': title, 'content': content, 'rating': rating})
            return redirect(url_for('queensCourse'))
    return render_template('queensCourse.html', appName=appName, queensCourseMessages=queensCourseMessages)

@app.route('/queensFood', methods=('GET', 'POST'))
def queensFood():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        rating = request.form['rating']

        if not title and not content:
            flash('Food location and content are empty!')
        elif not title:
            flash('Food location is empty!')
        elif not content and rating == "":
            flash('Content and rating are empty!')
        elif not content:
            flash('Content is empty!')
        elif rating == "":
            flash('Rating is empty!')
        elif not title  and rating == "":
            flash('Residence name and rating are empty!')
        elif not title and not content and rating == "":
            flash('Residence name, content, and rating are empty!')
        else:
            queensFoodMessages.append({'title': title, 'content': content, 'rating': rating})
            return redirect(url_for('queensFood'))
    return render_template('queensFood.html', appName=appName, queensFoodMessages=queensFoodMessages)

@app.route('/queensSocial', methods=('GET', 'POST'))
def queensSocial():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        rating = request.form['rating']

        if not title and not content:
            flash('Event name and content are empty!')
        elif not title:
            flash('Event name is empty!')
        elif not content and rating == "":
            flash('Content and rating are empty!')
        elif not content:
            flash('Content is empty!')
        elif rating == "":
            flash('Rating is empty!')
        elif not title  and rating == "":
            flash('Residence name and rating are empty!')
        elif not title and not content and rating == "":
            flash('Residence name, content, and rating are empty!')
        else:
            queensSocialMessages.append({'title': title, 'content': content, 'rating': rating})
            return redirect(url_for('queensSocial'))
    return render_template('queensSocial.html', appName=appName, queensSocialMessages=queensSocialMessages)

@app.route('/western', methods=('GET', 'POST'))
def western():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title and not content:
            flash('Title and content are empty!')
        elif not title:
            flash('Title is empty!')
        elif not content:
            flash('Content is empty!')
        else:
            westernMessages.append({'title': title, 'content': content})
            return redirect(url_for('western'))
    return render_template('western.html', appName=appName, westernMessages=westernMessages)

if __name__ == "__main__":
  app.run(debug=True)
