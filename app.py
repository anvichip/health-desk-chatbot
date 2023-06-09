from flask import Flask, render_template, request
#from bot_api import generate_response
#from lang_chain_bot import generate
#from prompt import handle_form_submission
from only_prompts import handle_form
from memory_bot import get_response
app = Flask(__name__)
chat_history = []

@app.route('/')
def home():
    # if request.method == 'POST':
    #     chat_history = []
    #     return render_template('index.html', chat_history=chat_history)
    
    return render_template('index.html', chat_history=chat_history)

# @app.route('/submit', methods=['POST'])
# def submit():
#     user_input = request.form['user_input']
#     response = generate_response(user_input)
#     chat_history.append({'user': user_input, 'bot': response})
#     return render_template('index.html', chat_history=chat_history)

@app.route('/submit', methods = ['POST'])
def submit():
    # user_input = request.form.get('user_input')
    condition = request.form.get('condition')
    severity = request.form.get('severity')
    message = request.form.get('message')
    response,user_input = handle_form(condition,severity,message)
    chat_history.append({'user': user_input, 'bot': response})
    return render_template('conversation.html',chat_history = chat_history)

@app.route('/chat',methods =['POST'])
def sub():
    message = request.form.get('message')
    response,user_input = handle_form('','',message)
    chat_history.append({'user': user_input, 'bot': response})
    return render_template('conversation.html',chat_history = chat_history)
    

# @app.route('/submit', methods=['POST'])
# def submit():
    # condition = request.form.get('condition')
    # severity = request.form.get('severity')
    # message = request.form.get('message')

#     # Check if both dropdown inputs are not empty
#     if condition and severity:
#         prompt = PromptTemplate(input_variables=['condition', 'severity', 'message'], template='write me a response for CONDITION: {condition}, SEVERITY: {severity}, MESSAGE: {message}')
#         response = prompt.run(condition=condition, severity=severity, message=message)
#     else:
#         response = message

#     return render_template('result.html', response=response)

# @app.route('/submit', methods=['POST'])
# def submit():
#     condition = request.form.get('condition')
#     severity = request.form.get('severity')
#     message = request.form.get('message')
#     output,history = handle_form_submission(condition,severity,message)
#     return render_template('conversation.html',response = output, history = history)

# def generate_response(user_input):
#     # Implement your chatbot logic here to generate a response based on the user input
#     # You can use any AI or rule-based techniques to generate the response
#     # For simplicity, let's just echo the user input as the bot's response
#     return user_input

if __name__ == '__main__':
    app.run(debug=True)
