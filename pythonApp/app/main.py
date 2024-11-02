from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def ProcessData():
    return '<h2 style="color:black;">Hello There, <br><br>This is docker based Python Flask! <br><br>Demo Application version 1.0<br><br>18-Nov-2023 09:00 PM IST PM</h2>'

if __name__ == '__main__':
    app.run(port=80)
    
