from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy function to return a response for the chatbot
def get_Chat_response(input):
    # Dummy implementation, replace with actual chatbot logic
    return "This is a dummy response for: " + input

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    return get_Chat_response(input)

if __name__ == '__main__':
    app.run(debug=True)
