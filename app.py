from flask import Flask, session, render_template, Response, request, url_for, flash, redirect

app = Flask(__name__)
appName = "QTMA Product Series"
pageName = ""

app.config['SECRET_KEY'] = 'AF92AF84692AE0661B1CE20B'

queensMessages = [{'title': 'Gord-Brock',
             'content': 'Overall pretty mid 5/10'},
            {'title': 'Message Two',
             'content': 'Message Two Content'},
            {'title': 'Message Three',
             'content': 'Message Three Content'},
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

@app.route('/queens', methods=('GET', 'POST'))
def queens():
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
            queensMessages.append({'title': title, 'content': content})
            return redirect(url_for('queens'))
    return render_template('queens.html', appName=appName, queensMessages=queensMessages)

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
