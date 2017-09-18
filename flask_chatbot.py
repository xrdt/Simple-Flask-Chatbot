from flask import Flask, render_template, request

user_responses = []
bot_responses = []

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def basic_greeting():
    global user_responses, bot_responses

    if request.method == 'POST':
        user_responses.append(request.form['input'])
        bot_responses.append(generate_response(request.form['input']))
        return render_template('form.html', user=user_responses, \
                response=bot_responses)
    if request.method == 'GET':
        return render_template('form.html')

def generate_response(user_input):
    # Repeats what the user says.
    return user_input
