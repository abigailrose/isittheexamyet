from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    header = "<h1>Has the EECS485 exam started yet?</h1>"
    answer = ""

    current_time = datetime.datetime.now()
    if current_time.month == 12 and current_time.day == 14:
        answer = "<p>yes</p>"
    else:
        answer = "<p>no</p>"

    response = header + answer
    return response

if __name__ == "__main__":
    app.run(debug=True)