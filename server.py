from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = ("berries and cream")

@app.route('/')
def index ():
    if 'counter' in session:
        session['counter'] = session['counter'] + 1
        session['visits'] = session['visits'] + 1
    else: 
        session['counter'] = 1
        session['visits'] = 1
    return render_template("index.html", counter = session['counter'])


@app.route('/destroy_session', methods=["POST"])
def destroy_session():
    if 'counter' in session:
        session.clear()
    else:
        session['counter'] = 1
    return redirect('/')

@app.route('/count', methods=["POST"])
def count_by_2():
    if 'counter' in session: 
        session['counter'] += 1
    else:
        session['counter'] = session['counter']
    return redirect('/')

@app.route('/increase_by', methods=['POST'])
def choose_amount():
    if 'counter' in session:
        session['counter'] += int(request.form['how_much'])
    else: 
        session['counter'] = session['counter']
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)