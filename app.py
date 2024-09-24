from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages

# Correct answers for each question
correct_answers_q1 = ["print(10 + 5)", "System.out.println(10 + 5);", "cout << 10 + 5 << endl;"]
correct_answers_q2 = ["print(multiply(2, 5))", "System.out.println(2 * 5);", "cout << 2 * 5 << endl;"]
correct_answers_q3 = ["print(15 - 10)", "System.out.println(15 - 10);", "cout << 15 - 10 << endl;"]

@app.route('/question1', methods=['GET', 'POST'])
def question1():
    if request.method == 'POST':
        solution = request.form['solution'].strip()
        if solution in correct_answers_q1:
            return redirect(url_for('question2'))
        else:
            flash('Incorrect answer, please try again.')
            return render_template('question1.html', error=True)
    return render_template('question1.html')

@app.route('/question2', methods=['GET', 'POST'])
def question2():
    if request.method == 'POST':
        solution = request.form['solution'].strip()
        if solution in correct_answers_q2:
            return redirect(url_for('question3'))
        else:
            flash('Incorrect answer, please try again.')
            return render_template('question2.html', error=True)
    return render_template('question2.html')

@app.route('/question3', methods=['GET', 'POST'])
def question3():
    if request.method == 'POST':
        solution = request.form['solution'].strip()
        if solution in correct_answers_q3:
            flash('Correct! You have completed the challenge!')
            return redirect(url_for('success'))
        else:
            flash('Incorrect answer, please try again.')
            return render_template('question3.html', error=True)
    return render_template('question3.html')

@app.route('/success')
def success():
    return 'Congratulations! You have successfully completed the challenge.'

if __name__ == '__main__':
    app.run(debug=True)
